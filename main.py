import pandas as pd
from src.collect_data import collect_tweets
from src.build_graph import build_graph
from src.detect_communities import detect_communities
from src.suspicious_analysis import analyze_suspicious
from src.visualize import visualize_graph

# Step 1: collect tweets
df = collect_tweets(query="#CryptoGiveaway since:2025-09-01 until:2025-09-30", limit=500)

# Step 2: build graph
G = build_graph("data/tweets.csv")

# Step 3: detect communities
partition = detect_communities(G)

# Step 4: analyze suspicious clusters
analyze_suspicious(df, partition)

# Step 5: visualize
visualize_graph(G, partition)
