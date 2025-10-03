import community as community_louvain
import networkx as nx

def detect_communities(G):
    partition = community_louvain.best_partition(G, weight="weight")
    modularity = community_louvain.modularity(partition, G, weight="weight")
    print(f"✅ Detected {len(set(partition.values()))} communities (Modularity={modularity:.4f})")
    return partition
