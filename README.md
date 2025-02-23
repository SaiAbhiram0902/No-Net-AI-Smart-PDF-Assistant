# No-Net-AI-Smart-PDF-Assistant
No-Net AI is an offline AI chatbot that provides human-like responses without internet access, ensuring data privacy and uninterrupted communication

## Features
- Fully offline operation, no internet required
- Automatic backend startup when running the UI
- Supports PDF uploads and AI-powered Q&A
- Simple and user-friendly interface

### **Prerequisites**
1. **Windows OS** (Tested on Windows)
2. **Python 3.8+** (Only needed for development)
3. **Ollama with Mistral-7B model** (Required for local AI processing)

## Installation  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/SaiAbhiram0902/No-Net-AI-Smart-PDF-Assistant
   cd No-Net-AI-Smart-PDF-Assistant
   ```
   
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Build Backend:**
   ```bash
   pyinstaller --onefile --hidden-import=pydantic --hidden-import=pydantic-core --hidden-import=pydantic.deprecated.decorator backend.py
   ```
   
4. **Build UI:**
   ```bash
   pyinstaller --clean ui.spec
   
5. **Run No-Net AI:**
   Navigate to the dist folder.
   Open No-Net AI.exe.

6. **Use No-Net AI:**
   Upload a PDF in the opened localhost page.
   Ask questions about the document.

**Notes:**

Ensure you do NOT manually start backend.exe before opening No-Net AI.exe, as it automatically launches the backend.
If backend.exe is already running, it will cause a port conflict on 9090. Restart your machine or close the existing backend process before running the UI.
The software is licensed under the MIT License, making it free and open-source for anyone to use and modify.
   

