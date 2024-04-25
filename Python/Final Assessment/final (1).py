# -*- coding: utf-8 -*-
"""Final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1czjL8Y5m0rFz4_yLU4saykvVl2y6wv0e
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""Q1"""

df = pd.read_csv("/content/Final Dataset - IPL.csv")

df.head()

df.info()

df.dtypes

df.shape

df.isnull().sum()

"""Q2"""

df.isnull().sum()
# df.fillna()
# df.replace()
#df.dropna()
# For missing values, we can check through the first condition, the dataset has no missing values.
# if we have we can use the following two ways fillna() or replace() to fill the missing values
# Also we could use df.dropna() to drop the null values

df.duplicated()
# df.drop_duplicates()
# the dataset does not contain any duplicates, but if it has we use the df.dropduplicates to drop the duplicates

"""Q3"""

df.describe()

num_col = df.select_dtypes(include=['float64','int64']).columns
print(num_col)

mean = df[num_col].mean()
print(mean)

median = df[num_col].median()
print(median)

mode = df[num_col].mode()
print(mode)

max=df[num_col].max()
min = df[num_col].min()
range = max-min
print(range)

standard_deviation = df[num_col].std()
print(standard_deviation)

variance = df[num_col].var()
print(variance)

#we could infere the central tendancies and variablility of each numeric values using the mean, median and variance functions
# we also infere the range of each variable , its maximum and minimum values and also their standard deviation, how much the points are deviated

"""Q4"""

# hist,scatter,box,bar, pie

df.head(3)

# Hostogram
df['first_ings_score'].plot(kind='hist', bins=20, title='first_ings_score')
plt.gca().spines[['top', 'right',]].set_visible(False)
# the histogram shows an idea of the frequency of the first innings scores and how its distributed

# Scatter Plot
df.plot(kind='scatter', x='first_ings_score', y='second_ings_score', s=32, alpha=.8)
#shows how the values are scattered

df.plot(kind='scatter', x='first_ings_wkts', y='second_ings_wkts', s=32, alpha=.8)
#it shows a big scattering of the values of the wickets in first and second innings

# box plot
plt.boxplot(df['highscore'])
plt.show()
#  the plot shows there is an outlier present near 140

# Bar Chart
size = df.groupby('toss_decision').size()
size.plot(kind='barh', color=['red','blue'])
#we could infere from the bar chart , most of the time after the win the toss, their decisions is to field first

#pie chart
venue = df['venue'].value_counts()
plt.figure(figsize=(4,4))
plt.pie(venue,labels= venue.index, autopct = '%1.1f%%')
plt.show()

#Pie chart gives a picture of the venue allotment of the matches, mumbai stadium had the most number of matches played
#  Eden Garden and narendra modi stadium being the least number of matches played

"""Q5"""

df[cor_col] = pd.columns=['toss_decision','venue']

print(df[num_col].corr())

cor = df[num_col].corr()
sns.heatmap(cor, annot = True)

"""  Q6"""

plt.figure(figsize=(15,5))
df.boxplot()
plt.show()
#yes there are outlines as we could identify here through the box plot, but in this scenario, removing the outliners would not be a feasible option
# as we could see the outliers are in the innings score, and scores are needed to calculate the sum or winning team
# so in this case, outliers can be present.

df.head(3)

"""Q7"""

max_individual_performance = df.groupby('player_of_the_match')['highscore'].max().nlargest(5)
# top five high scores
print(max_individual_performance)

max_individual_performance = df.groupby('player_of_the_match')['highscore'].max().head(5)
min_individual_performance = df.groupby('player_of_the_match')['highscore'].min().head(5)
average_individual_performance = df.groupby('player_of_the_match')['highscore'].mean().head(5)

print(max_individual_performance)
print(min_individual_performance)
print(average_individual_performance)

# First calculation shows the maximum of highscore each player has score
# second shows least they have scored within their high score margine
# shows the average high scores each playe gets
# everything is displayed only ten values but not sorted in any order, because the inference is show each player max scores

high_score = df.groupby(['match_winner','player_of_the_match'])['highscore'].count().nlargest(10)
print(high_score)

max_per_match = df.groupby(['player_of_the_match','match_id','venue'])['match_winner'].count()
print(max_per_match)
# ṭhis shows how many player of the match they have got in the respective venues

team = df.groupby(['team1','venue'])['match_winner'].count()
print(team)

# this shows number of times teams won in each stadiums

"""Q8"""

details_top = df.groupby(['match_winner','player_of_the_match'])['match_winner'].count().nlargest(5)
print(details_top)
# this shows the top five people who are player of the match and the impact they created on the winning teams
# here kuldeep yadav was four times player of the match amd also won four matches, as count is takes based on match winner team

bowling_top = df.groupby(['match_winner','best_bowling'])['match_winner'].count().nlargest(5)
print(bowling_top)
# the shows the top five bowlers with the times of win , Yuzvendra Chahal has got best bowler four times and the impact is , the team also won those times
# match team and best bowling player grouped by number of wins on their team, this shows the impact

"""Q9

1 - No datas was missing
2 - We could infere different relationsgips through the charts, Dr Dy Patil Sport Academy Mumbai had the higest numnber of matches played and Eden Garden and narendra modi stadium being the least number of matches played.
3 - Many teams who won the toss chose to field first
4 - kuldeep Yadav of delhi has the most number of man of the match and delhi has won for times
5 - Yuzvendra Chahal has got the best bowler four times and impacted his team to win  four times
6 high scores Quinton de Kock     140
Jos Buttler         116
Rajat Patidar       112
K L Rahul           103
Yuzvendra Chahal    103
"""