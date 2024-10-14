import cv2

def web_cam_capture(self):
    web_cam = cv2.VideoCapture(0)
    if not web_cam.isOpened():
        print('Error: Camera dod not open successfully')
        exit()
    path = 'webcam.jpg'
    ret, frame = web_cam.read()
    cv2.imwrite(path, frame)