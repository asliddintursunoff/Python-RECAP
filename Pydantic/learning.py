'''
Docstring for Pydantic.learning
Serializer - is for converting data one type to another
    Pydantic model -> json
    Pydantic model -> dict
    dict -> Pydantic model
    json -> Pydantic model 

Validators is for validading data(checking every data member or whole class that to be true)
Forexample: 
    you should take interger higher than 0 -> so you should need to write validator for checking value>0
'''

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