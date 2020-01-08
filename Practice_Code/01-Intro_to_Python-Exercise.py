#!/usr/bin/env python
# coding: utf-8

# jupyter nbconvert --to python YOURNOTEBOOKNAME.ipynb

# List Practice

# In[83]:


my_new_list = ["dude","55"]
print(my_new_list)
dude55 = my_new_list[0]+my_new_list[1]
print(dude55)
my_int = int(my_new_list[1])
print(my_int)
my_substring = dude55[2:5]
print(my_substring)
my_range = range(3,26,3)
print(list(my_range))


# Dictionaries Practice

# In[84]:


nyc={'manhattan':'work','brooklyn':'play','best borough':'brooklyn'}
type(nyc)
print(nyc.keys())
print(nyc.values())
print(nyc.items())

nyc['queen'] = 'england'
nyc.items()

del nyc['brooklyn']
nyc.items()


# In[85]:





# In[86]:


nyc['queen']
nyc['other boroughs'] = ['bronx','staten island']
print(nyc['best borough'])
nyc['new jersey'] = 'city'
nyc['other boroughs'] = ['bronx','staten island']
#print(nyc.items())
nyc['other boroughs'] = [nyc['other boroughs'][0].upper(), nyc['other boroughs'][1].upper()]
nyc.items()


# Functions Practice

# In[68]:


def compute_pay(hours,rate):
    #print(hours*rate)
    return hours*rate

print(compute_pay(40,10.50))

def get_hours_worked(total_pay,rate):
    return float(total_pay)/rate
print(get_hours_worked(500,10))
    


# In[87]:


for i in range(1,11):
    print(i+7, end = ' ')


# In[88]:


##List Comprehension

words = ['yo','hello','awesome']
list_words = [i.upper() for i in words]
print(list_words)
word = 'fancy'
list_word = [i.upper() for i in word]
print(list_word)

def awesome_sauce():
    for i in range(1,101):
        if i%2 ==0 and i%7==0:
            print('awesome sauce')
        elif i%2 == 0:
            print('awesome')
        elif i%7 == 0:
            print('sauce')
        else:
            print(i)

awesome_sauce()


# Get Data From CSV

# In[141]:


import csv

with open('C:/Users/Madhumita.Ganesan/Desktop/DataScience/data/vertebral_column_2_categories.txt','r') as f:
    vertebral_data= [row for row in csv.reader(f)]
    
for line in vertebral_data[0:5]:
    print(line)


# Get data from internet

# In[106]:


import requests

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

iris_data = [row.decode('utf-8') for row in r.iter_lines()]

for line in iris_data[:5]:
    print(line)


# In[139]:


## SPlit Iris Data items on commas

import requests
r= requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
iris_data=[row.decode('utf-8') for row in r.iter_lines()]

##List Comprehension
iris_data_split1 = [dude.split(",") for dude in iris_data]

print("List Comprehension version - Data Split")
print(iris_data_split1[:5])

##For Loop
iris_data_split2 = []
for i in iris_data:
    iris_data_split2.append(i.split(","))

print("Loop version - Data Split")
print(iris_data_split2[:5])

##Numeric entries on each item in iris_data
##List COmprehension

iris_data_numeric1 = [[float(var) for var in line.split(",")[:-1]] for line in iris_data]
print("List Comprehension version - Convert numeric")
print(iris_data_numeric1[:5])

## For Loop
converted_list = []
print("Loop version - Convert Numeric")
for line in iris_data:
    split1 = line.split(",")[:-1]
    converted_line_numbers = [float(num) for num in split1]
    converted_list.append(converted_line_numbers)
    
for line in converted_list[:5]:
        print(line)
    
    
    
    


# In[140]:


jupyter nbconvert --to python 01-Intro_to_Python-Exercise.ipynb


# In[ ]:




