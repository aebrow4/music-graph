from graph.models.artist import Artist


def create_artist_node(name):
    """
    :param string name: name of the artist
    :return neomodel.Node:

    Add an Artist node to the graph
    """
    return Artist(name=name).save()

def get_artist_nodes():
    """
    :return []neomodel.Node:

    Return all Artist nodes
    """
    return Artist.nodes.all()
