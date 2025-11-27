from pydantic import BaseModel
from typing import Union,Optional
class Person(BaseModel):
    first_name:Union[str,None] = None
    middle_name:Optional[str] = None
    last_name:str | None = None
    age:int = 0

dict_data = """{
    "first_name":"Asliddin",
    "last_name":"Tursunov",
    "age":"32"
}"""

print(Person.model_validate_json(dict_data))
Person()