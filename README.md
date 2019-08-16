# 表情認識やってみるプロジェクト

## requirements
python3  
opencv  
pillow  
chainer

## face-getter
カメラを起動して認識した顔を切り取ってexportにpngで保存する

## image-inflated
学習データの水増し  
importにあるpngを30パターンに水増ししてexportに保存

## generate-model
学習データからクラス分類モデルの生成

## face-detection
生成したモデルを使って顔認識
