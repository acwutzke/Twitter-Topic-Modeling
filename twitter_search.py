import tweepy
import config
import re

# instantiate api
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# search tweets
tweets=tweepy.Cursor(
	api.search, 
	q='$AAPL',
	lang="en").items(5)

for tweet in tweets:
	t=tweet.text
	t=re.sub(' +', ' ', t)
	print(t)

# write search result to file
# file=r'twitter_data.txt'
# with open(file, 'a') as f:
# 	for tweet in tweets:
# 		# f.write('AAPL,')
# 		t=tweet.text
# 		f.write(t.rstrip("\n"))
# 		# f.write('\n')