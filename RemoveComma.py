import os, time
import pandas as pd 

folder_path = r'E:\database Analystt\CarData\hundai'
destination_path= r'E:\database Analystt\CarData\hundai'
files = os.listdir(folder_path)
print(files[6])
file_processed=[]
for file in files[6:]:
    print(f'Removing extra comma of {file}, please wait...')
    file_path=os.path.join(folder_path, file)
    df = pd.read_csv(file_path, usecols=range(4),encoding='latin1')
    df.to_csv(f'{destination_path}\{file}', index=False)
    file_processed.append(file)
    print('Processed files are ',file_processed)
print("all files are processed")


