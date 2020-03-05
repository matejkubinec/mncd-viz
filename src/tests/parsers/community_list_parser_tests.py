from models import ActorToCommunity, Actor, Community
from parsers import CommunityListParser
import unittest


class CommunityListParserTests(unittest.TestCase):

    def test_without_metadata(self):
        community_list = "\n".join([
            "0 1",
            "1 0"
        ])

        parser = CommunityListParser()
        output = parser.parse_community_list(community_list)

        self.assertListEqual(output[0], [
            ActorToCommunity(0, 1),
            ActorToCommunity(1, 0)
        ])
        self.assertListEqual(output[1], [])
        self.assertListEqual(output[2], [])

    def test_with_actors_metadata(self):
        community_list = "\n".join([
            "0 1",
            "1 0",
            "# Actors",
            "0 a0",
            "1 a1"
        ])

        parser = CommunityListParser()
        output = parser.parse_community_list(community_list)

        self.assertListEqual(output[0], [
            ActorToCommunity(0, 1),
            ActorToCommunity(1, 0)
        ])
        self.assertListEqual(output[1], [
            Actor(0, "a0"),
            Actor(1, "a1")
        ])
        self.assertListEqual(output[2], [])

    def test_with_communities_metadata(self):
        community_list = "\n".join([
            "0 1",
            "1 0",
            "# Communities",
            "0 c0",
            "1 c1"
        ])

        parser = CommunityListParser()
        output = parser.parse_community_list(community_list)

        self.assertListEqual(output[0], [
            ActorToCommunity(0, 1),
            ActorToCommunity(1, 0)
        ])
        self.assertListEqual(output[1], [])
        self.assertListEqual(output[2], [
            Community(0, "c0"),
            Community(1, "c1")
        ])

    def test_with_all_metadata(self):
        community_list = "\n".join([
            "0 1",
            "1 0",
            "# Actors",
            "0 a0",
            "1 a1",
            "# Communities",
            "0 c0",
            "1 c1"
        ])

        parser = CommunityListParser()
        output = parser.parse_community_list(community_list)

        self.assertListEqual(output[0], [
            ActorToCommunity(0, 1),
            ActorToCommunity(1, 0)
        ])
        self.assertListEqual(output[1], [
            Actor(0, "a0"),
            Actor(1, "a1")
        ])
        self.assertListEqual(output[2], [
            Community(0, "c0"),
            Community(1, "c1")
        ])
