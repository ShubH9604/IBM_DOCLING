from docling.document_converter import DocumentConverter 

# Step 1: Initialize the converter
converter = DocumentConverter()

# Step 2: Convert the PDF
result = converter.convert("AAAcanara_epassbook_2025-06-27 082304.919155.pdf")

# Step 3: Access the document
doc = result.document

# Step 4: Export to plain text
plain_text_output = doc.export_to_text()
with open("AAAcanara_epassbook_2025-06-27 082304.919155.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(plain_text_output)
print("✅ Saved as 'AAAcanara_epassbook_2025-06-27 082304.919155.txt'")
