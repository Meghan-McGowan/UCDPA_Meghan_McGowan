import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

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

#Groupby target and relevent experience
target_experience =hr_analysis_concat.groupby(['relevent_experience','target']).agg({'target':'count'})
print(target_experience)

labels = ['Searching for a job', 'Not searching for a job']
Has_relevent_experience= [2961, 12355]
No_relevent_experience = [1816, 4155]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
ax1 = ax.bar(x - width/2, Has_relevent_experience, width, label='Has relevent experience')
ax2 = ax.bar(x + width/2, No_relevent_experience, width, label='No relevent experience', color='g')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of People')
ax.set_title('Relevent Experience & Job Searching')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(ax1, padding=3)
ax.bar_label(ax2, padding=3)

fig.tight_layout()

plt.show()

