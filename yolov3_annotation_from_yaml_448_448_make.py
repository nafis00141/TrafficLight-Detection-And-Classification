# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:43:28 2018

@author: NafiS
Example usage:
    python yolov3_annotation_from_yaml_448_448_make.py input_yaml foldername
    python yolov3_annotation_from_yaml_448_448_make.py t.yaml obj
"""

import sys
import os
import cv2
from read_label_file import get_all_labels
from PIL import Image

def ir(some_value):
    """Int-round function for short array indexing """
    return int(round(some_value))

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

area1 = (0, 0, 448, 448)
area2 = (416, 0, 864, 448)
area3 = (832, 0, 1280, 448)

def try_ext(input_yaml, output_folder):
    
    w = int(448)
    
    h = int(448)
    
    images = get_all_labels(input_yaml)
            
    desired_dim = (1280,720)
    
    k = 1
    
    for i, image_dict in enumerate(images):
        
        print(k)
        
        if not image_dict['boxes']:
            continue


        image = cv2.imread(image_dict['path'])
        
        image = cv2.resize(image, desired_dim, interpolation=cv2.INTER_LINEAR)
        
        pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        cropped_img1 = pil_img.crop(area1)
        cropped_img2 = pil_img.crop(area2)
        cropped_img3 = pil_img.crop(area3)
        
        p1 = []
        p2 = []
        p3 = []
            
        
        for box in image_dict['boxes']:
            
            x0 = float(box['x_min'])
            y0 = float(box['y_min'])
            x1 = float(box['x_max'])
            y1 = float(box['y_max'])
            
            
            if x1-x0<=0 or y1-y0<=0:
                continue
            
            if((x0>=0 and x1<=448) and (y0>=0 and y1<=448)):
                
                b = (float(x0), float(x1), float(y0), float(y1))
            
                bb = convert((w,h), b)
                
                p1.append(bb)
                
                
            if((x0>=416 and x1<=864) and (y0>=0 and y1<=448)):
                
                b = (float(x0-416), float(x1-416), float(y0), float(y1))
            
                bb = convert((w,h), b)
            
                p2.append(bb)

            if((x0>=832 and x1<=1280) and (y0>=0 and y1<=448)):
                
                b = (float(x0-832), float(x1-832), float(y0), float(y1))
            
                bb = convert((w,h), b)
            
                p3.append(bb)
        
        if p1:
        
            filepath = output_folder+'/'+str(k)+'.txt'
            
            out_file = open(filepath, 'w')
            
            for bb in p1:
                out_file.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
            
            imagefilepath = output_folder+'/'+str(k)+'.png'
            
            cropped_img1.save(imagefilepath, 'PNG')
            
            k = k + 1
                
        if p2:
        
            filepath = output_folder+'/'+str(k)+'.txt'
            
            out_file = open(filepath, 'w')
            
            for bb in p2:
                out_file.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
            
            imagefilepath = output_folder+'/'+str(k)+'.png'
            
            cropped_img2.save(imagefilepath, 'PNG')

            k = k + 1
            
        if p3:
        
            filepath = output_folder+'/'+str(k)+'.txt'
            
            out_file = open(filepath, 'w')
            
            for bb in p3:
                out_file.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
            
            imagefilepath = output_folder+'/'+str(k)+'.png'
            
            cropped_img3.save(imagefilepath, 'PNG')
            
            k = k + 1
            
            
        if not p1:
            filepath = output_folder+'/'+str(k)+'.txt'
            
            out_file = open(filepath, 'w')
            
            imagefilepath = output_folder+'/'+str(k)+'.png'
            
            cropped_img1.save(imagefilepath, 'PNG')
            
            k = k + 1
            
        if not p2:
            filepath = output_folder+'/'+str(k)+'.txt'
            
            out_file = open(filepath, 'w')
            
            imagefilepath = output_folder+'/'+str(k)+'.png'
            
            cropped_img2.save(imagefilepath, 'PNG')
            
            k = k + 1
            
        if not p3:
            filepath = output_folder+'/'+str(k)+'.txt'
            
            out_file = open(filepath, 'w')
            
            imagefilepath = output_folder+'/'+str(k)+'.png'
            
            cropped_img3.save(imagefilepath, 'PNG')
            
            k = k + 1

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(-1)
        
    label_file = sys.argv[1]
    output_folder = sys.argv[2]
    
    try_ext(label_file,output_folder)