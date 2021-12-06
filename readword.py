import re
import os
file_path=f'E:\Python Project\Assignment 2\Page'
pages= os.listdir(file_path)
filtered_word={}
word_page=[]
page_no=1
exclude_word = ['and','or','&','of','to','is','the','a','are','in']
for page in pages:
    file_page=os.path.join(file_path,page)
    with open(file_page,'r', encoding="utf8") as file:
        for line in file:       
            for word in line.split():
                word= word.lower()
                word = word.strip('-:?.,!;()[]"/')
                if word not in exclude_word and word.isalpha():         
                    if word not in  filtered_word.keys():
                        words={word:[page_no]}
                        filtered_word.update(words)
                    elif word in filtered_word.keys():
                        if page_no in (filtered_word[word]):
                            pass
                        else:
                            filtered_word[word].append(page_no)

    page_no+=1

sorted_items = dict(sorted(filtered_word.items()))
with open('Index1.txt','a+') as file:
    for word in sorted_items:
        pages = ", ".join(map(str, sorted_items[word]))
        to_append=f"{word} : {pages}"
        file.write(to_append)
        file.write("\n")      




