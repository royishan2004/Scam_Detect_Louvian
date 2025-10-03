import pandas as pd
import networkx as nx

def build_graph(path="data/tweets.csv"):
    df = pd.read_csv(path)
    G = nx.Graph()

    for row in df.itertuples():
        user = str(row.user_id)
        G.add_node(user, username=row.username)

        # Mentions
        if pd.notna(row.content) and "@" in row.content:
            for word in row.content.split():
                if word.startswith("@") and len(word) > 1:
                    G.add_edge(user, word, weight=G.get_edge_data(user, word, {}).get("weight", 0) + 1)

        # Reply edges
        if pd.notna(row.reply_to):
            G.add_edge(user, str(row.reply_to), weight=G.get_edge_data(user, str(row.reply_to), {}).get("weight", 0) + 1)

    print(f"✅ Graph built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G
