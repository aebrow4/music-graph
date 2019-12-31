from neo4j import GraphDatabase
import neomodel
from config.base import get_config
from graph.models.base_model import BaseModel

config = get_config()


def get_driver():
    """
    Returns a context manager for writing Cypher inside transactions.
    """
    return GraphDatabase.driver(
        "bolt://localhost:7687", auth=("neo4j", config["NEO4J_PASSWORD"])
    )


def init_neomodel_client():
    password = config["NEO4J_PASSWORD"]
    neomodel.config.DATABASE_URL = f"bolt://neo4j:{password}@localhost:7687"
