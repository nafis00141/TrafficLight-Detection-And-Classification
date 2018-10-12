# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 01:19:40 2018

@author: NafiS

Example usage:
    python groundtruth_file_and_image.py input_yaml foldername
    python groundtruth_file_and_image.py t.yaml ground_truths_images
"""

import sys
import os
import cv2
import random
from read_label_file import get_all_labels
from PIL import Image

def try_ext(input_yaml , output_folder_image , output_folder_gt):
    
    images = get_all_labels(input_yaml)
            
    desired_dim = (1280,720)
    
    k = 1
    
    for i, image_dict in enumerate(images):
        
        print(k)
        
        image = cv2.imread(image_dict['path'])
        
        image = cv2.resize(image, desired_dim, interpolation=cv2.INTER_LINEAR)
        
        imgfilePath = output_folder_image+'/'+str(k)+'.png'
        
        cv2.imwrite(imgfilePath,image)
        
        filePath = output_folder_gt+'/'+str(k)+'.txt'
        
        out_file = open(filePath, 'w')
            
        
        for box in image_dict['boxes']:
            
            x0 = float(box['x_min'])
            y0 = float(box['y_min'])
            x1 = float(box['x_max'])
            y1 = float(box['y_max'])
            
            out_file.write("traffic_light " + str(x0) + " "+ str(y0) + " " + str(x1) + " " + str(y1) +  "\n")

        k = k + 1
        
if __name__ == '__main__':

    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(-1)
        
    label_file = sys.argv[1]
    output_folder_gt = sys.argv[2]
    output_folder_image = sys.argv[3]
    
    try_ext(label_file,output_folder_image,output_folder_gt)
