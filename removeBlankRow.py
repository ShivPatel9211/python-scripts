import os, time
import pandas as pd 
import csv
import sys
folder_path = r'E:\database Analystt\Deleted data'
destination_path= r'E:\database Analystt\Deleted data'
files = os.listdir(folder_path)
print(files)
file_processed=[]
for file in files:
    print(f'Removing blank row of {file}, please wait...')
    file_path=os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    df = df.dropna(how='all')
    df.to_csv(f'{folder_path}/sample.csv', index=False)
    print(df)
    # print(df.iloc[1])
    # df = df.dropna(how='all')
    # print(df)
    print('Processed files are ',file_processed)
# inputCSV.close()
# outputCSV.close()
# print("all files are processed")


