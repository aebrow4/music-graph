from flask import g

from server.rebar import rebar, registry
from server.rest.v0.schema.release import ReleaseResponseSchema
from graph.models.release import Release
from common.util import date_to_iso_string


def create_release():
    catalogue_num = rebar.validated_body["catalogue_num"]
    title = rebar.validated_body.get("title")
    release_date = rebar.validated_body["release_date"]

    release = Release(catalogue_num=catalogue_num, title=title, release_date=release_date).save()
    return ReleaseResponseSchema().load(release.to_dict())

def get_releases():
    results = Release.nodes.all()
    releases = [r.to_dict() for r in results]
    releases_formatted = [_format_release_date_iso(r) for r in releases]

    return ReleaseResponseSchema(many=True).load(releases_formatted)


def _wipe_releases():
    for node in Release.nodes.all():
        node.delete()

def _format_release_date_iso(d):
    """
    :param dict d: a dictionary that is assumed to have a key 'release_date'
    :return dict: the same dictionary

    Mutates a dict in place, coercing release_date from datetime.date to string
    """
    d['release_date'] = date_to_iso_string(d['release_date'])
    return d
