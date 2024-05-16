import cv2
from ultralytics  import YOLO
from cv2 import getTickCount, getTickFrequency
import subprocess
import time

model = YOLO('weights/best.pt')
push_url = r"rtmp://192.168.50.47:1935/live/test-1"

# 在图像左上角添加FPS文本

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
text_color = (255,255,255) # 白色
text_position = (10, 30)

# 获取视频流
cap = cv2.VideoCapture()

while True:
    # result = cap.open("rtsp://admin:pa123456@192.168.50.74/h264/ch1/main/av_stream",cv2.CAP_FFMPEG)
    result = cap.open("rtmp://127.0.0.1:1935/live/test",cv2.CAP_FFMPEG)
    if not result:
        time.sleep(2)
        continue

    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    size_str = str(size[0])+'x'+ str(size[1])
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 视频编解码器
    fps = cap.get(cv2.CAP_PROP_FPS)  # 帧数
    file_writer = cv2.VideoWriter(str(time.time())+".mp4",fourcc=fourcc,fps=fps, frameSize=size)
    command = ['ffmpeg',
        '-y', '-an',
        '-f', 'rawvideo',
        # '-vcodec','rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', size_str,
        # '-r', '25',
        '-i', '-',
        '-c:v', 'nvenc_h264',
        # '-pix_fmt', 'yuv420p',
        # '-preset', 'ultrafast',
        '-f', 'flv',
        push_url]
    pipe = subprocess.Popen(command,shell=False,stdin=subprocess.PIPE)

    while cap.isOpened():
        loop_start = getTickCount()
        success,frame = cap.read() # 读取一帧图像

        # if success:
            # results = model.predict(source=frame,conf=0.3,device='0') # 对当前帧进行检测并显示结果

        # annotated_frame = results[0].plot()

        loop_time = getTickCount() - loop_start
        total_time = loop_time / (getTickFrequency())
        FPS = int(1/ total_time)

        fps_text = f"FPS: {FPS:.2f}"

        # cv2.putText(annotated_frame, fps_text, text_position, font, font_scale, text_color, font_thickness)
        cv2.imshow('img', frame)
        # file_writer.write(annotated_frame)
        # pipe.stdin.write(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

cap.release() # 释放流连接
pipe.terminate()
# cv2.destroyAllWindows() # 销毁窗口
