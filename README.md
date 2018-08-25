# Traffic Light Detection And Classification
A Better And Faster Deep Learning Approach to Trafﬁc Lights: Detection and Classiﬁcation

## Detection And Classification

Download [Darknet (neural network framework for object detection)](https://github.com/AlexeyAB/darknet) and satisfy the requirements.

##### Compile on Linux :
edit Makefile
  * `GPU=1`
  * `CUDNN=1`
  * `CUDNN_HALF=1` (if using NVIDIA Tesla V100)
  * `OPENCV=1` 
  * `DEBUG=1`
  * `OPENMP=1` 
  * `LIBSO=1`
  
Just do `make` in the darknet directory.

download [cfg](https://drive.google.com/open?id=1s-PGEHxfjsPDdL9rLTyh3MaEeRnRFiOn) and the trained [weight](https://drive.google.com/open?id=1LnzLB9daUyPD6B3QuMUU-CFaXCJDFjtA). Move the cfg file to the cfg folder and the weight file to the backup folder in darknet

Download [Bosch Small Traffic Lights Dataset and scripts](https://github.com/bosch-ros-pkg/bstld). Unzip dataset and go to train folder create a folder name obj

run the command: `python yolov3_annotation_from_yaml_448_448_make.py train.yaml obj` .

It will create training data and annotation for darknet. Move it to `darknet\data\`.

* Create file `obj.names` in the directory `darknet\data\` and write traffic_light
* Create file `obj.data` in the directory `darknet\data\`, containing (where **classes = number of objects**):
  ```
  classes= 1
  train  = data/train.txt
  valid  = 
  names = data/obj.names
  backup = backup/
  ```
* Create file `train.txt` in directory `darknet\data\`, with filenames of images for training each filename in new line example:
  ```
  data/obj/1.png
  data/obj/2.png
  data/obj/3.png
  ```


## AP AND Precision x Recall curve:
Download groundtruths and detections [Link](https://drive.google.com/file/d/1KZBb6pCyMLO757g5WV_ADTFtwGaW3bT8/view?usp=sharing)
unzip it and store it in TL-Detection-Metrics/Object-Detection-Metrics-master folder.

Groundtruths format: `<class_name> <left> <top> <width> <height>` .

Detections format: `<class_name> <confidence> <left> <top> <right> <bottom>`.

run the command: `python pascalvoc.py -gtformat xyrb -detformat xyrb`

![alt text](https://github.com/nafis00141/TL-Detection-And-Classification/blob/master/images%20for%20readme/map.PNG)

Download [Bosch Small Traffic Lights Dataset and scripts](https://github.com/bosch-ros-pkg/bstld). Unzip dataset and go to test folder and copy [groundtruth_file_and_image.py](https://github.com/nafis00141/TL-Detection-And-Classification/blob/master/groundtruth_file_and_image.py). Create 2 folders for groundtruths and images.  

run the command: `python groundtruth_file_and_image.py input_yaml FolderNameForGroundTruths FolderNameForImages`

this will generate GroundTruths and Images for testing from Test Data


## References
Dataset https://github.com/bosch-ros-pkg/bstld
Darknet https://github.com/AlexeyAB/darknet
forked and modified from https://github.com/rafaelpadilla/Object-Detection-Metrics
