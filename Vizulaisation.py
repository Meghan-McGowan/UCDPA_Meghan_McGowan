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

#Groupby major discipline and count the majors
major_level = hr_analysis_concat.groupby(["major_discipline"], as_index = False).count() .sort_values(by="major_discipline", ascending=False)
print(major_level)

#Show the number of major displines
labels = 'STEM', 'No Major','Humanities', 'Other', 'Business Degree', 'Arts'
count = [16113, 3370, 749, 421, 364, 270]
explode = ( 0.05,0 ,0 ,0, 0, 0 )  # only "explode" the 2nd slice (i.e. 'STEM')

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

Majors = ["16113 STEM",
          "3370 No_Major",
          "749 Humanities",
          "421 Other",
          "364 Business Degree",
          "270 Arts"]

data = [float(x.split()[0]) for x in Majors]
Major_Discipline = [x.split()[-1] for x in Majors]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%)".format(pct)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, Major_Discipline,
          title="Major Discipline",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=6, weight="bold")

ax.set_title("Major Discipline")

plt.show()