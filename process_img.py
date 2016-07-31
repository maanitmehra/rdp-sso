import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def grid_img(src_img, dest_img, num_rows, num_cols):

     im = cv2.imread(src_img)
     try:
        try:
                row,col,chan = im.shape
        except:
                row,col = im.shape
                chan = 1

        overlay = im.copy()
        output = im.copy()

        GRID_NUM_COL = num_rows
        GRID_NUM_ROW = num_cols

        GRID_WIDTH = col/GRID_NUM_COL
        GRID_HEIGHT= row/GRID_NUM_ROW


        #Horizontal lines
        for i,c_idx in enumerate(range(0, col, GRID_WIDTH)):
                cv2.line(overlay, (c_idx,0), (c_idx,row-1), (0,255,255), 2)
                cv2.putText(overlay, "{}".format(chr(i+ord('A'))),(c_idx + (GRID_WIDTH/2),row-5), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 4)
        #Vertical lines
        for i,r_idx in enumerate(range(0, row, GRID_HEIGHT)):
                cv2.line(overlay, (0,r_idx), (col-1,r_idx), (0,255,255), 2)
                cv2.putText(overlay, "{}".format(i+1),(0, r_idx + (GRID_HEIGHT/2)), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 4)

        #saving image
        cv2.imwrite(dest_img, overlay)

     except:
		pass

SRC_DIR_LIST  = ["./photos1/", "./photos2/photos/", "./photos3/photos/"]

for SRC_DIR in SRC_DIR_LIST:
   DEST_DIR = "./grid_" + SRC_DIR[2:]

   src_list = os.listdir(SRC_DIR)

   for img in src_list:
        src_img = SRC_DIR+img
        dest_img= DEST_DIR+img[:-4]+"_grid"+img[-4:]

        grid_img(src_img, dest_img, 4, 4)


