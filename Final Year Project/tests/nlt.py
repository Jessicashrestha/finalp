import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import praw
import seaborn as sns

# nltk.download('vader_lexicon')
# nltk.download('stopwords')

reddit = praw.Reddit(client_id = 'PyuxYZi0uwur3g',
                     client_secret = 'WBp2E7O1i7smsBTGSVVSL2BHDbc',
                     user_agent = 'khaoula202')

headlines = set()
for sub in reddit.subreddit('Business').new(limit = 1000):
    # print(headlines)
    headlines.add(sub.title)
print(len(headlines))
# print(headlines)

sia = SIA()
results = []
for line in headlines:
    scores = sia.polarity_scores(line)
    scores['headline'] = line
    results.append(scores)
df = pd.DataFrame.from_records(results)



df['label'] = 0
df.loc[df['compound'] > 0.1, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1
print(df.head())

df.to_csv('test.csv')


