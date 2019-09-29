#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Player Count
import pandas as pd


# In[3]:


# Load in file
csvpath = "../Resources/02-Homework_04-Pandas_Instructions_HeroesOfPymoli_Resources_purchase_data1.csv"


# In[4]:


# Read and display the CSV with Pandas
purchase_data_df = pd.read_csv(csvpath)
purchase_data_df.head(16)


# In[5]:


purchase_data_df.count()


# In[6]:


# Player Count
array_unique_player_count = purchase_data_df["SN"].unique()
unique_player_count = len(array_unique_player_count)
unique_player_count


# In[115]:


list_unique_player_count = list(array_unique_player_count)
list_unique_player_count


# In[7]:


Player_Count_df = pd.DataFrame({
    "Number of Unique Players": [unique_player_count],
})
Player_Count_df


# In[8]:


# Number of Unique Items
array_item_id_unique = purchase_data_df["Item ID"].unique()
unique_item_count = len(array_item_id_unique)
unique_item_count


# In[9]:


# Average Purchase Price
array_average_item_price = purchase_data_df["Price"].unique()
average_item_price = (sum(array_average_item_price) / len(array_average_item_price))
average_item_price


# In[10]:


# Total Number of Purchases
total_number_purchases = purchase_data_df["Purchase ID"].count()
total_number_purchases


# In[11]:


# Total Revenue
total_revenue = purchase_data_df["Price"].sum()
total_revenue


# In[12]:


# Purchasing Analysis (Total) output

unique_item_count = str(unique_item_count)
average_item_price = "$" + str(format(average_item_price, "4.2f"))
total_number_purchases = str(total_number_purchases)
total_revenue = "$" + str(format(total_revenue, "4.2f"))

print(unique_item_count)
print(average_item_price)
print(total_number_purchases)
print(total_revenue)


# In[13]:


Purchasing_Analysis_df = pd.DataFrame({
    "Number of Unique Items": [unique_item_count],
    "Average Price": [average_item_price],
    "Total Number of Purchases": [total_number_purchases],
    "Total Revenue": [total_revenue]
})
Purchasing_Analysis_df


# Gender Demographics

# In[14]:


purchase_data_df.head()


# In[15]:


purchase_data_df['Gender'].unique()


# In[16]:


# Create a List of unique users
list_unique_player_count = list(array_unique_player_count)
list_unique_player_count


# In[17]:


# Remove duplicate intances of users
unique_user_id_df = purchase_data_df.drop_duplicates(subset='SN')


# In[18]:


# Set the 'SN' as our index
unique_user_id_df = unique_user_id_df.set_index('SN')
unique_user_id_df


# In[19]:


# variables to hold counts
unique_player_male_count = 0
unique_player_female_count = 0
unique_player_other_count = 0


# In[20]:


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
        


# In[21]:


# Male Player Count
unique_player_male_count


# In[22]:


unique_player_male_percent = unique_player_male_count / unique_player_count
unique_player_male_percent


# In[23]:


# Female Player Count
unique_player_female_count


# In[24]:


unique_player_female_percent = unique_player_female_count / unique_player_count
unique_player_female_percent


# In[25]:


# Other Player Count
unique_player_other_count


# In[26]:


unique_player_other_percent = unique_player_other_count / unique_player_count
unique_player_other_percent


# In[27]:


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


# In[28]:


Gender_Demographics_df = pd.DataFrame({
    "Gender": ["Male", "Female", "Other / Non-Disclosed"],
    "Total Count": [unique_player_male_count, unique_player_female_count, unique_player_other_count],
    "Percentage of Players": [unique_player_male_percent, unique_player_female_percent, unique_player_other_percent]
})

Gender_Demographics_df = Gender_Demographics_df.set_index("Gender")

Gender_Demographics_df


# Purchasing Analysis (Gender)

# In[29]:


purchase_data_df.head(16)


# In[30]:


# Dataframe housing female data
male_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Male", :]
male_df.head(16)


# In[31]:


purchase_count_male = male_df["SN"].count()
purchase_count_male


# In[32]:


average_purchase_price_male = male_df["Price"].mean()
average_purchase_price_male


# In[33]:


total_purchase_price_male = male_df["Price"].sum()
total_purchase_price_male


# In[34]:


average_male_purchase = float(total_purchase_price_male) / float(unique_player_male_count)
average_male_purchase


# In[35]:


# Dataframe housing female data
female_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Female", :]
female_df.head()


# In[36]:


purchase_count_female = female_df["SN"].count()
purchase_count_female


# In[37]:


average_purchase_price_female = female_df["Price"].mean()
average_purchase_price_female


# In[38]:


total_purchase_price_female = female_df["Price"].sum()
total_purchase_price_female


# In[39]:


average_female_purchase = float(total_purchase_price_female) / float(unique_player_female_count)
average_female_purchase


# In[40]:


# Dataframe housing female data
other_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Other / Non-Disclosed", :]
other_df.head()


# In[41]:


purchase_count_other = other_df["SN"].count()
purchase_count_other


# In[42]:


average_purchase_price_other = other_df["Price"].mean()
average_purchase_price_other


# In[43]:


total_purchase_price_other = other_df["Price"].sum()
total_purchase_price_other


# In[44]:


average_other_purchase = float(total_purchase_price_other) / float(unique_player_other_count)
average_other_purchase


# In[45]:


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


# In[46]:


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

# In[47]:


purchase_data_df.head()


# In[48]:


age_max = purchase_data_df["Age"].max()
age_max


# In[49]:


# Create bins in which to place values based upon users age
bins = [0, 10, 14, 19, 24, 29, 34, 39, 50]

# Create labels for these bins
age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# In[50]:


# Slice the data and place it into bins
pd.cut(purchase_data_df["Age"], bins, labels = age_labels).head()


# In[51]:


# Place the data series into a new column inside of the DataFrame
purchase_data_df["Age Range"] = pd.cut(purchase_data_df["Age"], bins, labels = age_labels)
purchase_data_df


# In[52]:


unique_user_id_df = purchase_data_df.drop_duplicates(subset='SN')
unique_user_id_df


# In[53]:


array_age_range_count = unique_user_id_df["Age Range"].value_counts()
array_age_range_count


# In[54]:


array_age_range_count = array_age_range_count.sort_index()
array_age_range_count


# In[55]:


list_age_range_count = list(array_age_range_count)
list_age_range_count


# In[56]:


age_percentage_of_players = [i / sum(list_age_range_count) for i in list_age_range_count]
age_percentage_of_players = [format(i, "4.2%") for i in age_percentage_of_players]
age_percentage_of_players


# In[57]:


Age_Demographics_df = pd.DataFrame(list(zip(age_labels, list_age_range_count, age_percentage_of_players)), columns = ["Age Range", "Total Count", "Percentage of Players"])
Age_Demographics_df


# In[58]:


Age_Demographics_df = Age_Demographics_df.set_index("Age Range")
Age_Demographics_df


# Purchasing Analysis (Age)

# In[ ]:





# In[59]:


purchase_data_df.head()


# In[60]:


purchasing_analysis = purchase_data_df.groupby("Age Range")
array_purchase_count = purchasing_analysis["Price"].count()
array_average_purchase_price = purchasing_analysis["Price"].mean()
array_total_purchase_value = purchasing_analysis["Price"].sum()
array_total_purchase_value


# In[61]:


list_purchase_count = list(array_purchase_count)
list_purchase_count


# In[62]:


list_average_purchase_price = list(array_average_purchase_price)
list_average_purchase_price


# In[63]:


list_total_purchase_value = list(array_total_purchase_value)
list_total_purchase_value


# In[64]:


Purchasing_Analysis_Age_df = pd.DataFrame(list(zip(age_labels, list_purchase_count, list_average_purchase_price, list_total_purchase_value)), columns = ["Age Range", "Purchase Count", "Average Purchase Price", "Total Purchase Value"])
Purchasing_Analysis_Age_df


# In[65]:


Purchasing_Analysis_Age_df = Purchasing_Analysis_Age_df.set_index("Age Range")
Purchasing_Analysis_Age_df


# In[66]:


# Create bins in which to place values based upon users age
#bins = [0, 10, 14, 19, 24, 29, 34, 39, 50]

# Create labels for these bins
#age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# In[67]:


# Player Count
# array_unique_player_count = purchase_data_df["SN"].unique()
# unique_player_count = len(array_unique_player_count)
# unique_player_count


# In[68]:


Purchasing_Analysis_Age_df["Avg Total Purchase per Person"] = (Purchasing_Analysis_Age_df["Total Purchase Value"] / unique_player_count)


# In[69]:


Purchasing_Analysis_Age_df.head()


# Top Spenders

# In[70]:


purchase_data_df.head()


# In[80]:


Array_Purchase_Count = purchase_data_df["SN"].value_counts()
List_Purchase_Count = list(Array_Purchase_Count)
List_Purchase_Count


# In[82]:


Array_SN = purchase_data_df["SN"]
List_SN = list(Array_SN)
List_SN


# In[92]:


Array_User_Purchases = purchase_data_df["Price"]
List_User_Purchases = list(Array_User_Purchases)
List_User_Purchases


# In[ ]:


#Top_Spenders_df["Purchase Count"] =  for i in purchase_data_df["SN"]
#Top_Spenders_df.head()


# In[83]:


Top_Spenders_df = pd.DataFrame(list(zip(List_SN, List_Purchase_Count)), columns = ["SN", "Purchase Count"])
Top_Spenders_df


# In[87]:


Top_Spenders_df["Total Purchase Value"] = ""
Top_Spenders_df["Average Purchase Price"] = ""
Top_Spenders_df.head()


# Dictionary creation addition and exhicution example:

# In[100]:


wordFreqDic = {}


# In[101]:


wordFreqDic.update( {'before' : 23} )


# In[104]:


for k, v in wordFreqDic.items():
    print(str(k) + str(v))


# In[ ]:





# In[129]:


user_dictionary = {}


# In[130]:


#Top_Spenders_df["Total Purchase Value"] = purchase_data_df["SN"] 
for i in List_SN:
    popped_user = List_SN.pop()
    popped_purchase = List_User_Purchases.pop()
    user_dictionary.update( {str(popped_user) : float(popped_purchase) })


# In[131]:


for k, v in user_dictionary.items():
    print(str(k) + " / " + str(v))


# In[132]:


list_user_purchases = []


# In[133]:


for i in List_SN:
    popped_user = List_SN.pop()
    popped_purchase = List_User_Purchases.pop()
    if popped_user in user_dictionary
        user_dictionary.update( {str(popped_user) : list_user_purchases.append(popped_purchase) })


# In[ ]:


for k, v in user_dictionary.items():
    print(str(k) + " / " + str(v))


# In[ ]:


for k, v in user_dictionary.item()
    


# In[ ]:


from collections import defaultdict

d["flow"].append("flow")
d["flow"].append("wolf")

