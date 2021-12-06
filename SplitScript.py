import pandas as pd 
from pathlib import Path
import os, requests, time
chunk_size = 100000
batch_no =1

source_path = r'E:\database Analystt\Deleted data'
destination_path =r'E:\database Analystt\Final Justdail'
files = os.listdir(source_path)
# print(files[6])
for file in files:
    if file.split('.')[-1] == 'csv' or file.split('.')[-1] == 'CSV':
        print(f"spliting of {file} is started, Please wait...")
        file_path = os.path.join(source_path, file)
        fileName=(Path(file_path).stem)
        for chunk in pd.read_csv(file_path, chunksize=chunk_size, encoding='latin1'):
            chunk.to_csv(f'{destination_path}\{fileName}' + str(batch_no) + '.csv' , index=False)
            batch_no +=1
            print(f'{fileName}' + str(batch_no) + '.csv' + f' is new splited file from {file}' )
        print(f"{file} spliting is done")
    else:
        print("This is not csv file",file)
print("File spliting are done")
