import os, requests, time
from requests.auth import HTTPBasicAuth
url = 'http://13.234.67.115/contacts/upload'
folder_path = r'E:\database Analystt\Final Justdail'

files = os.listdir(folder_path)
# print(files[2])
success= open(f"{folder_path}\Success.txt","w+")
fail= open(f"{folder_path}\Fail.txt","w+")
success_index =0
fail_index=0
for file in files[17:]:
    if file.split('.')[-1] == 'csv':
        print(f'{file} uploading is started, please wait...')
        file_path = os.path.join(folder_path, file)
        files = {'file': (file, open(file_path, 'rb'), 'text/csv')}
        r = requests.post(url, files=files, auth=HTTPBasicAuth('analystt', 'Hello!1234'))
        if r.status_code == 200:
            print(f'{file} Uploaded')
            print('waiting for next upload ....')
            success_index +=1
            success.write(f"{success_index}. {file}\n")
        else:
            print(f'Error - {file}', r)
            fail_index +=1
            fail.write(f"{fail_index}. Error in uploading {file}\n")
        time.sleep(60*4) # wait 5 min after every upload
    else:
        fail_index +=1
        fail.write(f"{fail_index}. File is not csv {file}\n")
        print('File is not csv', file)
success.close()
fail.close()
print("Done")
