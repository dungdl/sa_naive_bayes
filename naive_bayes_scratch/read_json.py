# MARK:- Libs
import json

# MARK:- Get content from json data file
with open('test.json', encoding='utf8') as json_file:
    reviews = json.load(json_file)
    comments = []
    i = 0
    for rev in reviews:
        print(rev)
        i += 1
        if i == 3 : 
            break
    
        