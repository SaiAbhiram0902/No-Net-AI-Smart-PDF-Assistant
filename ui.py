import gradio as gr
import requests
import subprocess
import threading
import os

def start_backend():
    subprocess.Popen(["backend.exe", "--port", "9090"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

threading.Thread(target=start_backend, daemon=True).start()

BACKEND_URL = "http://127.0.0.1:9090"

def upload_pdf(file):
    if not file:
        return "", "Error: No file selected"
    
    file_name = os.path.basename(file.name) 
    with open(file.name, "rb") as f:
        response = requests.post(f"{BACKEND_URL}/upload/", files={"file": f})
    
    data = response.json()
    if response.status_code == 200 and "filename" in data:
        return data["filename"], "File uploaded successfully ✅"
    
    return "", "Upload failed ❌"

def ask_question(filename, question):
    if not filename:
        return "Error: No file uploaded. Please upload a file first."

    response = requests.get(f"{BACKEND_URL}/ask/", params={"filename": filename, "question": question})
    
    if response.status_code != 200:
        return "Error processing request ❌"

    return response.json().get("answer", "Error processing request ❌")

with gr.Blocks() as demo:
    gr.HTML("""
    <style>
        button[data-testid="block-api-button"] { display: none !important; }
    </style>
    <h1>📝 No-Net AI: Smart PDF Assistant 📝</h1>
    """)



    file = gr.File(label="Upload PDF")
    upload_button = gr.Button("Upload File")
    file_output = gr.Textbox(label="Uploaded Filename", interactive=False)  
    upload_status = gr.Textbox(label="Status", interactive=False)  

    upload_button.click(upload_pdf, inputs=file, outputs=[file_output, upload_status])

    question_input = gr.Textbox(label="Ask a question about the document")
    answer_output = gr.Textbox(label="Answer")
    ask_button = gr.Button("Get Answer")

    ask_button.click(ask_question, inputs=[file_output, question_input], outputs=answer_output)

demo.launch(server_name="127.0.0.1", server_port=7861, inbrowser=True, show_api=False)
