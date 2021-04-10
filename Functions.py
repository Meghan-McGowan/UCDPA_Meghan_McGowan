import pandas as pd
#Create Lists
female_education1 = {'education_level': 'Masters', 'major-disciplne': 'STEM'}
female_education2 = {'education_level': 'Graduate', 'major-disciplne': 'Business Degree'}
female_education3 = {'education_level': 'Graduate', 'major-disciplne': 'STEM'}
female_education =[female_education1,female_education2,female_education3]

male_education1 = {'education_level': 'Masters', 'major-disciplne': 'STEM'}
male_education2 = {'education_level': 'Graduate', 'major-disciplne': 'Business Degree'}
male_education3 = {'education_level': 'Masters', 'major-disciplne': 'STEM'}
male_education =[male_education1,male_education2,male_education3]

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
        if i['education_level'] == education_level_lookup:
            selected_education_level = i

print(selected_education_level)





