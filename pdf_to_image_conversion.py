# Dependencies
# ! pip install pdf2image
# ! sudo apt-get install poppler-utils

# Functionality: Read PDF and return images

from typing import List
from pdf2image import convert_from_path
from PIL import Image
from pydantic import FilePath, BaseModel

class PDFToImageModel(BaseModel):
    pdf_path: FilePath

class pdf_to_image:
  def __init__(self, pdf_path: str):
    self.pdf_path = pdf_path
    try:
      validate_data = PDFToImageModel(pdf_path=pdf_path)
    except Exception as e:
      raise Exception ('Your Path Fromat Is Wrong')

  def return_image_bytes(self) -> List[Image.Image]:
    pages_images: List[Image.Image] = convert_from_path(self.pdf_path)
    return pages_images

  def save_image(self, name: str) -> None:
    for idx, image in enumerate(self.return_image_bytes()):
      image.save(f'{name}_{idx + 1}.jpg', 'JPEG')

# convert_image = pdf_to_image('PDF_path')
# convert_image.save_image('invoice_DIN')
