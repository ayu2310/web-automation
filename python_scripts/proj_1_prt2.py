#url image read
from selenium import webdriver
from selenium.webdriver import ActionChains

def img_to_text(url):
    import urllib.request
    import numpy as np
    import cv2

    #url = "https://cyberautics.co.in/QuestionsImages/102.PNG"
    url_response = urllib.request.urlopen(url)
    array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(array, 1)

    import pytesseract as tess
    from PIL import Image


    tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    text = tess.image_to_string(img, config='-c preserve_interword_spaces=1')

    from itertools import chain

    list = text.split('   ')

    list2 = []
    list3 = []
    list4 = []
    for element in list:
        if (len(element) >= 1):
            list2.append(element)

    for i in range(0, len(list2)):
        list3.append(list2[i].split('\n'))

    for element in list3:
        if (len(element) == 1):
            list4.append(element[0])
        elif (len(element) > 1):
            for i in element:
                list4.append(i)

    for element in list4:
        if (len(element) == 0):
            list4.remove(element)

    list5 = []
    for element in list4:
        list5.append(element.strip())

    return(list5)

    #return(list)



