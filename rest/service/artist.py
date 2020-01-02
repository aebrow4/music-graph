from graph.data_access.artist import create_artist_node, get_artist_nodes, get_artist_node, update_artist_node
from rest.util import hydrate_update_for_node


def create_artist(name):
    artist = create_artist_node(name)
    return artist

def get_artists():
    return get_artist_nodes()

def update_artist(uid, updates):
    """
    """
    artist = get_artist_node(uid=uid)
    releases = []
    GRAPH_UPDATES = ['genres', 'labels', 'songs', 'releases']
    for node_type in GRAPH_UPDATES:
        hydrated_update = hydrate_update_for_node(updates, node_type) 

    updated = update_artist_node(artist, hydrated_update)
    return updated
