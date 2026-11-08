from pdf2epub import PDF2EPUB

# Set your file names
pdf_file = "name.pdf"
output_epub = "name.epub"

print("Starting conversion... (This may take a minute)")

# Initialize the converter
# Note: If you have an M1/M2/M3 Mac, use device="mps". 
# If you have an Intel Mac, use device="cpu".
converter = PDF2EPUB(pdf_file, device="mps") 

# 1. Extract text and images to Markdown
converter.convert_pdf_to_markdown()

# 2. Convert the Markdown to EPUB
converter.convert_markdown_to_epub(output_epub)

print(f"Done! Your file is saved as {output_epub}")
