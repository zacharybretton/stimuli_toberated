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
from os import path



object_results_dir='/Users/zb3663/Library/CloudStorage/Box-Box/LewPeaLabBox/STUDY/clearvale_rating/MTurk_batch/object_results'

face_results_dir='/Users/zb3663/Library/CloudStorage/Box-Box/LewPeaLabBox/STUDY/clearvale_rating/MTurk_batch/face_results'

object_export_dir='/Users/zb3663/Library/CloudStorage/Box-Box/LewPeaLabBox/STUDY/clearvale_rating/MTurk_batch/object_sorted'

face_export_dir='/Users/zb3663/Library/CloudStorage/Box-Box/LewPeaLabBox/STUDY/clearvale_rating/MTurk_batch/face_sorted'

valence_answers=np.array(['Exremely negative','Negative','Somewhat negative','Neutral','Somewhat positive','Positive','Extremely positive'])
arousal_answers=np.array(['Very relaxed/calm','Relaxed/calm','Somewhat relaxed/calm','Neutral','Somewhat excited/aroused', 'Excited/aroused','Very excited/aroused'])
typical_answers=np.array(['Very atypical/unusual','Atypical/unusual','Somewhat atypical/unusual','Neutral','Somewhat typical/usual','Typical/usual','Very typical/usual'])

def find(pattern, path): #find the pattern we're looking for
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
        return result

def check_file(filePath):
    if path.exists(filePath):
        numb = 1
        while True:
            newPath = "{0}_{2}{1}".format(*path.splitext(filePath) + (numb,))
            if path.exists(newPath):
                numb += 1
            else:
                return newPath
    return filePath

#find the batch csv's so that we can load in the information
obj_batch_files=find('Batch*.csv',object_results_dir)

for file in obj_batch_files:
    batch_df=pd.read_csv(file)

    for row in batch_df.index:
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

            image_dict={}
            image_num=image.split(".")[-1].split("_")[-1] #this splits out the "." and the "_" allowing us to grab the last value which is the image #
            image_name=batch_df.loc[row,image].split("/")[-1] #this splits the image path so we can get just the name
            image_dict['name']=image_name

            temp_arousal=[]
            temp_valence=[]
            temp_typical=[]

            for temp_column in arousal_columns:
                temp_num=temp_column.split(".")[-2].split("_")[-2]

                if temp_num==image_num:
                    temp_arousal.append(temp_column)
            a_answer=arousal_answers[batch_df.loc[row,temp_arousal].values.astype(bool)][0]
            image_dict['Arousal']=a_answer

            for temp_column in valence_columns:
                temp_num=temp_column.split(".")[-2].split("_")[-2]

                if temp_num==image_num:
                    temp_valence.append(temp_column)
            v_answer=valence_answers[batch_df.loc[row,temp_valence].values.astype(bool)][0]
            image_dict['Valence']=v_answer

            for temp_column in typical_columns:
                temp_num=temp_column.split(".")[-2].split("_")[-2]

                if temp_num==image_num:
                    temp_typical.append(temp_column)

            t_answer=typical_answers[batch_df.loc[row,temp_valence].values.astype(bool)][0]
            image_dict['Typicality']=t_answer

            data_dict[image_num]=image_dict

            del image_dict

        worker_id=batch_df.loc[row,'WorkerId']

        temp_df=pd.DataFrame(data=data_dict)

        temp_file=os.path.join(object_export_dir,(worker_id+'.csv'))

        temp_df.to_csv(check_file(temp_file))

        del temp_df, temp_file

###################################################
# Face results
###################################################

face_batch_files=find('Batch*.csv',face_results_dir)

for file in face_batch_files:
    batch_df=pd.read_csv(file)

    for row in batch_df.index:
        arousal_columns=[]
        valence_columns=[]
        image_columns=[]
        data_dict={}
        for _c in batch_df.columns:
            if 'Arousal' in _c:
                arousal_columns.append(_c)
            elif 'Valence' in _c:
                valence_columns.append(_c)
            elif 'image' in _c:
                image_columns.append(_c)
        for image in image_columns:

            image_dict={}
            image_num=image.split(".")[-1].split("_")[-1] #this splits out the "." and the "_" allowing us to grab the last value which is the image #
            image_name=batch_df.loc[row,image].split("/")[-1] #this splits the image path so we can get just the name
            image_dict['name']=image_name

            temp_arousal=[]
            temp_valence=[]
            temp_typical=[]

            for temp_column in arousal_columns:
                temp_num=temp_column.split(".")[-2].split("_")[-2]

                if temp_num==image_num:
                    temp_arousal.append(temp_column)
            a_answer=arousal_answers[batch_df.loc[row,temp_arousal].values.astype(bool)][0]
            image_dict['Arousal']=a_answer

            for temp_column in valence_columns:
                temp_num=temp_column.split(".")[-2].split("_")[-2]

                if temp_num==image_num:
                    temp_valence.append(temp_column)
            v_answer=valence_answers[batch_df.loc[row,temp_valence].values.astype(bool)][0]
            image_dict['Valence']=v_answer

            data_dict[image_num]=image_dict

            del image_dict

        worker_id=batch_df.loc[row,'WorkerId']

        temp_df=pd.DataFrame(data=data_dict)

        temp_file=os.path.join(face_export_dir,(worker_id+'.csv'))

        temp_df.to_csv(check_file(temp_file))

        del temp_df, temp_file
