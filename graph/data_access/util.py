from graph.models.release import Release
from graph.models.artist import Artist


def get_resource_by_uid(resource_type, uid):
    if resource_type == 'artists':
        return Artist.nodes.get(uid=uid)
    if resource_type == 'releases':
        return Release.nodes.get(uid=uid)

def set_node_property(node, key, updates):
    """
    Accesses a single key-value pair from the updates dict and updates
    the node's corresponding property with that value.

    """
    existing_value = getattr(node, key)
    update = updates.get(key) if updates.get(key) is not None else existing_value
    setattr(node, key, update)

def connect_a_to_b(a, b, relation):
    """
    Connects node a to b along relation
    """
    getattr(a, relation).connect(b)

