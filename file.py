from fastapi import FastAPI, UploadFile, File
from typing import List


app = FastAPI()

'''
#General file methods
@app.post("/upload")
async def endpoint(uploaded_file: UploadFile):
  fileName = uploaded_file.filename
  contentType = uploaded_file.content_type
  content = await uploaded_file.read()
  size = len(content)
  print(fileName, size, contentType, content)


#For processing huge files
@app.post("/upload")
async def endpoint(request: Request):
  async for data in request.stream():
    print(data)


#Uploading multiple files
@app.post("/multiple")
async def multiple_files(files: List[UploadFile] = File(...)):
  return {
    "files": [file.filename for file in files]
  }

'''