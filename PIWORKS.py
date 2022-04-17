import csv

file = open('C:\\Users\\Hp\\Downloads\\country_vaccination_stats.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)

# Question 1
i = 0
newCountryID = i
country_name = ""
temp = ""
minVaccinations = 99999999999
val = minVaccinations

while i < len(rows):
    temp = rows[i][0]
    if rows[i][2] != '':
        val = rows[i][2]
    else:
        val = minVaccinations
    if temp != country_name:
        country_name = temp
        rows[newCountryID][2] = minVaccinations
        minVaccinations = 99999999999
        newCountryID = i
    elif temp == country_name and rows[i][2] != '':
        if int(val) < int(minVaccinations):
            minVaccinations = rows[i][2]

    if rows[i][2] == '':
        if i != 0 and rows[i][2] == '':
            if rows[i][0] != rows[i - 1][0] or rows[i][0] != rows[i + 1][0]:
                rows[i][2] = 0
        if i == 0 and rows[i][2] == '':
            if rows[i][0] != rows[i + 1][0]:
                rows[i][2] = 0
        if rows[i][0] == '':
            rows[i][0] = minVaccinations
    i = i + 1

# Question 2
i = 0
median = 0
medianList = [0, 0, 0]
countryDict = {}
checker = 3
sortedList = []
country_name = rows[0][0]
tempCountryName = ""
while i < len(rows):
    tempCountryName = rows[i][0]
    if tempCountryName == country_name:
        median = median + 1
        sortedList.append(rows[i][2])
    else:
        sortedList.sort()
        medianList.sort()
        if len(sortedList) > 0 and int(sortedList[int(median / 2)]) > int(medianList[0]):
            if medianList[0] in countryDict:
                countryDict.pop(medianList[0])
            medianList[0] = int(sortedList[int(median / 2)])
            countryDict[medianList[0]] = country_name
        sortedList.clear()
        median = 0
        country_name = rows[i][0]
    i = i + 1

print("Top-3 countries with highest median daily vaccination numbers: ")
print(countryDict.values())

# Question 3
i = 0
total = 0
while i < len(rows):

    if rows[i][1] == "1/6/2021":
        total = total + int(rows[i][2])
    i = i + 1
print(total)

# Question 4
countryList = []
i = 0
while i < len(rows):
    countryList.append(rows[i][0])
    i = i + 1

# Calculates median for each country.
i = 0
while i < len(countryList):
    sql = "SELECT " \
          "( " \
          "SELECT MAX(vaccination) FROM (SELECT TOP 50 PERCENT vaccination FROM country_vaccination_stats ORDER BY vaccination) +" \
          "SELECT MIN(vaccination) FROM (SELECT TOP 50 PERCENT vaccination FROM country_vaccination_stats ORDER BY vaccination DESC) / 2  As Median" \
          "), country WHERE country == countryList[i]"
    i = i + 1
