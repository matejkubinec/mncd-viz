from typing import List
from models import Actor, ActorToCommunity, Community
from parsers import CommunityListParser


def convert_community_list(community_list: str) -> (List[ActorToCommunity], List[Actor], List[Community]):
    parser = CommunityListParser()
    return parser.parse_community_list(community_list)
