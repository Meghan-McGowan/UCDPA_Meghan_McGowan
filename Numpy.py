import numpy as np
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

#Replaceing missing values for gender,enrolled university and major discipline using numpy
hr_analysis_concat['gender'] = hr_analysis_concat['gender'].replace(np.nan, 'Other')
hr_analysis_concat['enrolled_university'] = hr_analysis_concat['enrolled_university'].replace(np.nan, 'no_enrollment')
hr_analysis_concat['major_discipline'] = hr_analysis_concat['major_discipline'].replace(np.nan, 'No Major')

print(hr_analysis_concat['gender'].unique())
print(hr_analysis_concat['enrolled_university'].unique())
print(hr_analysis_concat['major_discipline'].unique())

#Replaceing missing values for all other columns using numpy
hr_analysis=hr_analysis_concat.replace(np.nan,0, inplace=True)
print(hr_analysis_concat.info())

#Numpy array
np_education_level= np.array(['Graduate', 'High School', 'Masters', '0', 'Phd', 'Primary School'])
np_major_discipline= np.array(['STEM', 'No Major', 'Other', 'Business Degree', 'Arts', 'Humanities'])
np_education_level_major = np.array([['Graduate', 'High School', 'Masters', '0', 'Phd', 'Primary School'],['STEM', 'No Major', 'Other', 'Business Degree', 'Arts', 'Humanities']])

#Show the shape of the data
#Show the first row of the np.array
#Show the second row of the np.array
print(np_education_level_major.shape)
print(np_education_level_major[0])
print(np_education_level_major[1])

#Show High School and No Major
print(np_education_level_major[0:2,1:2])











