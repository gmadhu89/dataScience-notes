#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# In[13]:


## Getting Movie data for practice
movie_data = pd.read_csv("C:/Users/Madhumita.Ganesan/Desktop/DataScience/data/movieData/movieData/movies.dat",sep = "::",names = ["MovieId","Title","Genres"],engine="python")

user_data = pd.read_csv("C:/Users/Madhumita.Ganesan/Desktop/DataScience/data/movieData/movieData/users.dat",sep = "::",names = ["UserID","Gender","Age","Occupation","Zip-code"],engine="python")
                         
rating_data = pd.read_csv("C:/Users/Madhumita.Ganesan/Desktop/DataScience/data/movieData/movieData/ratings.dat",sep = "::",names = ["UserID","MovieID","Rating","Timestamp"],engine="python")


# In[14]:


movie_data.head()


# In[15]:


# Checking if the movie ID's are Unique in the data set
print("Total Number of rows: ", movie_data.shape)
print("Total Unique movies: ",movie_data.MovieId.unique().shape)
print("Are the movies unique in the dataset",movie_data.shape[0] == movie_data.MovieId.unique().shape[0])


# In[16]:


# Parsing / splitting the Title and the year
print("Original movie data is \n",movie_data.head(5))

movie_data['year'] = movie_data.Title.str.slice(-5,-1)
movie_data.Year = movie_data.year.astype(int)
movie_data.Title = movie_data.Title.str.slice(0,-7)

print("Formatted Movie data is \n",movie_data.head(5))


# In[21]:


## Getting the identifier representation for the Genres 
movie_genres = movie_data.Genres.str.get_dummies(sep = '|')
type(movie_genres)

## Joining this datatype with the actual dataset to print the results
moviedatawithgenre = movie_data.merge(movie_genres,left_index=True,right_index=True)
moviedatawithgenre.head()


# In[22]:


moviedatawithgenre2 = pd.concat((movie_data,movie_genres),axis=1)
moviedatawithgenre2.head()


# In[23]:


## Delete the Genres column
del moviedatawithgenre["Genres"]
moviedatawithgenre.head()


# In[30]:





# In[32]:


##In what decade were the most of the movies found in this dataset made?
movie_data.year = movie_data.year.astype(int)
yeardata = movie_data[["Title","year"]]

minyear = yeardata.year.min()
maxyear = yeardata.year.max()

print("Earliest year is %d  and Latest Year is %d "%(minyear,maxyear))

mindecade=np.floor_divide(minyear,10)*10
maxdecade=np.floor_divide(maxyear,10)*10

print("Earliest decade is %d  and Latest Decade is %d "%(mindecade,maxdecade))


# In[34]:


all_decades = np.arange(mindecade,maxdecade+10,10)

print("All decades : %s"%(all_decades))


# In[59]:


yeardata["Decade"] = pd.cut(yeardata.year,all_decades)
#yeardata.head()
moviesperdecade = yeardata.groupby("Decade").size()
moviesperdecade.sort_values(ascending=False,inplace=True)
type(moviesperdecade)
print(moviesperdecade.head(1))


# In[62]:


#### User data calculations
user_data.head(5)


# In[71]:


##Make sure that every user mapped to Age 1 has an Occupation 4 or 10, if not, remove them.
##Make sure no one that has an Occupation other than 10 is of Age either 1 or 18, otherwise remove them.
##Make sure all of the zipcodes are in a standard (5 digit) format, but keep them as string types (any idea why?)

UserMask1=np.logical_and(user_data.Age==1,np.logical_or(user_data.Occupation==4,user_data.Occupation==10))
UserMask2=np.logical_and(user_data.Age!=1,np.logical_and(user_data.Occupation!=4,user_data.Occupation!=10))

UserDataMask=np.logical_or(UserMask1,UserMask2)
UserDataFiltered = user_data[UserDataMask]

#print(UserDataFiltered)


# In[77]:


myMask2 = np.logical_or(np.logical_and(UserDataFiltered.Occupation!=10,np.logical_and(UserDataFiltered.Age!=1,UserDataFiltered.Age!=18)),UserDataFiltered.Occupation==10)
userDataFinallyFiltered = UserDataFiltered[myMask2]

user_data["Zip-code"].unique()                     
userDataFinallyFiltered = userDataFinallyFiltered[userDataFinallyFiltered["Zip-code"].str.len()>=5]
userDataFinallyFiltered["Zip-code"] = userDataFinallyFiltered["Zip-code"].str.slice(0,5)

print("Before removing garbage:",user_data.shape)
print("After removing garbage:",userDataFinallyFiltered.shape)


# In[88]:


rating_data.columns
#rating_data.shape
rating_data['UserID'].unique().shape


# In[89]:


filledAndCleanedUserAndRatingData = userDataFinallyFiltered.merge(rating_data,on="UserId")


# In[ ]:




