try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pdf2image import convert_from_path
import tempfile
import time

with tempfile.TemporaryDirectory() as path:
    images = convert_from_path('./files/test.pdf', output_folder=path, dpi=80, thread_count=4,
                               jpegopt={"progressive": False, "optimize": False}, output_file='img',
                               fmt='jpeg'
                               )

word_list = ""
start = time.time()
for i, img in enumerate(images):
    word_list += pytesseract.image_to_string(img, lang='eng')

print(len(word_list.replace("\n", " ").split()))
print(time.time() - start)