import pandas as pd
from collections import defaultdict
import re

def analyze_suspicious(df, partition):
    comms = defaultdict(list)
    for idx, row in df.iterrows():
        comm_id = partition.get(str(row["user_id"]), -1)
        comms[comm_id].append(row)

    print("\n🔍 Suspicious Community Candidates:\n")
    for cid, tweets in comms.items():
        texts = [t["content"] for t in tweets]
        urls = [u for t in tweets for u in (t["urls"] if pd.notna(t["urls"]) else [])]

        # simple heuristics
        url_ratio = len(urls) / max(len(tweets), 1)
        dup_text_ratio = len(set(texts)) / max(len(texts), 1)

        if url_ratio > 0.5 or dup_text_ratio < 0.6:  # many repeated URLs or duplicate text
            print(f"⚠️ Community {cid} looks suspicious: {len(tweets)} tweets, url_ratio={url_ratio:.2f}, dup_text_ratio={dup_text_ratio:.2f}")
            for t in tweets[:3]:  # show 3 sample tweets
                print("  -", t["content"][:120])
