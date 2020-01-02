from graph.data_access.util import get_resource_by_uid


def hydrate_update_for_node(updates, node_type):
    """
    Mutates the input dict, replacing the uids with their corresponding node objects

    :param dict updates: keys are node types, values are uids.
                         the uids represent nodes that will be connected to
                         by a source node
    :param string node_type: the type of the node that will be updated
    :return dict:
    """
    for uid in updates[node_type]:
        updates[node_type] = [get_resource_by_uid(node_type, uid) for uid in updates[node_type]]
    
    return updates

