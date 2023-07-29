# Python
from typing import Any

# Django
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

# Local
from .models import (
    Album,
    Artist,
    Song
)


def index(request: WSGIRequest) -> HttpResponse:
    """index."""

    # TODO: сделать так чтобы текущий
    # юзер мог видеть только свои альбомы
    # user: User = request.user
    #
    albums: QuerySet[Album] = Album.objects.all()
    songs: QuerySet[Song] = Song.objects.all()
    context: dict[str, QuerySet[Any]] = {
        'albums': albums,
        'songs': songs
    }
    return render(
        request,
        'main/index.html',
        context
    )


def detail(
    request: WSGIRequest,
    album_id: int
) -> HttpResponse:
    """detail."""

    user: User = request.user
    album: QuerySet[Album] = Album.objects.get(
        id=album_id
    )
    context: dict[str, QuerySet[Any]] = {
        'album': album,
        'user': user
    }
    return render(
        request,
        'main/detail.html',
        context
    )


def song_detail(
        request: WSGIRequest, 
        song_id: int
) -> HttpResponse:
    """Song_detail."""

    user: User = request.user
    song: QuerySet[Song] = Song.objects.get(
        id=song_id
    )
    context = {
        'song': song,
        'user': user
    }
    return render(
        request, 
        'main/song_detail.html', 
        context
    )