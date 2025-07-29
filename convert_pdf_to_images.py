from pdf2image import convert_from_path
import os

pdf_path = "karur_vysya.pdf"  # 🔁 Your bank statement
output_folder = "karur_pages"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Convert PDF to images
images = convert_from_path(pdf_path, dpi=300)

# Save each page as PNG
for i, img in enumerate(images):
    img_path = os.path.join(output_folder, f"page_{i+1}.png")
    img.save(img_path, "PNG")
    print(f"✅ Saved {img_path}")