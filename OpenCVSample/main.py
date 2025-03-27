import cv2
import time

rtsp_url = ""

capture = cv2.VideoCapture()
capture.open(rtsp_url, cv2.CAP_FFMPEG)
# capture = cv2.VideoCapture(rtsp_url)
# capture.open()

width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)  # 视频宽度
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 视频高度
fps = capture.get(cv2.CAP_PROP_FPS)  # 视频FPS

while True:
    if not capture.isOpened():
        print("open media failed")
        continue

    success, frame = capture.read()

    if not success:
        print("read media failed")
        time.sleep(0.3)
        continue

    cv2.imshow("OpenCV Sample", frame)
    cv2.waitKey(30)
