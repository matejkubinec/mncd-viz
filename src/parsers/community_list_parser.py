from models import ActorToCommunity, Community, Actor
from typing import List


class CommunityListParser():

    def parse_community_list(self, community_list: str) -> (List[ActorToCommunity], List[Actor], List[Community]):
        lines = community_list.split("\n")
        actorToCommunity: List[ActorToCommunity] = []
        actors: List[Actor] = []
        communities: List[Community] = []

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
