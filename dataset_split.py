#randomly divide stimuli into sublists to be used for MTurk

#the CSV originally loaded in is the name of the images, separated by category (column)
# this code will take 15 random indices and then save that as first_split.csv
# this will continue until all items are split up into a total of 26/27 splits of that data

import pandas as pd
from os.path import join
from os import chdir 
import numpy as np

chdir('/Users/zb3663/Documents/GitHub/stimuli_toberated/')

df=pd.read_csv("filenames_1.csv")

prefix_hi='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_household_items/'
prefix_p='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_produce/'
prefix_nf='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_negative_faces/'
prefix_pf='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_positive_faces/'
prefix_np='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_negative_places/'
prefix_pp='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_positive_places/'
prefix_pa='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_positive_animals/'
prefix_na='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_negative_animals/'

df['household_items'] = prefix_hi +df['household_items'].astype(str)
df['produce'] = prefix_p + df['produce'].astype(str)
df['negative_places'] = prefix_np + df['negative_places'].astype(str)
df['positive_places'] = prefix_pp + df['positive_places'].astype(str)
df['positive_animals'] = prefix_pa + df['positive_animals'].astype(str)
df['negative_animals'] = prefix_na + df['negative_animals'].astype(str)

full_df=pd.DataFrame()

for n in range(1,32):
    temp_split=df.sample(12,random_state=400)
    df=df.drop(temp_split.index)
    temp_split_flat=pd.concat([temp_split[col] for col in temp_split])
    temp_split_flat=temp_split_flat.sample(frac=1) #the subset list is now flat, next we need to save into a new df
    temp_list=[]
    for i in range(1,73): #going to have to label all images in a different column
        temp_list.append(('image_url_'+str(i)))
    subset=pd.DataFrame(temp_split_flat) #save to new DF
    subset=subset.T #transpose the arrays
    subset.columns=temp_list #reset column names
    #subset['faces'] = subset['image_url'].str.contains('faces')*1 #search the url column for 'faces' and place a 1 in a new column when there is a face
    subset.to_csv(("item_list_"+str(n)+".csv"),index=False)
    full_df=full_df.append(subset,ignore_index=True)
    del temp_split, temp_split_flat, subset,temp_list

full_df.to_csv("full_HIT_list.csv",index=False)


full_df=pd.DataFrame()
df=pd.read_csv("filenames_2.csv")
df['positive_faces'] = prefix_pf + df['positive_faces'].astype(str)
df['negative_faces'] = prefix_nf + df['negative_faces'].astype(str)
for n in range(1,34):
    temp_split=df.sample(12,random_state=400)
    df=df.drop(temp_split.index)
    temp_split_flat=pd.concat([temp_split[col] for col in temp_split])
    temp_split_flat=temp_split_flat.sample(frac=1) #the subset list is now flat, next we need to save into a new df
    temp_list=[]
    for i in range(1,25): #going to have to label all images in a different column
        temp_list.append(('image_url_'+str(i)))
    subset=pd.DataFrame(temp_split_flat) #save to new DF
    subset=subset.T #transpose the arrays
    subset.columns=temp_list #reset column names
    #subset['faces'] = subset['image_url'].str.contains('faces')*1 #search the url column for 'faces' and place a 1 in a new column when there is a face
    subset.to_csv(("item_list_"+str(n)+".csv"),index=False)
    full_df=full_df.append(subset,ignore_index=True)
    del temp_split, temp_split_flat, subset,temp_list

full_df.to_csv("full_HIT_list_faces.csv",index=False)    