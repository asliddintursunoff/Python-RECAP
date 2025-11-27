from pydantic import BaseModel,Field

class Person(BaseModel):
    id :int = Field(alias="id")
    first_name : str|None  = Field(alias="First Name",default=None)
    last_name: str = Field(alias="LASTNAME")
    age: int = Field(alias="age in years")

data = {
    "id":12,
    "First Name":"Jhon",
    "LASTNAME":"Dwaysen",
    "age in years":12
}
p1 = Person.model_validate(data) #validating json
print(p1)
print(p1.model_dump_json(by_alias=True)) #json converting