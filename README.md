# 📊 PDF Extractor – Streamlit Frontend

This is the **frontend application** for the PDF Extractor project.  
It is built using **Streamlit** and interacts with the FastAPI backend to:
- Upload PDF files
- Display extracted text, tables, and images
- Download results as a ZIP file

---

## 🚀 Features
- Simple UI for uploading PDF files
- Displays **extracted text** (always shown first)
- Displays **tables** (converted to CSV) in order
- Displays **images** at the end
- Option to download all results as a `.zip` file

---

## 🛠️ Tech Stack
- **Streamlit** – frontend framework
- **Requests** – to communicate with FastAPI backend
- **FastAPI Backend** – handles PDF extraction, processing, and zipping

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Dipesh-Ydv/pdf-extractor-frontend.git
   cd pdf-extractor-frontend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. Start your **FastAPI backend** (make sure it’s running on `http://localhost:8000`):
   ```bash
   uvicorn app.main:app --reload
   ```

2. Start the **Streamlit frontend**:
   ```bash
   streamlit run app.py
   ```

3. Open the app in your browser:
   ```
   http://localhost:8501
   ```

---

## 📁 Project Structure
```
streamlit-frontend/
│── app.py                  # Main Streamlit app
│── requirements.txt        # Dependencies for frontend
│── README.md               # Project documentation
```

---

## ⚙️ Configuration
- By default, the frontend expects the backend to run at:
  ```
  http://localhost:8000/extract
  ```
- If deploying, update the backend URL inside `app.py`.

---

## 🐳 Docker (Optional)

1. Build the image:
   ```bash
   docker build -t pdf-extractor-frontend .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 pdf-extractor-frontend
   ```

---

## 📷 Screenshots
(Add screenshots of your app UI here once you run it.)

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License
This project is licensed under the MIT License.
