# Traffic Light Detection And Classification
A Better And Faster Deep Learning Approach to Trafﬁc Lights: Detection and Classiﬁcation

## AP AND Precision x Recall curve:
Download groundtruths and detections [Link](https://drive.google.com/file/d/1KZBb6pCyMLO757g5WV_ADTFtwGaW3bT8/view?usp=sharing)
unzip it and store it in TL-Detection-Metrics/Object-Detection-Metrics-master folder.

Groundtruths format: `<class_name> <left> <top> <width> <height>` .

Detections format: `<class_name> <confidence> <left> <top> <right> <bottom>`.

run the comand.bat

![alt text](https://github.com/nafis00141/TL-Detection-And-Classification/blob/master/images%20for%20readme/map.PNG)

Download [Bosch Small Traffic Lights Dataset and scripts](https://github.com/bosch-ros-pkg/bstld). Unzip dataset and go to test folder and copy [groundtruth_file_and_image.py](https://github.com/nafis00141/TL-Detection-And-Classification/blob/master/groundtruth_file_and_image.py). Create 2 folders for groundtruths and images.  

run the command: `python groundtruth_file_and_image.py input_yaml FolderNameForGroundTruths FolderNameForImages`

this will generate GroundTruths and Images for testing from Test Data


## References
Dataset https://github.com/bosch-ros-pkg/bstld

forked and modified from https://github.com/rafaelpadilla/Object-Detection-Metrics
