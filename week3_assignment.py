#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df = pd.read_csv("financial_transactions.csv")


# In[6]:


df.head()


# In[7]:


df.shape


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[58]:


df.columns = df.columns.str.lower()


# In[59]:


df.columns


# In[56]:


df["price"].median()


# In[57]:


df["price"] = df["price"].fillna(df["price"].median())


# In[53]:


df["product_name"] = df["product_name"].str.strip().str.lower()
df["payment_method"] = df["payment_method"].str.strip().str.lower()
df["transaction_status"] = df["transaction_status"].str.strip().str.lower()
df["customer_id"] = df["customer_id"].str.strip().str.lower()


# In[54]:


df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")


# In[55]:


df = df.drop_duplicates()


# In[45]:


df["total_value"] = df["quantity"] * df["price"]


# In[43]:


df = pd.read_csv("financial_transactions.csv")


# In[48]:


df.head()


# In[49]:


def my_function(x):
    if x >= 100:
        return "bulk"
    else:
        return "regular"

df["transaction_type"] = df["quantity"].apply(my_function)


# In[50]:


df[["quantity", "transaction_type"]].head()


# In[60]:


df.head()


# In[61]:


df["year"] = df["transaction_date"].dt.year


# In[62]:


df.head()


# In[63]:


df["month"] = df["transaction_date"].dt.month


# In[64]:


df.head()


# In[65]:


def high_value(total):
    if total > 2000:
        return True
    else:
        return False
df["high_value"] = df["total_value"].apply(high_value)        


# In[66]:


df.head()


# In[ ]:


def categorize_revenue(total):
    if total < 500:
        return "low"
    elif 500 <= total <= 2000:
        return "medium"
    else:  # total > 2000
        return "high"


df["revenue_category"] = df["total_value"].apply(categorize_revenue)


# In[79]:


df["transaction_weekday"] = df["transaction_date"].dt.day_name()


# In[80]:


df.head()


# In[81]:


df.tail()


# In[69]:


df.to_csv("clean_transactions.csv", index="false")


# In[77]:


def clean_transaction_data(file_name):
    import pandas as pd

    df = pd.read_csv("financial_transactions.csv")

    df.columns = df.columns.str.lower()

    df["price"].median()

    df["price"] = df["price"].fillna(df["price"].median())

    df["product_name"] = df["product_name"].str.strip().str.lower()
    df["payment_method"] = df["payment_method"].str.strip().str.lower()
    df["transaction_status"] = df["transaction_status"].str.strip().str.lower()
    df["customer_id"] = df["customer_id"].str.strip().str.lower()

    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

    df = df.drop_duplicates()

    df["total_value"] = df["quantity"] * df["price"]

    def my_function(x):
        if x >= 100:
            return "bulk"
        else:
            return "regular"

    df["transaction_type"] = df["quantity"].apply(my_function)

    df["year"] = df["transaction_date"].dt.year

    df["month"] = df["transaction_date"].dt.month


    def high_value(total):
        if total > 2000:
            return True
        else:
            return False
        df["high_value"] = df["total_value"].apply(high_value) 


    def categorize_revenue(total):
        if total < 500:
            return "low"
        elif 500 <= total <= 2000:
            return "medium"
        else:  # total > 2000
            return "high"


    df["revenue_category"] = df["total_value"].apply(categorize_revenue) 


    df["transaction_weekday"] = df["transaction_date"].dt.day_name()


    df.to_csv("clean_transactions.csv", index="false")

    return df    




# In[78]:


clean_df = clean_transaction_data("financial_transactions.csv")


# In[ ]:




