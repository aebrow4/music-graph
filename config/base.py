import os


_CONFIG = {"NEO4J_PASSWORD": os.getenv("NEO4J_PASSWORD")}

if _CONFIG["NEO4J_PASSWORD"] is None:
    print("You must specify the NEO4J_PASSWORD environment variable.")


def get_config():
    return _CONFIG
