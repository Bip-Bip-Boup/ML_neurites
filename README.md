# ML_neurites
A project in collaboration with a biology laboratory for the detection and segmentation of organelles and neurites using 2D chromatic pictures from a microscope

PROJECT SETUP
One may install the correct biolab software to visualize the CZI images,
We will use czifile python library (install by running pip install czifile ) just in case we will also install the aicspylibczi (pip install aicspylibczi )


#####################PIPELINE############################

From the raw data in czifile we will need :

1. Code to visualize the CZIfiles 

2. Properly separate the data between the data that will be used for training, testing and validation (maybe training with isolated images of organelles and neurites, validation with images of mix, then testing on unseen images of mix)

3. Extracting potential additionnal data from videos on the onedrive

4. Code to properly segment and extract the organelles and neurites, 1 picture per organelle and per neurite

5. Preprocessing of all images, resizing mainly for normalization



