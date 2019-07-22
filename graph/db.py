from neo4j import GraphDatabase
from config.base import get_config


config = get_config()


def get_driver():
    return GraphDatabase.driver(
        "bolt://localhost:7687", auth=("neo4j", config["NEO4J_PASSWORD"])
    )
