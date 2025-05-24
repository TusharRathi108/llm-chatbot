import pypdf

# Load PDF
reader = pypdf.PdfReader(r'C:\Users\acer\Downloads\An-Autobiography.pdf')

# Total pages in the book
total_pages = len(reader.pages)

print(total_pages)

# Choose page
page = reader.pages[1]
print(page.extract_text())

# Extract raw text
# raw_text = page.extract_text()

# start_page = 0

# Read every page to make a paragraph out of it
# while start_page < total_pages:
#     page = reader.pages[start_page]
#     # text = page.extract_text()

#     print(f"Page: ", start_page)
#     if start_page == 556:
#         print("557th page")
      
#     start_page += 1

# Clean and format as paragraph
# lines = raw_text.split('\n')
# paragraph = ' '.join([line.strip() for line in lines if line.strip()])

# print(paragraph)