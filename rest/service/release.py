from graph.data_access.release import get_release_node, get_release_nodes, update_release_node, create_release_node
from common.util import date_to_iso_string

def update_release(uid, updates={}):
    """
    """
    release = get_release_node(uid=uid)
    # TODO do validation n shit
    update_release_node(release, updates)
    return release

def create_release(catalogue_num, release_date, title):
    release = create_release_node(catalogue_num, release_date, title)
    return release

def get_releases():
    results = get_release_nodes()
    releases = [r.to_dict() for r in results]
    releases_formatted = [_format_release_date_iso(r) for r in releases]
    return releases

def _format_release_date_iso(d):
    """
    :param dict d: a dictionary that is assumed to have a key 'release_date'
    :return dict: the same dictionary

    Mutates a dict in place, coercing release_date from datetime.date to string
    """
    d['release_date'] = date_to_iso_string(d['release_date'])
    return d
