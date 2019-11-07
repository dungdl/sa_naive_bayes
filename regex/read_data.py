
# MARK:- Libs
import re

# MARK:- Open data file
input = open("data.txt")

# MARK:- Define regex
delimiter = "#[0-9]+"

# MARK:- Define layers
entities = ['RESTAURANT', 'FOOD', 'DRINKS',
            'AMBIENCE', 'SERVICE', 'LOCATION']
atrributes = ['GENERAL', 'PRICES', 'QUALITY', 'STYLE&OPTIONS', 'MISCELLANEOUS']
values = ['positive', 'neutral', 'negative']

# MARK:- Read input by lines

i = 1
while i in range(1, 10):
    line = input.readline()
    x = re.search(delimiter, line)
    if x:
        print(x.string)
        content = input.readline()
        tag = input.readline()

        for e in entities:
            en = re.findall(r'' + e + '', tag)
            if en.__len__() > 0:
                print("Entity: " + en[0])
                for a in atrributes:
                    at = re.findall(r'' + a + '', tag)
                    if at.__len__() > 0:
                        print("Attribute: " + at[0])
                        for v in values:
                            va = re.findall(r'' + v + '', tag)
                            if va.__len__() > 0:
                                print("Value: " + va[0])

        print("---------")
    line = input.readline()
    i += 1
