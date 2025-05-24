import fitz

# extract text from pdf file
def extractText(path,  skip_pages=0):
  document = fitz.open(path)
  
  # inside text of PDF
  full_text = ""

  for page_num in range(skip_pages, len(document)):
      page = document[page_num]
      full_text += page.get_text()
    
  return full_text.strip()


# split text in variable chunks
def createChunks(text, chunk_size):
  chunks = []
  for index in range(0, len(text), chunk_size):
    chunk = text[index:index+chunk_size].strip()
    chunks.append(chunk)
  return chunks

# Example
pdf_path = "C:\\Users\\acer\\Downloads\\progit.pdf"
text = extractText(pdf_path, 10)
chunks = createChunks(text, 1000)

# Display chunks (first five)
for index, chunk in enumerate(chunks[:]):
  print(f"---- Chunk {index + 1} ----\n{chunk}\n")



