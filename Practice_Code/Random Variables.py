#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import statsmodels as stats


# In[21]:


## Discrete and Continuous Random Variables

n_trials = 10
prob_heads = 0.5
num_heads = np.random.binomial(n_trials,prob_heads)
print("Num heads is ",num_heads)
print("Fraction of heads ",float(num_heads)/n_trials)


# In[22]:


cont_variable=np.random.exponential(size=7)
print(cont_variable)


# In[23]:


#### Exercise
n_trials = 10000
prob_heads = 0.5
num_heads=np.random.binomial(n_trials,prob_heads)
fraction_heads=float(num_heads)/n_trials
print(fraction_heads)


# In[24]:


## Binomial distribution

n_trials_binomial = 10000
binomial_data=np.random.binomial(n_trials,prob_heads,n_trials_binomial)
#binomial_number=np.random.binomial(n_trials,prob_heads)
print(binomial_data)


# In[25]:


#sns.mpl.pyplot.hist(binomial_data,normed=True,alpha=0.5)


# In[26]:


mu=0
sigma=1
n_trials = 10000
normal_data=np.random.normal(mu,sigma,n_trials)
sns.distplot(normal_data)


# In[28]:


sns.distplot(normal_data, hist_kws={"cumulative":True},kde_kws={"cumulative":True})
print("CDF of normal distribution:")


# In[31]:


negative_mu = -3
positive_mu = 3
negative_mu_normal_data = np.random.normal(negative_mu, sigma, n_trials)
positive_mu_normal_data = np.random.normal(positive_mu, sigma, n_trials)
sns.distplot(negative_mu_normal_data)
sns.distplot(positive_mu_normal_data)
sns.distplot(normal_data)

print("100000 values sampled from three normal distributions with different mean=-3,0,5 and same standard deviation= 1:")


# In[32]:


sns.distplot(negative_mu_normal_data, hist_kws={"cumulative":True},kde_kws={"cumulative":True})
sns.distplot(positive_mu_normal_data, hist_kws={"cumulative":True},kde_kws={"cumulative":True})
sns.distplot(normal_data, hist_kws={"cumulative":True},kde_kws={"cumulative":True})
print("CDF of three normal distributions with different mean=-3,0,5 and same standard deviation= 1:")


# In[34]:


larger_sigma = 3
largest_sigma = 5
#Generate 2 collections of 100,000 samples from each distribution. 
larger_sigma_normal_data = np.random.normal(mu, larger_sigma, n_trials)
largest_sigma_normal_data = np.random.normal(mu, largest_sigma, n_trials)
#plot all 3 distributions on the same plot
sns.distplot(largest_sigma_normal_data)
sns.distplot(larger_sigma_normal_data)
sns.distplot(normal_data)
print("100,000 values sampled from three normal distributions with the same mean = 0 but different standard deviations = 1,3,5:")


# In[38]:


sns.distplot(largest_sigma_normal_data, hist_kws={"cumulative":True},kde_kws={"cumulative":True})
sns.distplot(larger_sigma_normal_data, hist_kws={"cumulative":True},kde_kws={"cumulative":True})
sns.distplot(normal_data, hist_kws={"cumulative":True},kde_kws={"cumulative":True})
sns.mpl.pyplot.xlim((-10,10))
print("CDF for three normal distributions with the same mean = 0 but different standard deviations = 1,3,5:")


# In[36]:


##Exponential distribution

e=np.random.exponential(size=n_trials)
sns.mpl.pyplot.hist(e,bins=100,normed=True)
sns.mpl.pyplot.xlim((0,11))


# In[39]:


sns.distplot(e, hist_kws={"cumulative":True},kde_kws={"cumulative":True})
sns.mpl.pyplot.xlim((0,11))
print("CDF of exponential distribution:")


# In[ ]:




