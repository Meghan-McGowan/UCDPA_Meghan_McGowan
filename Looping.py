import pandas as pd

train_data = pd.read_csv("aug_train.csv")
print(train_data)

test_data = pd.read_csv("aug_test.csv")
print(test_data)

#Train dataframe analysis
print(train_data.head())
print(train_data.info())

#Test dataframe analysis
print(test_data.head())
print(test_data.info())

#Merge dataframes using concat
hr_analysis_concat=pd.concat([test_data,train_data])
print(hr_analysis_concat.info())

#Identify the number of missing values in each column
missing_values=hr_analysis_concat.isnull().sum()
print(missing_values)

#Replaceing missing values for gender and enrolled university
hr_analysis_concat['gender'] = hr_analysis_concat['gender'].fillna('Other')
hr_analysis_concat['enrolled_university'] = hr_analysis_concat['enrolled_university'].fillna('No Enrollment ')

#Replaceing missing values for all other columns using numpy
hr_analysis=hr_analysis_concat.fillna(0, inplace=True)

#Confirm missing values have been populated
missing_values=hr_analysis_concat.isnull().sum()
print(missing_values)

print(hr_analysis_concat.info())

#Create Lists
female_education1 = {'education_level': 'Masters', 'major-disciplne': 'STEM'}
female_education2 = {'education_level': 'Graduate', 'major-disciplne': 'Business Degree'}
female_education3 = {'education_level': 'Graduate', 'major-disciplne': 'STEM'}
female_education =[female_education1,female_education2,female_education3]

#Iterate through the rows using a loop
for i in female_education:
    print(i)

#Iterate through the rows by the education_level key
for i in female_education:
    print(i['education_level'])

#Loop and condition
selected_education_level = {}
education_level_lookup = "Masters"
for i in female_education:
    if 'education_level' in i:
        if i['education_level'] == education_level_lookup:
            selected_education_level = i

print(selected_education_level)







