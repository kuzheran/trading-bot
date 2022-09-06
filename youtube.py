import pafy
import cv2
from threading import Thread
import time

buy_template = cv2.imread('buy.png')
sell_template = cv2.imread('sell.png')
w, h = buy_template.shape[:-1]

def screenshot(image, i):
    cv2.imwrite(f"frames/{i}.png", image)
    print(f"Screenshot {i}.jpg")
    print(image)

def watch(link):
    i = 0
    video = pafy.new(link)
    best = video.getbest(preftype="mp4")
    capture = cv2.VideoCapture(best.url)

    while True:
        grabbed, frame = capture.read()

        if frame is None:
            break
        
        #frame = cv2.resize(frame, (1280, 720), interpolation = cv2.INTER_AREA)
        #cv2.imshow("Output Frame", frame)

        i += 1
        if i % 300 == 0:
            screenshot(frame, i)

        key = cv2.waitKey(1) & 0xFF

if __name__ == "__main__":
    watch("https://youtu.be/Onqre9MQK7c")