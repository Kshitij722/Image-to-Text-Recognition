import easyocr
import cv2
import numpy as np
import matplotlib.pyplot as plt
def singleline():
        image_path = 'images/sign2.jpeg'

        render = easyocr.Reader(['en'], gpu=False)
        result = render.readtext(image_path)
        print(result)


        top_left = tuple(result[0][0][0])
        bottom_right = tuple(result[0][0][2])
        text = result[0][1]
        font = cv2.FONT_HERSHEY_PLAIN

        img = cv2.imread(image_path)
        img = cv2.rectangle(img, top_left, bottom_right, (255,0,0), 2)
        img = cv2.putText(img, text, top_left, font, .5, (0,255,0), 1, cv2.LINE_AA )
        plt.imshow(img)
        plt.show()


def multipleline():
        image_path = 'images/sign.png'

        render = easyocr.Reader(['en'], gpu=False)
        result = render.readtext(image_path)
        print(result)

        img = cv2.imread(image_path)
        for detection in result:
                top_left = tuple([int(val) for val in detection[0][0]])
                bottom_right = tuple([int(val) for val in detection[0][2]])
                text = detection[1]
                font = cv2.FONT_HERSHEY_PLAIN
                img = cv2.rectangle(img, top_left, bottom_right, (255,0,0), 2)
                img = cv2.putText(img, text, top_left, font, .5, (0,255,0), 1, cv2.LINE_AA)

        plt.figure(figsize=(10,10))
        plt.imshow(img)
        plt.show()

singleline()
multipleline()
        