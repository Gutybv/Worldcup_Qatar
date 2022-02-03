import tweepy
import schedule
import time
from countdown import count

# create a .env file to keep the security of yours Twitter API KEYS
CONSUMER_KEY ='CONSUMER_KEY'
CONSUMER_SECRET ='CONSUMER_SECRET'
ACCESS_TOKEN ='ACCESS_TOKEN'
ACCESS_TOKEN_SECRET ='ACCESS_TOKEN_SECRET'
# You can find these tokens in this link https://developer.twitter.com/en/portal/dashboard


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
# Authentication 



# Def to twitt
def countdown():
    countdown = count()
    api.update_status(countdown)
    



# Use time to twitt every x hours
def main():
    # schedule.every().hour.do(twitt_price)
    schedule.every(12).hours.do(countdown)
    while True:
        try:
            schedule.run_pending()
            time.sleep(2) 
        except tweepy.TweepError as e:
            raise e
    

if __name__ == '__main__':
    main()