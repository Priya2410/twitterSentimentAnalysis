import tweepy
ACCESS_TOKEN = "1324649238609891328-VxijcVXLvEPynwdnwfV9h62TzfJOP1"
ACCESS_TOKEN_SECRET = "4Llx0FGVTE1sGL4zRx7FhB0vwKb738iubZzR5dVnfNLou"
API_KEY = "sdqyBrXyBcGcfNeJQeOxymWSg"
API_SECRET_KEY = "TVLtVL0YoR0lhsn6yBCxXh8NhvUT3uVyXuhswcWBDiEwbqUJ6Q"

# To authorize
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
api.update_status(status="Hello World I AM PRIYA!")


