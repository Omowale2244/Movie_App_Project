from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get('/movies', tags=['Movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()                                     
    result = MovieService(db).get_movies()            
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.get('/movies/{id}', tags=['Movies'], response_model=Movie, status_code=404)
def get_movie(id: int = Path(ge=1, le=100)) -> Movie:
    db = Session()                                     
    result = MovieService(db).get_movie(id)           
    if not result:
        return JSONResponse(status_code=404, content={"Message:": "Movie not available, check later"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/', tags=['Movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=1, max_length=10)) -> List[Movie]:
    db = Session()                                     
    result = MovieService(db).get_movies_by_category(category) 
    if not result:
        return JSONResponse(status_code=404, content={"Message:": "Movie not available, check later"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.post('/movies', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()                                      
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"Message": "Movie not available, check later"})


@movie_router.put('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"Message:": "Movie not available, check later"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=201, content={"Message:": "your movie has been updated succesfully"})


@movie_router.delete('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()                                      
    result : MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"Message:": "Movie not available"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"Message": "Movie deleted successful"})