from graph.data_access.artist import create_artist_node, get_artist_nodes


def create_artist(name):
    artist = create_artist_node(name)
    return artist

def get_artists():
    return get_artist_nodes()
