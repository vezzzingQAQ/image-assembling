import os

import cv2

import numpy as np

import PIL.Image as Image

import matplotlib.pyplot as plt

img_type = ['.jpg', '.JPG', '.png', '.PNG', '.bmp', '.BMP']  # 可继续添加图片类型

# 输入几行几列

ROW = 6

COL = 6


def resize_blank_img(srcimg, dstpath):

    img = cv2.imread(srcimg)

    blankimg = np.zeros(np.shape(img), np.uint8)

    blankimg[:, :, 0] = 255

    blankimg[:, :, 1] = 255

    blankimg[:, :, 2] = 255

    num = [os.path.join(dstpath, imgpath) for imgpath in os.listdir(
        dstpath) if os.path.splitext(imgpath)[1] in img_type]

    cv2.imwrite(dstpath + "\\" + str(len(num)+1) + ".jpg", blankimg)


def image_compose(image_path):

    if not os.path.isdir(image_path):

        return -1

    imgpath_vec = [os.path.join(image_path, imgpath) for imgpath in os.listdir(
        image_path) if os.path.splitext(imgpath)[1] in img_type]

    # 1、使用平均的width，heigth或者可以自定义width，heigth

    # 2、resize图片大小

    vec = [os.path.join(image_path, imgpath) for imgpath in os.listdir(image_path) if

           os.path.splitext(imgpath)[1] in img_type]

    while (len(vec)) < COL * ROW:

        vec = [os.path.join(image_path, imgpath) for imgpath in os.listdir(image_path) if

               os.path.splitext(imgpath)[1] in img_type]

        resize_blank_img(vec[0], image_path)

    imgs = []

    for item in vec:

        imgs.append((Image.open(item)))

    # 3、拼接成大图

    result_img = Image.new(imgs[0].mode, (3000 * COL, 2400 * ROW))

    index = 0

    for i in range(COL):

        for j in range(ROW):
            print(i, j,imgs[index])
            result_img.paste(imgs[index], (i * 3000, j * 2400))

            index += 1
    print("正在解析图像...")
    # 4、显示拼接结果
    result_img.save("result.png")

# result_img.save(path)#保存结果


if __name__ == "__main__":

    path = r'E:\classicClass\算法艺术\下载器7'  # 输入你的图片路径

    image_compose(path)
