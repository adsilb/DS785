# DS785
Capstone code related to automated classifications of breast cancer lesions

## The folders

- **images**: contains all of the original images in the data set and all of the marked images that the radiologist created
- **spreadsheets**: contains the file of annotations from the radiologist (BUSL_Notes.csv) as well as any other spreadsheets created or consumed by the code along the way

## A brief tour of the code files

- **Common.py**

This file contains the primary function for opening image files.

- **Radiomics.ipynb**

Contains code for iterating through the image files and generating radiomics statistics

- **Data_Prep.ipynb**

Contains code for combining the radiomics data with the annotations provided by the radiologist, and then adding additional columns for abruptness and orientation metrics

- **Boxplots.py**

Contains code for comparing how the numerical algorithms perform relative to the annotations provided by the radiologist.

- **Pycaret_Radiomics_Auot_Split.ipynb**

As the name suggests, this file uses Pycaret to generate a list of models based on the cleanest version of the data, once unhelpful columns have been removed. The top candidates are then evaluated for performance and feature importance.
