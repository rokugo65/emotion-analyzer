import numpy as np
import cv2
import os

import argparse

import chainer
import chainer.links as L
import chainer.functions as F
from chainer import Variable

from network import LinearNet
from util import load_data, load_label

def predict(model, inputdata, labellist):
    """
    predict from image data
    """
    x = Variable(np.asarray([inputdata]))
    y = model.predictor(x)
    y = F.softmax(y)

    p_max = None
    index = None
    for i, p in enumerate(y.data[0]):
        if (p_max is None) or (p_max < p):
            p_max = p
            index = i
            label = labellist[index]
    return index, p_max, label

def importingargs():
    """
    Definition of args
    """
    parser = argparse.ArgumentParser("predicting using saved model")
    parser.add_argument("--first-hidden-layer-units", "-fu",
                        type=int, default=500,
                        help="the units num of first hidden")
    parser.add_argument("--second-hidden-layer-units", "-su",
                        type=int, default=100,
                        help="the units num of first hidden")
    parser.add_argument("--label-num", "-l", type=int, default=5)
    parser.add_argument("--modelpath", "-mf", help="model path")
    parser.add_argument("--labelfilepath", "-lf", help="labelfile")
    parser.add_argument("--imagefilepath", "-if",
                        help="imagefilepath you want to predict")
    args = parser.parse_args()
    return args.first_hidden_layer_units,\
            args.second_hidden_layer_units, args.label_num,\
            args.modelpath, args.labelfilepath, args.imagefilepath

if __name__ == "__main__":
    n_units_h1, n_units_h2, n_out,\
            modelpath, labelfilepath, imagefilepath = importingargs()
    model = L.Classifier(LinearNet(n_units_h1, n_units_h2, n_out))
    chainer.serializers.load_npz(modelpath, model)
    labellist = load_label(labelfilepath)

    cascade_path = 'haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path) 

    cap = cv2.VideoCapture(0)

    frame_count = 0
    face_count = 0

    while True:
        frame_count += 1
        face_count = 0

        # 内蔵カメラから読み込んだキャプチャデータを取得
        ret, frame = cap.read()

        exportPath = os.path.join('export', str(frame_count) + '.png')
        cv2.imwrite(exportPath,frame)

        # フレーム画像をグレースケールに変換
        frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # 顔を検出
        faces = face_cascade.detectMultiScale(frame_gray)

        # 検出された顔を四角で囲む
        for(x,y,w,h) in faces:
            dst = frame[y:y+h,x:x+w]
            dst = cv2.resize(dst,(128,128))
            dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
            dst = dst * 1.0 / 255
            img = np.array(dst,dtype='f4')
            index, prob, label = predict(model, img, labellist)
            print("index: %d, prob: %f, label: %s" % (index, prob, label))

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
            cv2.rectangle(frame, (x-1, y+h), (x+130, y+h+25), (255, 0, 255), -1)
            cv2.putText(frame, label,(x+2,y+h+20),5, 1,(255,255,255))

        # 表示
        cv2.imshow('frame', frame)

        # qキーが押されたら終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()