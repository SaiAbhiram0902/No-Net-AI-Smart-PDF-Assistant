import pydantic
if hasattr(pydantic, "deprecated"):
    del pydantic.deprecated

from fastapi import FastAPI, UploadFile, File, HTTPException
import fitz  
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage
import os
import uvicorn

app = FastAPI()
model = ChatOllama(model="mistral")  # Uses local Mistral model from Ollama

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        return "\n".join([page.get_text() for page in doc])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text: {str(e)}")

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())  
        return {"filename": file.filename, "message": "File uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

@app.get("/ask/")
async def ask_question(filename: str, question: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    document_text = extract_text_from_pdf(file_path)
    response = model([HumanMessage(content=f"Document: {document_text}\n\nQ: {question}")])
    
    return {"answer": response.content}

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9090)
