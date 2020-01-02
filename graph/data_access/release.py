from graph.models.release import Release
from graph.data_access.util import set_node_property, connect_a_to_b


def create_release_node(catalogue_num, release_date, title):
    """
    :param string catalogue_num:
    :param datetime.date release_date:
    :param string title:
    :return neomodel.Node:

    Add a Release node to the graph
    """
    release = Release(catalogue_num=catalogue_num, title=title, release_date=release_date).save()
    return release
    
def get_release_nodes():
    """
    :return []neomodel.Node:

    Return all Release nodes
    """
    return Release.nodes.all()

def get_release_node(uid):
    """
    :return neomodel.Node:

    Return a single Release node
    """
    return Release.nodes.get(uid=uid)

def update_release_node(release, updates):
    """
    Update a release node with the specified updates.
    For metadata updates the update value is a primitive,
    for relation updates the update value is the destination node.
    """

    METADATA_UPDATES = ['catalogue_num', 'release_date', 'title']
    GRAPH_UPDATES = ['artists', 'genres', 'labels', 'songs']
    for metadata_update in METADATA_UPDATES:
        set_node_property(release, metadata_update, updates)
    
    for graph_update in GRAPH_UPDATES:
        [connect_a_to_b(release, node, graph_update) for node in updates[graph_update]]
    release = release.save()
    return release
