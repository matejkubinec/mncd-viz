from app.models import Actor, ActorToCommunity, Community


def parse_community_list(
    community_list: str,
) -> tuple[list[ActorToCommunity], list[Actor], list[Community]]:
    lines = community_list.split("\n")
    actorToCommunity: list[ActorToCommunity] = []
    actors: list[Actor] = []
    communities: list[Community] = []

    reading = "actor-community"
    for line in lines:

        if line.startswith("# Actors"):
            reading = "actors"
            continue
        elif line.startswith("# Communities"):
            reading = "communities"
            continue
        elif line == "":
            break

        if reading == "actor-community":
            a, c = line.split(" ")
            actorToCommunity.append(ActorToCommunity(int(a), int(c)))

        elif reading == "actors":
            a, n = line.split(" ")
            actors.append(Actor(int(a), n))

        elif reading == "communities":
            c, n = line.split(" ")
            communities.append(Actor(int(c), n))

    return actorToCommunity, actors, communities
