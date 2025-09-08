import pytesseract
from PIL import Image
import os

folder_path = "content/"

# Output text file
output_file = "ocr_output.txt"

# Open the file in write mode
with open(output_file, "w", encoding="utf-8") as f:
    for img_file in os.listdir(folder_path):
        if img_file.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder_path, img_file)
            img = Image.open(img_path)

            # Extract text
            text = pytesseract.image_to_string(img)

            # Write image name and extracted text into file
            f.write(f"--- Text from {img_file} ---\n")
            f.write(text + "\n\n")

print(f"✅ OCR complete! Extracted text saved to {output_file}")
