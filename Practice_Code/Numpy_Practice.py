#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[27]:


# np.ScalarType  -- Types of scalars in Numpy


# In[28]:


# Vector - Array (list)
my_array = np.array([1,2,3])
print("my_array is ",my_array,type(my_array))

my_list = [1,2.5,4]
my_array2 = np.array(my_list)
print(my_array2,type(my_array2))

my_add = my_array + 2
print("Added array is \t\t", my_add)

my_sub = my_array -1
print("Subtracted array is \t\t",my_sub)

my_mul = my_array * 5
print("Multiplied array is \t\t",my_mul)

my_div = my_array / 2
print("Divided array is \t\t",my_div)

## Array should have all elements of the same datatype
my_datatyp = np.array(["hello",12,5.0])
print("Mixed element type", type(my_datatyp))
print("Mixed element type \t\t",type(my_datatyp[1]))

## Shape of array gives length of array
print("Shape of array is \t\t", my_datatyp.shape)

## Operations on 2 vectors
## Vectors should have the same shape
vector1 = np.array([1,4,10])
vector2 = np.array([3.5,6,9])

print("Original vectors are \t",vector1,"\t",vector2)
print("Added vectors are \t",vector1+vector2)
print("Subtracted vectors are \t",vector1 - vector2)
print("Multipied vectors are \t",vector1 * vector2)
print("Divided vectors are \t",vector1 / vector2)

## Comparison of vectors
vector1 > 3
greater_than_3_vector = vector1[vector1 > 3]
print("Greater than 3 array is \t\t",greater_than_3_vector)


# # PRACTICE PROBLEMS
# 
# create a NumPy array called heights = [6.5,7.3,5.1,4.9]
# multiply all of the heights by 4 and store that into a new variable called huge_people
# create a new array basketballers with only those entries in heights that are > 6
# create another array little_people with only those entries in heights that are < 5

# In[29]:


heights = np.array([6.5,7.3,5.1,4.9])

print("Array heigths is \t\t",heights)

huge_people = heights * 4
print("Multipled array huge_people is \t\t",huge_people)

basketballers = heights[heights > 6]
print("Basketballer array is \t\t",basketballers)

little_people = heights[heights < 5]
print("Little people array is \t\t",little_people)


# In[30]:


## Matrices

## Defining
## Shape of Matrix
## Matrices slicing
## Scalar operations
## 2 Matrices operations


# In[3]:


M1 = np.array([[1,2,4],[1,3,4]])
V1=np.array([10,12,13])

print("Shape of M1 is \t\t",M1.shape)
print("Shape of V1 is \t\t",V1.shape)

#Mul_Mat = M1.dot(V1)
#print("Multiplied Matrix \t\t",Mul_Mat, Mul_Mat.shape)

#Mul_Mat2 = V1.dot(M1)
#print("Multiplied Matrix \t\t",Mul_Mat2, Mul_Mat2.shape)


# In[4]:


Mat = np.array([[1,2],[3,4]])


# In[13]:


print("Shape of Matrix is ",Mat.shape)
print(Mat[0,:],type(Mat[0,:]))
print(Mat[1,:])


# In[17]:


print("Addition of scalar 5 \n", Mat + 5)
print("Subtraction of scalar 5\n", Mat - 5)
print("Multiplication of scalar 5\n", Mat * 5)
print("Division of scalar 5\n", Mat / 5)


# In[31]:


my_first_matrix = np.array([[20,12],[30,1]])
my_second_matrix = np.array([[1,3],[6,7]])
my_third_matrix = np.array([[1,2,4],[1,3,5]])


# In[35]:


print("First Matrix is \n",my_first_matrix)
print("Second Matrix is \n",my_second_matrix)

print("Are my first 2 matrices of same shape ? ",my_first_matrix.shape == my_second_matrix.shape)

print("Addition of first two matrices : \n",my_first_matrix + my_second_matrix)
print("Subtraction of first two matrices : \n",my_first_matrix - my_second_matrix)

print("Are my first and 3rd matrices of the same shape :\n",my_first_matrix.shape == my_third_matrix.shape)
## Cannot add matrices of different shape
##print("Trying to add first and 3rd matrix : ",my_first_matrix + my_third_matrix)

print("First Matrix dot Second Matrix \n",my_first_matrix.dot(my_second_matrix))
print("Second Matrix dot First Matrix \n",my_second_matrix.dot(my_first_matrix))

print("First Matrix dor third Matrix \n",my_first_matrix.dot(my_third_matrix))

# print(my_third_matrix.dot(my_first_matrix)) - cannot do dot product of this shape


# In[38]:


print(np.eye(3)*3)


# In[40]:


## Inverse of a  matrix

print("Inverse of my first matrix is \n",np.linalg.inv(my_first_matrix))


# In[41]:


## Matrix Division using numpy linalg

# my_first_matrix/my_second_matrix  == my_first_matrix.dot(np.linalg.inv(my_second_matrix))

my_second_inverse = np.linalg.inv(my_second_matrix)

div_matrix = my_first_matrix.dot(my_second_inverse)
print("Division result is \n ",div_matrix)


# In[47]:


## transpose of a matrix

A = np.array([[10,2],[-1,5],[3,3]])
B = np.array([2,3,31])

print("Matrix A is :\n", A)
print("Matrix B is :\n", B)

print("Transpose of matrix A is :\n",A.T, A.T.shape)
print("Transpose of matrix B is :\n",B.T, B.T.shape)

#print("Multiply A and B will give error :\n", A.dot(B))
print("Multiply A Transpose and B transpose will work :\n", A.T.dot(B.T), A.T.dot(B.T).shape)


# In[48]:


## Practice Problem


# In[62]:


C = np.array([[12,3,4],[1,-1,10],[2,5,2]])
D = np.array([3,-2,10])

print("Matrix C is :\n",C, C.shape)
print("Vector D is :\n",D, D.shape)

print("Inverse of C is \n",np.linalg.inv(C))

#print(C.dot(D))

#print(C.T.dot(D.T))

#print(D*C)
print(np.dot(C,D.T))
print(np.dot(D,C))
print(np.dot(C,D))


# In[ ]:




