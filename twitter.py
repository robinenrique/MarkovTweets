import twitter as ts
from TwitterSearch import TwitterUserOrder

i = 0

	#tso = TwitterSearchOrder()
	#tso.setKeywords(['Calgary', 'WildRoseBrewery'])
	#tso.setLanguage('en')
	#tso.setCount(5)
	
	#tso.setIncludeEntities(False)
tuo = TwitterUserOrder('NeinQuarterly') # create a TwitterUserOrder
	
ts = TwitterSearch(
	consumer_key = '8eQxQ9m0tAWs6xuG7U6ta4qq7',
	consumer_secret = 'jR2RSYqAgJACRq2jVzAS7M8whB3ErAsdrsfCoVZE6L32pdT4Va',
	access_token = '2855949602-VN8IbEkTYFmBulVGYvu0boUOnzlXwiAC4bClCK9',
	access_token_secret = 'ZG1GqcoyWqkVHCTKfcHfWV833sTd9droEYKKa1LsWtdQG'
	)

for tweet in ts.searchTweetsIterable(tso):
	if i < 5:
		 print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
	i = i+1

