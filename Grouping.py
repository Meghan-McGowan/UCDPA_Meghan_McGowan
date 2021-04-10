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

#Replaceing missing values for gender, enrolled university and major discipline
hr_analysis_concat['gender'] = hr_analysis_concat['gender'].fillna('Other')
hr_analysis_concat['enrolled_university'] = hr_analysis_concat['enrolled_university'].fillna('no_enrollment')
hr_analysis_concat['major_discipline'] = hr_analysis_concat['major_discipline'].fillna('No Major')

#Replaceing missing values for all other columns
hr_analysis=hr_analysis_concat.fillna(0, inplace=True)

#Confirm missing values have been populated
missing_values=hr_analysis_concat.isnull().sum()
print(missing_values)

print(hr_analysis_concat.info())

#Replacing values where >20
hr_analysis_concat['experience']. replace(['>20', '<1'],['21', '1'], inplace=True)
print(hr_analysis_concat['experience']. unique())

#Replacing last new job values
hr_analysis_concat['last_new_job']. replace(['>4', 'never'],['5', '0'], inplace=True)
print(hr_analysis_concat['last_new_job']. unique())

#Confirm missing values have been populated
missing_values=hr_analysis_concat.isnull().sum()
print(missing_values)

print(hr_analysis_concat.info())

#Groupby gender and training hours
gender_training = hr_analysis_concat.groupby(["gender"], as_index = False)[["training_hours"]].mean() .sort_values(by="training_hours", ascending=False)
print(gender_training)

#Groupby relevent experience and training hours
relevent_experience_training = hr_analysis_concat.groupby(["relevent_experience"], as_index = False)[["training_hours"]].mean() .sort_values(by="training_hours", ascending=False)
print(relevent_experience_training)

#Groupby gender, training hours and target
gender_training_target = hr_analysis_concat.groupby(["gender","target"], as_index = False)[["training_hours"]].mean() .sort_values(by="training_hours", ascending=False)
print(gender_training_target)



