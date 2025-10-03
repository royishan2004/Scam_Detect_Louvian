import snscrape.modules.twitter as sntwitter
import pandas as pd

def collect_tweets(query="#CryptoGiveaway since:2025-09-01 until:2025-09-30", limit=1000, save_path="data/tweets.csv"):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        tweets.append({
            "tweet_id": tweet.id,
            "user_id": tweet.user.id,
            "username": tweet.user.username,
            "date": tweet.date,
            "content": tweet.content,
            "hashtags": tweet.hashtags,
            "urls": tweet.outLinks,
            "reply_to": tweet.inReplyToUser,
        })
        if i >= limit:
            break

    df = pd.DataFrame(tweets)
    df.to_csv(save_path, index=False)
    print(f"✅ Saved {len(df)} tweets to {save_path}")
    return df
