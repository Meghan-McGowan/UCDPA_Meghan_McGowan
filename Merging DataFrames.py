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

#Merge dataframes using join and add a suffix to identify the orginal data frame
hr_analysis_join=train_data.join(test_data, lsuffix='_train', rsuffix='_test')
print(hr_analysis_join.info())
