import pyperclip
import cv2
from PIL import ImageGrab

class Sensors:
    def __init__(self):
        self.name="asdf"

    def take_screenshot(self):
        path = 'screenshot.jpg'
        screenshot = ImageGrab.grab()
        rgb_screenshot = screenshot.convert('RGB')
        rgb_screenshot.save(path, quality=15)

    def web_cam_capture(self):
        web_cam = cv2.VideoCapture(0)
        if not web_cam.isOpened():
            print('Error: Camera dod not open successfully')
            exit()
        path = 'webcam.jpg'
        ret, frame = web_cam.read()
        cv2.imwrite(path, frame)

    def get_clipboard_text(self):
        clipboard_content = pyperclip.paste()
        if  isinstance(clipboard_content, str):
            return clipboard_content
        else:
            print('No clipboard text to copy')
            return None