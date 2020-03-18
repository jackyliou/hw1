# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = 'sample_input.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

target_data = list(filter(lambda item: float(item['WDSD']) != -99, data))
target_data = list(filter(lambda item: float(item['WDSD']) != -999, target_data))

# Retrive ten data points from the beginning.

#target_data = target_data[995:999]


#=======================================


# Part. 4

#=======================================

# Print result
#print(target_data)

maxi = 0.0
mini = 0.0
flag = 0
for item in target_data:
   if item['station_id']=='C0A880':
      flag = flag + 1
      temp = float(item['WDSD'])
      if flag == 2:
         if temp > maxi:
            mini = maxi
            maxi = temp
         else :
            mini = temp
      else:
         if maxi < temp:
            maxi = temp
         elif mini > temp:
            mini = temp
if flag == 0:
   s = "[['C0A880', 'none'],"
   print(s)
else:
   s = "[['C0A880', {0}],".format(maxi-mini)
   print(s)

maxi = 0.0
mini = 0.0
flag = 0
for item in target_data:
   if item['station_id']=='C0F9A0':
      flag = flag + 1
      temp = float(item['WDSD'])
      if flag == 2:
         if temp > maxi:
            mini = maxi
            maxi = temp
         else :
            mini = temp
      else:
         if maxi < temp:
            maxi = temp
         elif mini > temp:
            mini = temp
if flag == 0:
   s = "[['C0F9A0', 'none'],"
   print(s)
else:
   s = "[['C0F9A0', {0}],".format(maxi-mini)
   print(s)

maxi = 0.0
mini = 0.0
flag = 0
for item in target_data:
   if item['station_id']=='C0G640':
      flag = flag + 1
      temp = float(item['WDSD'])
      if flag == 2:
         if temp > maxi:
            mini = maxi
            maxi = temp
         else :
            mini = temp
      else:
         if maxi < temp:
            maxi = temp
         elif mini > temp:
            mini = temp
if flag == 0:
   s = "[['C0G640', 'none'],"
   print(s)
else:
   s = "[['C0G640', {0}],".format(maxi-mini)
   print(s)

maxi = 0.0
mini = 0.0
flag = 0
for item in target_data:
   if item['station_id']=='C0R190':
      flag = flag + 1
      temp = float(item['WDSD'])
      if flag == 2:
         if temp > maxi:
            mini = maxi
            maxi = temp
         else :
            mini = temp
      else:
         if maxi < temp:
            maxi = temp
         elif mini > temp:
            mini = temp
if flag == 0:
   s = "[['C0R190', 'none'],"
   print(s)
else:
   s = "[['C0R190', {0}],".format(maxi-mini)
   print(s)

maxi = 0.0
mini = 0.0
flag = 0
for item in target_data:
   if item['station_id']=='C0X260':
      flag = flag + 1
      temp = float(item['WDSD'])
      if flag == 2:
         if temp > maxi:
            mini = maxi
            maxi = temp
         else :
            mini = temp
      else:
         if maxi < temp:
            maxi = temp
         elif mini > temp:
            mini = temp
if flag == 0:
   s = "[['C0X260', 'none'],"
   print(s)
else:
   s = "[['C0X260', {0}],".format(maxi-mini)
   print(s)
#print(target_data[:10])

#========================================