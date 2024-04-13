'''
Let us see now how we would automate our categorical data. Firstly let us see our dataset and then we can start with the analysis.
'''

import pandas as pd
df=pd.read_csv('googleplaystore.csv')
df.head()

'''
Output

Total number of apps in each category
'''

categories = {}

for name in df['Category'].unique():
    ct = 0
    for i in df['Category']:
        if(i == name):
            ct += 1
    categories[name] = ct
    
print(categories)

'''
{'ART_AND_DESIGN': 65, 'AUTO_AND_VEHICLES': 85, 'BEAUTY': 53, 'BOOKS_AND_REFERENCE': 231, 'BUSINESS': 460, 'COMICS': 60, 'COMMUNICATION': 387, 'DATING': 234, 'EDUCATION': 156, 'ENTERTAINMENT': 149, 'EVENTS': 64, 'FINANCE': 366, 'FOOD_AND_DRINK': 127, 'HEALTH_AND_FITNESS': 341, 'HOUSE_AND_HOME': 88, 'LIBRARIES_AND_DEMO': 85, 'LIFESTYLE': 382, 'GAME': 1144, 'FAMILY': 1972, 'MEDICAL': 463, 'SOCIAL': 295, 'SHOPPING': 260, 'PHOTOGRAPHY': 335, 'SPORTS': 384, 'TRAVEL_AND_LOCAL': 258, 'TOOLS': 843, 'PERSONALIZATION': 392, 'PRODUCTIVITY': 424, 'PARENTING': 60, 'WEATHER': 82, 'VIDEO_PLAYERS': 175, 'NEWS_AND_MAGAZINES': 283, 'MAPS_AND_NAVIGATION': 137, '1.9': 1}
 
So we now know now each and every category is containing how many apps in our dataset with the help of this analysis.

Total number of apps in each Type
'''

types = {}

for name in df['Type'].unique():
    ct = 0
    for i in df['Type']:
        if(i == name):
            ct += 1
    types[name] = ct
    
print(types)

'''
Output

{'Free': 10039, 'Paid': 800, nan: 0, '0': 1}
So there are a total of 10039 Free apps and 800 Paid apps.

Total number of apps in each Content Rating
'''

content_rating = {}

for name in df['Content Rating'].unique():
    ct = 0
    for i in df['Content Rating']:
        if(i == name):
            ct += 1
    content_rating[name] = ct
    
print(content_rating)

'''
Output

{'Everyone': 8714, 'Teen': 1208, 'Everyone 10+': 414, 'Mature 17+': 499, 'Adults only 18+': 3, 'Unrated': 2, nan: 0}
So we can see from here the number of apps in each and every individual Content Rating
'''
