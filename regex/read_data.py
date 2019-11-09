
# MARK:- Libs
import re
import io
import json
import pprint

# MARK:- Supoprt functions
# read data file
def readData(fileName):
    outFile = io.open(fileName, 'r', encoding='utf-8')
    return outFile

# write to output file
def writeData(fileName, data):
    file = io.open(fileName, "w", encoding='utf-8')
    file.write(data)
    file.close()

# MARK:- Operation
# read input data
input = readData("data.txt")

# define sharp delimiter
delimiter = "#[0-9]+"

# init result
json_result = []

# MARK:- Define layers
entities = ['RESTAURANT', 'FOOD', 'DRINKS',
            'AMBIENCE', 'SERVICE', 'LOCATION']
atrributes = ['GENERAL', 'PRICES', 'QUALITY', 'STYLE&OPTIONS', 'MISCELLANEOUS']
values = ['positive', 'neutral', 'negative']

# MARK:- Read input by lines

i = 1
while i in range(1, 3000):
    line = input.readline()
    x = re.search(delimiter, line)
    if x:
        number = x.string
        content = input.readline()
        tag = input.readline()

        # remove \n character
        content = content[:-1]
        number = number[:-1]

        # remove first and last bracket
        tag = tag[:-2]
        tag = tag[1:]
        tags = re.split("}, {", tag)

        for s in tags:
            for e in entities:
                en = re.findall(r'' + e + '', s)
                if en.__len__() > 0:
                    # save entity
                    res_e = en[0]
                    for a in atrributes:
                        at = re.findall(r'' + a + '', s)
                        if at.__len__() > 0:
                            # save attribute
                            res_a = at[0]
                            for v in values:
                                va = re.findall(r'' + v + '', s)
                                if va.__len__() > 0:
                                    # save value
                                    res_v = va[0]
            # create a json object for ONE tag
            json_part = {}
            
            json_part["number"] = number
            json_part["data"] = content
            json_part["entity"] = res_e 
            json_part["attribute"] = res_a
            json_part["value"] = res_v

            # append to result
            json_result.append(json_part)

    line = input.readline()
    i += 1

# result now is a list
# convert result to json
parsed_json = json.dumps(json_result, indent=4, sort_keys=True, ensure_ascii=False)
# and output to file
writeData("test.json", parsed_json)
