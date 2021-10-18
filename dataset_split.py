#randomly divide stimuli into sublists to be used for MTurk

#the CSV originally loaded in is the name of the images, separated by category (column)
# this code will take 15 random indices and then save that as first_split.csv
# this will continue until all items are split up into a total of 26/27 splits of that data

import pandas as pd
from os.path import join
from os import chdir 
import numpy as np

chdir('/Users/zb3663/Documents/GitHub/stimuli_toberated/')

df=pd.read_csv("filenames.csv")

prefix_hi='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_household_items/'
prefix_fv='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_fruits_vegetables/'
prefix_af='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_angry_faces/'
prefix_hf='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_happy_faces/'
prefix_np='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_negative_places/'
prefix_pp='https://raw.githubusercontent.com/zacharybretton/stimuli_toberated/main/resized_positive_places/'

df['Household_items'] = prefix_hi +df['Household_items'].astype(str)
df['Fruits_vegetables'] = prefix_fv + df['Fruits_vegetables'].astype(str)
df['Angry_faces'] = prefix_af + df['Angry_faces'].astype(str)
df['Happy_faces'] = prefix_hf + df['Happy_faces'].astype(str)
df['Negative_places'] = prefix_np + df['Negative_places'].astype(str)
df['Positive_places'] = prefix_pp + df['Positive_places'].astype(str)

for n in range(1,26):
    temp_split=df.sample(16,random_state=400)
    df=df.drop(temp_split.index)
    temp_split_flat=pd.concat([temp_split[col] for col in temp_split])
    temp_split_flat=temp_split_flat.sample(frac=1) #the subset list is now flat, next we need to save into a new df
    subset=pd.DataFrame(temp_split_flat,columns=['image_url'])
    subset['faces'] = subset['image_url'].str.contains('faces')*1 #search the url column for 'faces' and place a 1 in a new column when there is a face
    subset.to_csv(("item_list_"+str(n)+".csv"),index=False)
    del temp_split, temp_split_flat, subset