#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Player Count
import pandas as pd


# In[2]:


# Load in file
csvpath = "../Resources/02-Homework_04-Pandas_Instructions_HeroesOfPymoli_Resources_purchase_data1.csv"


# In[3]:


# Read and display the CSV with Pandas
purchase_data_df = pd.read_csv(csvpath)
purchase_data_df.head(16)


# In[4]:


purchase_data_df.count()


# In[5]:


# Player Count
array_unique_player_count = purchase_data_df["SN"].unique()
unique_player_count = len(array_unique_player_count)
unique_player_count


# In[6]:


Player_Count_df = pd.DataFrame({
    "Number of Unique Players": [unique_player_count],
})
Player_Count_df


# In[7]:


# Number of Unique Items
array_item_id_unique = purchase_data_df["Item ID"].unique()
unique_item_count = len(array_item_id_unique)
unique_item_count


# In[8]:


# Average Purchase Price
array_average_item_price = purchase_data_df["Price"].unique()
average_item_price = (sum(array_average_item_price) / len(array_average_item_price))
average_item_price


# In[9]:


# Total Number of Purchases
total_number_purchases = purchase_data_df["Purchase ID"].count()
total_number_purchases


# In[10]:


# Total Revenue
total_revenue = purchase_data_df["Price"].sum()
total_revenue


# In[11]:


# Purchasing Analysis (Total) output

unique_item_count = str(unique_item_count)
average_item_price = "$" + str(format(average_item_price, "4.2f"))
total_number_purchases = str(total_number_purchases)
total_revenue = "$" + str(format(total_revenue, "4.2f"))

print(unique_item_count)
print(average_item_price)
print(total_number_purchases)
print(total_revenue)


# In[12]:


Purchasing_Analysis_df = pd.DataFrame({
    "Number of Unique Items": [unique_item_count],
    "Average Price": [average_item_price],
    "Total Number of Purchases": [total_number_purchases],
    "Total Revenue": [total_revenue]
})
Purchasing_Analysis_df


# Gender Demographics

# In[13]:


purchase_data_df.head()


# In[14]:


purchase_data_df['Gender'].unique()


# In[15]:


# Create a List of unique users
list_unique_player_count = list(array_unique_player_count)
list_unique_player_count


# In[16]:


# Remove duplicate intances of users
unique_user_id_df = purchase_data_df.drop_duplicates(subset='SN')


# In[17]:


# Set the 'SN' as our index
unique_user_id_df = unique_user_id_df.set_index('SN')
unique_user_id_df


# In[18]:


# variables to hold counts
unique_player_male_count = 0
unique_player_female_count = 0
unique_player_other_count = 0


# In[19]:


# for loop to count instances of player gender
for i in list_unique_player_count:
    user_name = i
    unique_player_gender = unique_user_id_df.loc[user_name, "Gender"]
    if unique_player_gender == "Male":
        unique_player_male_count = unique_player_male_count + 1
    elif unique_player_gender == "Female":
        unique_player_female_count = unique_player_female_count + 1
    elif unique_player_gender == "Other / Non-Disclosed":
        unique_player_other_count = unique_player_other_count + 1
        


# In[20]:


# Male Player Count
unique_player_male_count


# In[21]:


unique_player_male_percent = unique_player_male_count / unique_player_count
unique_player_male_percent


# In[22]:


# Female Player Count
unique_player_female_count


# In[23]:


unique_player_female_percent = unique_player_female_count / unique_player_count
unique_player_female_percent


# In[24]:


# Other Player Count
unique_player_other_count


# In[25]:


unique_player_other_percent = unique_player_other_count / unique_player_count
unique_player_other_percent


# In[26]:


# Gender Demographics Output


unique_player_male_count = str(unique_player_male_count)
unique_player_female_count = str(unique_player_female_count)
unique_player_other_count = str(unique_player_other_count)

unique_player_male_percent = str(format(unique_player_male_percent, "4.2%"))
unique_player_female_percent = str(format(unique_player_female_percent, "4.2%"))
unique_player_other_percent = str(format(unique_player_other_percent, "4.2%"))

print(unique_player_male_count)
print(unique_player_male_percent)
print(unique_player_female_count)
print(unique_player_female_percent)
print(unique_player_other_count)
print(unique_player_other_percent)


# In[27]:


Gender_Demographics_df = pd.DataFrame({
    "Gender": ["Male", "Female", "Other / Non-Disclosed"],
    "Total Count": [unique_player_male_count, unique_player_female_count, unique_player_other_count],
    "Percentage of Players": [unique_player_male_percent, unique_player_female_percent, unique_player_other_percent]
})

Gender_Demographics_df = Gender_Demographics_df.set_index("Gender")

Gender_Demographics_df


# Purchasing Analysis (Gender)

# In[28]:


purchase_data_df.head(16)


# In[29]:


# Dataframe housing female data
male_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Male", :]
male_df.head(16)


# In[30]:


purchase_count_male = male_df["SN"].count()
purchase_count_male


# In[31]:


average_purchase_price_male = male_df["Price"].mean()
average_purchase_price_male


# In[32]:


total_purchase_price_male = male_df["Price"].sum()
total_purchase_price_male


# In[35]:


average_male_purchase = float(total_purchase_price_male) / float(unique_player_male_count)
average_male_purchase


# In[36]:


# Dataframe housing female data
female_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Female", :]
female_df.head()


# In[37]:


purchase_count_female = female_df["SN"].count()
purchase_count_female


# In[38]:


average_purchase_price_female = female_df["Price"].mean()
average_purchase_price_female


# In[39]:


total_purchase_price_female = female_df["Price"].sum()
total_purchase_price_female


# In[41]:


average_female_purchase = float(total_purchase_price_female) / float(unique_player_female_count)
average_female_purchase


# In[42]:


# Dataframe housing female data
other_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Other / Non-Disclosed", :]
other_df.head()


# In[43]:


purchase_count_other = other_df["SN"].count()
purchase_count_other


# In[44]:


average_purchase_price_other = other_df["Price"].mean()
average_purchase_price_other


# In[45]:


total_purchase_price_other = other_df["Price"].sum()
total_purchase_price_other


# In[47]:


average_other_purchase = float(total_purchase_price_other) / float(unique_player_other_count)
average_other_purchase


# In[48]:


# Purchasing Analysis (Gender) Output

purchase_count_male = str(purchase_count_male)
purchase_count_female = str(purchase_count_female)
purchase_count_other = str(purchase_count_other)

average_purchase_price_male = "$" + str(format(average_purchase_price_male, "4.2f"))
average_purchase_price_female = "$" + str(format(average_purchase_price_female, "4.2f"))
average_purchase_price_other = "$" + str(format(average_purchase_price_other, "4.2f"))

total_purchase_price_male = "$" + str(format(total_purchase_price_male, "4.2f"))
total_purchase_price_female = "$" + str(format(total_purchase_price_female, "4.2f"))
total_purchase_price_other = "$" + str(format(total_purchase_price_other, "4.2f"))

average_male_purchase = "$" + str(format(average_male_purchase, "4.2f"))
average_female_purchase = "$" + str(format(average_female_purchase, "4.2f"))
average_other_purchase = "$" + str(format(average_other_purchase, "4.2f"))

print(purchase_count_male)
print(purchase_count_female)
print(purchase_count_other)
print(average_purchase_price_male)
print(average_purchase_price_female)
print(average_purchase_price_other)
print(total_purchase_price_male)
print(total_purchase_price_female)
print(total_purchase_price_other)
print(average_male_purchase)
print(average_female_purchase)
print(average_other_purchase)


# In[49]:


Purchasing_Analysis_Gender_df = pd.DataFrame({
    "Gender": ["Male", "Female", "Other / Non-Disclosed"],
    "Purchase Count": [purchase_count_male, purchase_count_female, purchase_count_other],
    "Average Purchase Price": [average_purchase_price_male, average_purchase_price_female, average_purchase_price_other],
    "Total Purchase Value": [total_purchase_price_male, total_purchase_price_female, total_purchase_price_other],    
    "Avg Total Purchase per Person": [average_male_purchase, average_female_purchase, average_other_purchase]   
})

Purchasing_Analysis_Gender_df = Purchasing_Analysis_Gender_df.set_index("Gender")

Purchasing_Analysis_Gender_df


# Age Demographics

# In[50]:


purchase_data_df.head()


# In[51]:


age_max = purchase_data_df["Age"].max()
age_max


# In[52]:


# Create bins in which to place values based upon users age
bins = [0, 10, 14, 19, 24, 29, 34, 39, 50]

# Create labels for these bins
age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# In[53]:


# Slice the data and place it into bins
pd.cut(purchase_data_df["Age"], bins, labels = age_labels).head()


# In[131]:


# Place the data series into a new column inside of the DataFrame
purchase_data_df["Age Range"] = pd.cut(purchase_data_df["Age"], bins, labels = age_labels)
purchase_data_df


# In[98]:


unique_user_id_df = purchase_data_df.drop_duplicates(subset='SN')
unique_user_id_df


# In[122]:


array_age_range_count = unique_user_id_df["Age Range"].value_counts()
array_age_range_count


# In[125]:


array_age_range_count = array_age_range_count.sort_index()
array_age_range_count


# In[126]:


list_age_range_count = list(array_age_range_count)
list_age_range_count


# In[127]:


age_percentage_of_players = [i / sum(list_age_range_count) for i in list_age_range_count]
age_percentage_of_players = [format(i, "4.2%") for i in age_percentage_of_players]
age_percentage_of_players


# In[129]:


Age_Demographics_df = pd.DataFrame(list(zip(age_labels, list_age_range_count, age_percentage_of_players)), columns = ["Age Range", "Total Count", "Percentage of Players"])
Age_Demographics_df


# In[130]:


Age_Demographics_df = Age_Demographics_df.set_index("Age Range")
Age_Demographics_df


# Purchasing Analysis (Age)

# In[138]:


purchase_data_df.head()


# In[149]:


Purchasing_Analysis_Age_df = purchase_data_df[["Age Range", "Price"]]
Purchasing_Analysis_Age_df


# In[159]:


#age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
age_labels_indices = []

purchase_price_collection = []

for i in Purchasing_Analysis_Age_df:
    if Purchasing_Analysis_Age_df.iloc[0, i] == "<10":
        purchase_price_collection = purchase_price_collection.append(purchase_data_df["Price"][i])
print(purchase_price_collection)


# In[133]:


array_age_range_count = array_age_range_count.sort_index()
array_age_range_count


# In[134]:


list_age_range_count = list(array_age_range_count)
list_age_range_count


# In[136]:


age_percentage_of_players = [i / sum(list_age_range_count) for i in list_age_range_count]
age_percentage_of_players = [format(i, "4.2%") for i in age_percentage_of_players]
age_percentage_of_players


# In[137]:


Age_Demographics_df = pd.DataFrame(list(zip(age_labels, list_age_range_count, age_percentage_of_players)), columns = ["Age Range", "Total Count", "Percentage of Players"])
Age_Demographics_df


# Top Spenders

# In[ ]:




