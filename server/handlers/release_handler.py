from flask import g

from server.rebar import rebar, registry
from rest.v0.schema.release import ReleaseResponseSchema
from rest.service.release import update_release, get_releases, create_release
from graph.data_access.release import create_release_node


def handle_create_release():
    catalogue_num = rebar.validated_body["catalogue_num"]
    release_date = rebar.validated_body["release_date"]
    title = rebar.validated_body.get("title")

    release = create_release(catalogue_num, release_date, title)
    return ReleaseResponseSchema().load(release.to_dict())

def handle_get_releases():
    releases = get_releases()
    return ReleaseResponseSchema(many=True).load(releases)

def handle_update_release():
    uid = rebar.validated_body["uid"]
    artist_uids = rebar.validated_body.get('artists')
    updates = {
            'catalogue_num': rebar.validated_body.get('catalogue_num'),
            'title': rebar.validated_body.get('title'),
            'release_date': rebar.validated_body.get('release_date'),
            'artists': rebar.validated_body.get('artists', []),
            'genres': rebar.validated_body.get('genres', []),
            'labels': rebar.validated_body.get('labels', []),
            'songs': rebar.validated_body.get('songs', []),
        }

    updated = update_release(uid, updates)
           
    return ReleaseResponseSchema().load(updated.to_dict())


def _wipe_releases():
    for node in Release.nodes.all():
        node.delete()

