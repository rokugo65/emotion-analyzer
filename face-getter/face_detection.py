import numpy as np
import cv2
import os

cascade_path = 'haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(cascade_path) 

cap = cv2.VideoCapture(0)

while True:
    # 内蔵カメラから読み込んだキャプチャデータを取得
    ret, frame = cap.read()

    # フレーム画像をグレースケールに変換
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 顔を検出
    faces = face_cascade.detectMultiScale(frame_gray)

    # 検出された顔を四角で囲む
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)

    # 表示
    cv2.imshow('frame', frame)

    # qキーが押されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()

