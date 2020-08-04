import cv2
import pytesseract
import io
import numpy as np 
import cv2

def convert(file):
    ## Read the image using cv2.imread
    image_stream = io.BytesIO(file)
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    print(file_bytes)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    ## convert the read image document to text with the given configuration
    text=pytesseract.image_to_string(img,config=r"--oem 3 --psm 6")

    ## store the read text to file named image2text.txt
    with open("image2text.txt","w") as file:
        file.write(text)
        print( text)
    
    return text