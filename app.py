import streamlit as st
import requests
import zipfile
import io
import os

BACKEND_URL = st.sidebar.text_input('Backend URL', value='http://localhost:8000')

st.title('PDF Extractor (text, tables, images)')

uploaded_file = st.file_uploader('Upload a PDF', type=['pdf'])

if uploaded_file:
    with st.spinner('Sending to backend...'):
        files = {'file': (uploaded_file.name, uploaded_file.getvalue(), 'application/pdf')}
        try:
            resp = requests.post(f"{BACKEND_URL}/api/extract", files=files, timeout=120)
            resp.raise_for_status()
            zip_bytes = resp.content
        except Exception as e:
            st.error(f'Error: {e}')
            st.stop()

    st.success('Extraction complete!')
    st.download_button(
        label="Download ZIP of extracted content",
        data=zip_bytes,
        file_name="extracted_content.zip",
        mime="application/zip"
    )

    # Optionally preview contents of the ZIP
    with zipfile.ZipFile(io.BytesIO(zip_bytes), 'r') as zipf:
        st.subheader("📦 ZIP Contents Preview")

        files = zipf.namelist()

        # Define priority order for preview
        def preview_order(fname):
            if fname.endswith('.txt'):
                return 0
            elif fname.endswith('.csv'):
                return 1
            elif any(fname.endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                return 2
            return 3  # fallback for other file types

        # Sort files based on our custom order
        files_sorted = sorted(files, key=preview_order)

        for fname in files_sorted:
            st.write(f"**{fname}**")
            
            if fname.endswith('.txt'):
                with zipf.open(fname) as f:
                    text = f.read().decode(errors='ignore')
                    st.text_area(fname, text, height=600)

            elif fname.endswith('.csv'):
                import pandas as pd
                with zipf.open(fname) as f:
                    df = pd.read_csv(f)
                    st.dataframe(df)

            elif any(fname.endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                from PIL import Image
                with zipf.open(fname) as f:
                    img = Image.open(f)
                    st.image(img, caption=fname, use_container_width=True)