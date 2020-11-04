#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 1:08
# @Author  : Xilun Wu
# @email   : nnuwxl@gmail.com
# @File    : Pic2Icon.py
import os
from PIL import Image
import numpy as np
import cv2
import sys
import time


class Picture:
    def __init__(self, file):
        self.ext = ['jpg', 'jpeg', 'png']
        self.files = [file]
        self.savepath = ""

    def handle_picture(self, file):
        print("Converting to four channel RGBA images...")
        time.sleep(0.5)

        img = Image.open(file).convert('RGBA')
        width = img.size[0]
        height = img.size[1]
        x = width / height
        matrix = np.asarray(img)
        print("The image resolution is being sampled at 2048x2048 size...")
        time.sleep(0.5)

        if width >= height:
            matrix = cv2.resize(matrix, (2048, int(2048 / x)))
            m = np.zeros((2048, 2048, 4), dtype=np.int)
            a = int(2048 / x)
            b = int((2048 - a) / 2)
            for i1 in range(2048):
                for i2 in range(2048):
                    if i1 >= b and i1 < b + a:
                        m[i1][i2] = m[i1][i2] + matrix[i1 - b][i2]


        else:
            matrix = cv2.resize(matrix, (int(x * 2048), 2048))
            m = np.zeros((2048, 2048, 4), dtype=np.int)
            a = int(2048 * x)
            b = int((2048 - a) / 2)
            for i1 in range(2048):
                for i2 in range(2048):
                    if i2 >= b and i2 < b + a:
                        m[i1][i2] = m[i1][i2] + matrix[i1][i2 - b]

        img = Image.fromarray(np.uint8(m), "RGBA")
        print("Output image in *.ico format...")
        time.sleep(0.5)
        savefile0 = os.path.dirname(self.files[0])
        savefile = os.path.join(savefile0, "Output_Icon")
        if os.path.exists(savefile) == False:
            print("Creating the output folder：{}".format(savefile))
            time.sleep(1)

            os.mkdir(savefile)
        savepath = (self.files[0].split('\\')[-1]).split('.')[0] + ".ico"
        savepath = os.path.join(savefile, savepath)
        img.save(savepath, sizes=[(int(2048), int(2048))], quality=100)
        print("Output complete:{}".format(savepath))
        time.sleep(1)
        self.savepath = savepath

    def run(self):
        for file in self.files:
            if os.path.exists(file) == False:
                print("Input image path error, please check and try again!")
                print(file)
                time.sleep(3)
                sys.exit(0)

            if file.split('.')[-1] not in self.ext:
                print("Sorry, the program does not support images in this format.")
                print("Surpported format: *.jpg, *.jpeg, *.png")
                time.sleep(3)
                sys.exit(0)

            if file.split('.')[-1] in self.ext:
                self.handle_picture(file)


if __name__ == "__main__":
    try:
        file = input("Please enter the path of the image:")
        if file[0] == '\"' and file[-1] == "\"":
            file = file[1:-1]
        file = r"{}".format(file)
        ins = Picture(file)
        ins.run()
        print("Opening the output Icon...")
        time.sleep(0.7)
        message = os.popen('\"{}\"'.format(ins.savepath))
        print("The conversion has been completed, and if it fails to open,\n"
              " it may be because your system does not have a default application to open the icon image.")
        print("\nProcess done。\n")
    except Exception as e:
        print("Something went wrong:\n{}".format(e))
        print("\nYou can send an error message and a screenshot of the program to the author's email for help\n")
    finally:
        print("Thank you for using this software.\n@Author : NNUwxl\n"
              "Having additional question can email me at : nnuwxl@gmail.com")
        input()
