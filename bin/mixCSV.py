__author__ = 'Oscar'

import sys
import pprint

FILE_ONE = "../"

FILE_TWO = "../"

FILE_THREE = "../"

SEPARATOR_ONE = ";"

SEPARATOR_TWO = ";"

SEPARATOR_THREE = ";"

COMMON_FIELD = "field"

fileIn = open(FILE_ONE,"rbU")

first = True

dataOne = {}

for line in fileIn:

    fields = line.rstrip().decode("utf8").split(SEPARATOR_ONE)

    if first:
        header = fields
        first = False
    else:
        myData = {}

        for i in range(0,len(fields)):
            myData[header[i]] = fields[i]

        dataOne[myData[COMMON_FIELD]] = myData

fileIn.close()

pprint.pprint(dataOne)


fileIn = open(FILE_TWO, "rbU")

first = True

dataTwo = {}

for line in fileIn:

    fields = line.rstrip().decode("utf8").split(SEPARATOR_ONE)

    if first:
        header = fields
        first = False
    else:
        myData = {}

        for i in range(0,len(fields)):
            myData[header[i]] = fields[i]

        dataTwo[myData[COMMON_FIELD]] = myData

fileIn.close()

pprint.pprint(dataTwo)

# And now mix dictionaries

dataFinal = []

headerFields = {}

for key in dataOne.keys():
    if key in dataTwo.keys():
        myData = {}

        for field in dataTwo[key]:
            myData[field] = dataTwo[key][field]

            headerFields[field] = True

        for field in dataOne[key]:
            myData[field] = dataOne[key][field]
            headerFields[field] = True


        dataFinal.append(myData)

pprint.pprint(dataFinal)

pprint.pprint(headerFields)

# And write final file

fileOut = open(FILE_THREE, "wb")

# Write header

header = sorted(headerFields.keys())

fileOut.write(SEPARATOR_THREE.join(header).encode("utf8")+"\n")

for data in dataFinal:
    myData = []
    for field in header:
        myData.append(data[field])

    fileOut.write(SEPARATOR_THREE.join(myData).encode("utf8")+"\n")

fileOut.close()



