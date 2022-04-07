import os
import shutil
import streamlit as st
from PIL import Image

st.header("Vegetables detection with YOLO and PyTorch")
st.write("Choose an image to detect vegetables (lettuce, potato, carrot, onion, garlic, leek and broccoli): ")

uploaded_file = st.file_uploader("Choose an image...")


if st.button('Send'):
    #os.system("conda activate testcv")
    #print(str(uploaded_file.name))
    image = Image.open(uploaded_file)
    st.image(uploaded_file, caption='Input Image', use_column_width=True)
    image.save("uploaded.png")
    os.system("python yolov5/detect.py --source ./uploaded.png --weights yolov5/runs/train/yolo_veg_det/weights/best.pt --conf 0.25 --name streamlit_veg_det")
    detected= Image.open("yolov5/runs/detect/streamlit_veg_det/uploaded.png")
    st.image(detected, caption='Output Image', use_column_width=True)
    shutil.rmtree("yolov5/runs/detect/streamlit_veg_det")
