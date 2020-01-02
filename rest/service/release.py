from graph.data_access.release import get_release_node, get_release_nodes, update_release_node, create_release_node
from graph.data_access.artist import get_artist_node
from graph.data_access.util import get_resource_by_uid
from common.util import date_to_iso_string
from rest.util import hydrate_update_for_node


def get_releases():
    results = get_release_nodes()
    releases = [r.to_dict() for r in results]
    releases_formatted = [_format_release_date_iso(r) for r in releases]
    return releases

def create_release(catalogue_num, release_date, title):
    release = create_release_node(catalogue_num, release_date, title)
    return release

def update_release(uid, updates):
    """
    Update a relase record by setting metadata properties
    and connecting to other nodes

    :param dict updates: keys are destination node 
    """
    release = get_release_node(uid=uid)
    
    GRAPH_UPDATES = ['artists', 'genres', 'labels', 'songs']
    for node_type in GRAPH_UPDATES:
        hydrated_update = hydrate_update_for_node(updates, node_type) 

    updated = update_release_node(release, hydrated_update)
    return updated

def _format_release_date_iso(d):
    """
    :param dict d: a dictionary that is assumed to have a key 'release_date'
    :return dict: the same dictionary

    Mutates a dict in place, coercing release_date from datetime.date to string
    """
    d['release_date'] = date_to_iso_string(d['release_date'])
    return d
