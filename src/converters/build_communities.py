def build_communities(community_list: str) -> dict:
    rows = [row.split(" ") for row in community_list.splitlines()]

    actor_to_community = dict()
    communities = set()

    for a, c in rows:
        actor_to_community[a] = c
        communities.add(c)

    return actor_to_community, communities
