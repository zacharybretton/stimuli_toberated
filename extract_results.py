#python code to take in the MTurk CSV and look at the results

#Imports
import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")
import numpy as np
import nibabel as nib
import scipy as scipy
import scipy.io as sio
import matplotlib.pyplot as plt
import seaborn as sns
import os
import fnmatch
import pandas as pd
import pickle


results_dir='/Users/zb3663/Library/CloudStorage/Box-Box/LewPeaLabBox/STUDY/clearvale_rating/MTurk_batch'

valence_answers=['Exremely negative','Negative','Somewhat negative','Neutral','Somewhat positive','Positive','Extremely positive']
arousal_answers=['Very relaxed/calm','Relaxed/calm','Somewhat relaxed/calm','Neutral','Somewhat excited/aroused', 'Excited/aroused','Very excited/aroused']
typical_answers=['Very atypical/unusual','Atypical/unusual','Somewhat atypical/unusual','Neutral','Somewhat typical/usual','Typical/usual','Very typical/usual']

def find(pattern, path): #find the pattern we're looking for
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
        return result

#find the batch csv's so that we can load in the information
batch_files=find('Batch*.csv',results_dir)

for file in batch_files:
    batch_df=pd.read_csv(file)
    arousal_columns=[]
    valence_columns=[]
    typical_columns=[]
    image_columns=[]
    data_dict={}
    for _c in batch_df.columns:
        if 'Arousal' in _c:
            arousal_columns.append(_c)
        elif 'Valence' in _c:
            valence_columns.append(_c)
        elif 'Typical' in _c:
            typical_columns.append(_c)
        elif 'image' in _c:
            image_columns.append(_c)
    for image in image_columns:
        image_num=image.split(".")[-1].split("_")[-1] #this splits out the "." and the "_" allowing us to grab the last value which is the image #
        image_name=batch_df[image].values[0].split("/")[-1] #this splits the image path so we can get just the name
        data_dict[image_num]={'name':image_name}
