from graph.models.release import Release

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
    """

    release.title = 'foo'
    release = release.save()
    return release
