from pydantic import BaseModel,Field
from datetime import date
from pprint import pprint
class Place(BaseModel):
    country :str
    city:str
class Born(BaseModel):
    born:Place
    dt:date = Field(alias='date')

class Person(BaseModel):
    first_name :str = Field(alias="firstName")
    last_name:str = Field(alias='lastName')
    born:Born|None = Field(default=None)


data = """{
    "firstName": "Asliddin",
    "lastName": "Tursunov",
    "born": {
        "born": {
            "country": "Uzbekistan",
            "city": "Tashkent"
        },
        "date": "2001-01-01"
    }
}
"""

p = Person.model_validate_json(data)
# print(p)
print(Person.model_dump_json(p,by_alias=True))