import cv2
import matplotlib.pyplot as plt

import argparse

parser = argparse.ArgumentParser(description='Input some file')
parser.add_argument(
    '--inp_path', dest='inp_path', type=str, help='input path'
)
parser.add_argument(
    '--out_path', dest='out_path', type=str, help='output path'
)
args = parser.parse_args()

img=cv2.imread(args.inp_path) #Path to input image

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.axis(False)

grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert_img=cv2.bitwise_not(grey_img)

blur_img=cv2.GaussianBlur(invert_img, (111,111),0)

invblur_img=cv2.bitwise_not(blur_img)

sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

cv2.imwrite(args.out_path, sketch_img)  #Generate output in .jpg
