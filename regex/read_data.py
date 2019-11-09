
# MARK:- Libs
import re
import io
import json
import pprint

# MARK:- Supoprt functions
# read data file


def readData(fileName):
    outFile = io.open(fileName, 'r', encoding='utf-8-sig')
    return outFile

# write to output file


def writeData(fileName, data):
    file = io.open(fileName, "w", encoding='utf-8')
    file.write(data)
    file.close()


# MARK:- Operation
# read input data
input = readData(
    "data.txt")

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
while i in range(1, 7):
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
        tag = tag[1:-2]
        tags = re.split("}, {", tag)

        # create a json object for a tag
        json_part = {}

        json_part["index"] = number
        json_part["comment"] = content[1:]

        # entity json array
        entities = {}

        for t in tags:
            (key, value) = re.split(", ", t)
            (entity, attribute) = re.split("#", key)

            if entity not in entities:
                entities[entity] = {attribute: value}
            else:
                ob = entities[entity]
                ob[attribute] = value
                entities[entity] = ob

        json_part["tags:"] = entities

        # append to result
        json_result.append(json_part)

    line = input.readline()
    i += 1

# result now is a list
# convert result to json
parsed_json = json.dumps(json_result, indent=4,
                         sort_keys=True, ensure_ascii=False)
# and output to file
writeData("test.json", parsed_json)
