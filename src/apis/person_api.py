# coding: utf-8

from typing import List

from fastapi import APIRouter, Body, HTTPException, Path, Query, Response
from starlette.responses import Response
from odmantic.bson import ObjectId

from ..models.person import Person
from ..models.db import get_db

router = APIRouter()


@router.post(
    "/person",
    tags=["Person"],
    summary="Creates a Person",
    status_code=201,
)
async def create_Person(
    PersonCreate: Person = Body(None, description="The Person to be created"),
) -> Person:
    """This operation creates a Person entity."""

    try:
        return await get_db().save(PersonCreate)
    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


@router.delete(
    "/person/{id}",
    tags=["Person"],
    summary="Deletes a Person",
)
async def delete_Person(
    id: ObjectId = Path(..., description="Identifier of the Person")
) -> None:
    """This operation deletes a Person entity."""

    try:
        person = await get_db().find_one(Person, Person.id == id)
        if person is None:
            raise HTTPException(404)
        await get_db().delete(person)
        return Response(status_code=204)
    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


@router.get(
    "/person",
    tags=["Person"],
    summary="List or find Person objects",
)
async def list_Person(
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
) -> List[Person]:
    """This operation list or find Person entities"""

    try:
        return await get_db().find(Person, skip=offset, limit=limit)
    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


@router.get(
    "/person/{id}",
    tags=["Person"],
    summary="Retrieves a Person by ID",
)
async def retrieve_Person(
    id: ObjectId = Path(..., description="Identifier of the Person"),
    fields: str = Query(
        None, description="Comma-separated properties to provide in response"
    ),
) -> Person:
    """This operation retrieves a Person entity. Attribute selection is enabled for all first level attributes."""

    try:
        person = await get_db().find_one(Person, Person.id == id)
        if person is None:
            raise HTTPException(404)
        return person
    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e
