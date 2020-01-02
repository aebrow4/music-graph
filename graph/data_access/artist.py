from graph.models.artist import Artist
from graph.data_access.util import set_node_property, connect_a_to_b


def get_artist_node(uid):
    """
    :return neomodel.Node:

    Return a single Artist node
    """
    return Artist.nodes.get(uid=uid)

def get_artist_nodes():
    """
    :return []neomodel.Node:

    Return all Artist nodes
    """
    return Artist.nodes.all()

def create_artist_node(name):
    """
    :param string name: name of the artist
    :return neomodel.Node:

    Add an Artist node to the graph
    """
    return Artist(name=name).save()

def update_artist_node(artist, updates):
    METADATA_UPDATES = ['name']
    GRAPH_UPDATES = ['genres', 'labels', 'songs', 'releases']
    for metadata_update in METADATA_UPDATES:
        set_node_property(artist, metadata_update, updates)
    
    for graph_update in GRAPH_UPDATES:
        [connect_a_to_b(artist, node, graph_update) for node in updates[graph_update]]
    artist = artist.save()
    return artist
