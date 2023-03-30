'''
This file is intended to import CSV data exported from my Google Forms
Happiness Survey for a single individual at a time.
'''

# Basic data manipulation
import pandas as pd

# Read data from CSV downloaded from Google Forms
df_raw = pd.read_csv('./test_responses.csv')

df_clean = pd.DataFrame(columns = ['date'
                                   ,'first'
                                   ,'second'
                                   ,'third'
                                   ,'work_day'
                                   ,'work_evening'
                                   ,'travel'
                                   ,'time_outside'
                                   ,'exercise'
                                   ,'family'
                                   ,'friends'
                                   ,'pets'
                                   ,'reading'
                                   ,'watching'
                                   ,'skill'
                                   ,'sex'
                                   ,'meat'
                                   ,'vegetables'
                                   ,'fruits'
                                   ,'carbs'
                                   ,'dairy'
                                   ,'sweets'
                                   ,'juice'
                                   ,'coffee'
                                   ,'alcohol'
                                   ,'biggest_influence'
                                   ])

df_clean['date'] = df_raw.iloc[:,4].copy()

df_clean['first'] = df_raw.iloc[:,1].copy()
df_clean['second'] = df_raw.iloc[:,2].copy()
df_clean['third'] = df_raw.iloc[:,3].copy()

df_clean['work_day'] = df_raw.iloc[:,5].copy()
df_clean['work_day'] = df_clean['work_day'].map({'Yes': True, 'No': False})
df_clean['work_evening'] = df_raw.iloc[:,6]

df_clean['travel'] = df_raw.iloc[:,7].copy()
df_clean['travel'] = df_clean['travel'].map({'No': 0
                                             ,'Yes, for work': 1
                                             ,'Yes, for pleasure': 2})

for i in range(df_raw.shape[0]):
    df_clean.iloc[i,7] = True if 'Spent time outside' in df_raw.iloc[i,8] else False
    df_clean.iloc[i,8] = True if 'Exercised appreciably' in df_raw.iloc[i,8] else False
    df_clean.iloc[i,9] = True if 'Spent time with family' in df_raw.iloc[i,8] else False
    df_clean.iloc[i,10] = True if 'Spent time with friends' in df_raw.iloc[i,8] else False
    df_clean.iloc[i,11] = True if 'Spent time with pets' in df_raw.iloc[i,8] else False
    df_clean.iloc[i,12] = True if 'Read a longer book or interest piece' in df_raw.iloc[i,8] else False
    df_clean.iloc[i,13] = True if 'Watched a TV show or movie you enjoy' in df_raw.iloc[i,8] else False
    df_clean.iloc[i,14] = True if 'Practiced a skill (e.g., knitting, drawing, writing code, playing a sport, etc.)' in df_raw.iloc[i,8] else False
    df_clean.iloc[i,15] = True if 'Had sex or intimate relations with a partner' in df_raw.iloc[i,8] else False

for j in range(df_raw.shape[0]):
    df_clean.iloc[j,16] = True if 'Meat or fish' in df_raw.iloc[j,9] else False
    df_clean.iloc[j,17] = True if 'Vegetables' in df_raw.iloc[j,9] else False
    df_clean.iloc[j,18] = True if 'Fruits' in df_raw.iloc[j,9] else False
    df_clean.iloc[j,19] = True if 'Pasta, bread or other complex carbohydrates' in df_raw.iloc[j,9] else False
    df_clean.iloc[j,20] = True if 'Milk, yogurt, or dairy products' in df_raw.iloc[j,9] else False
    df_clean.iloc[j,21] = True if 'Sweets such as candy, chocolate, or pastries' in df_raw.iloc[j,9] else False
    df_clean.iloc[j,22] = True if 'Fresh juice' in df_raw.iloc[j,9] else False
    df_clean.iloc[j,23] = True if 'Coffee or hot tea' in df_raw.iloc[j,9] else False
    df_clean.iloc[j,24] = True if 'Alcohol' in df_raw.iloc[j,9] else False

print(df_clean)