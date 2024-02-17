import PyPDF2

# Open the PDF file in binary mode
with open('classificacao.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Iterate through each page
    for page_num in range(len(pdf_reader.pages)):
        # Extract text from the page
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        
        # Print or process the extracted text
        print(f"Page {page_num + 1}:")
        print(text)