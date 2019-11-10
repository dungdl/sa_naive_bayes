# MARK:- Libs
import json

# MARK:- Get content from json data file
with open('test.json', encoding='utf8') as json_file:
    reviews = json.load(json_file)
    comments = []
    for rev in reviews:
        comments.append(rev['comment'])
    
        
