# coding: utf-8

from typing import List

from fastapi import APIRouter, Body, HTTPException, Path, Query, Response
from starlette.responses import Response
from odmantic.bson import ObjectId

from ..models.db import get_db
from ..models.room import Room


router = APIRouter()


@router.post(
    "/room",
    tags=["Room"],
    summary="Creates a Room",
    status_code=201,
)
async def create_Room(
    roomCreate: Room = Body(None, description="The Room to be created")
) -> Room:
    """This operation creates a Room entity."""

    try:
        return await get_db().save(roomCreate)
    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


@router.delete(
    "/room/{id}",
    tags=["Room"],
    summary="Deletes a Room",
)
async def delete_Room(
    id: ObjectId = Path(..., description="Identifier of the Room")
) -> None:
    """This operation deletes a Room entity."""

    try:
        room = await get_db().find_one(Room, Room.id == id)
        if room is None:
            raise HTTPException(404)
        await get_db().delete(room)
        return Response(status_code=204)
    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


@router.get(
    "/room",
    tags=["Room"],
    summary="List or find Room objects",
)
async def list_Room(
    fields: str = Query(
        None, description="Comma-separated properties to be provided in response"
    ),
    offset: int = Query(
        0,
        description="Requested index for start of resources to be provided in response",
    ),
    limit: int = Query(
        10, description="Requested number of resources to be provided in response"
    ),
) -> List[Room]:
    """This operation list or find Room entities"""

    try:
        return await get_db().find(Room, skip=offset, limit=limit)
    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


@router.get(
    "/room/{id}",
    tags=["Room"],
    summary="Retrieves a Room by ID",
)
async def retrieve_Room(
    id: ObjectId = Path(..., description="Identifier of the Room"),
    fields: str = Query(
        None, description="Comma-separated properties to provide in response"
    ),
) -> Room:
    """This operation retrieves a Room entity. Attribute selection is enabled for all first level attributes."""

    try:
        room = await get_db().find_one(Room, Room.id == id)
        if room is None:
            raise HTTPException(404)
        return room
    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e
