import os
import pandas as pd 

folder_path = r'E:\database Analystt\Deleted data'
destination_path= r'E:\database Analystt\Deleted data'
files = os.listdir(folder_path)
# print(files)
file_processed=[]
success= open(f"{folder_path}\Success.txt","w+")
fail= open(f"{folder_path}\Fail.txt","w+")
success_index = 0
fail_index=0
for file in files:
    if file.split('.')[-1] == 'csv' or file.split('.')[-1] == 'CSV':
        print(f'Removing extra comma and space of {file}, please wait...')
        file_path=os.path.join(folder_path, file)
        df = pd.read_csv(file_path,encoding='latin1')
        df = df.rename(columns=lambda x:x.strip())
        # print(df['PhoneNumbers'].dtypes)
        # df = df.dropna(how='all') #remove blank space
        # if (df['PhoneNumbers'].dtypes) !='int64':
        #     df['PhoneNumbers'] = df['PhoneNumbers'].astype('float')
        #     df['PhoneNumbers'] = df['PhoneNumbers'].astype('Int64') # tTo convert the phone number into interger
        df.to_csv(f'{destination_path}\{file}',index=False)
        success_index +=1
        success.write(f"{success_index}. {file}\n")
    else:
        fail_index +=1
        fail.write(f"{fail_index}. {file}\n")
        print(f"{file} is not csv file")
success.close()
fail.close()
print("all files are processed")


