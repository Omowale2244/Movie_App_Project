from pydantic import BaseModel, Field
from typing import Optional, List

class Movie(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=5, max_length=20)
    overview: str = Field(min_length=20, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=10)

    model_config = {
     "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Fast and Furious",
                    "overview": "This movies is an interesting action movie",
                    "year": 2020,
                    "rating": 8.5,
                    "category": "Action"
                },
                {
            
                    "id": 2,
                    "title": "Titanic",
                    "overview": "This movies is a love reality story",
                    "year": 1997,
                    "rating": 8.0,
                    "category": "Romance"
                
                },
                {
            
                    "id": 3,
                    "title": "Avatar",
                    "overview": "This movies is",
                    "year": 2009,
                    "rating": 8.5,
                    "category": "Robcom"
                }
            ]
        }
    }
