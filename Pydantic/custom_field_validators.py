'''
Docstring for Pydantic.custom_field_validators
Fields Validator is for validating each field not whole class
it can be before and after pydantic validation itself

changing mode is like this:
    @field_validator("property_name",mode= "after or before")

before is used for data seperation (1 example):
    we should take age as int but api sends it like 22 year so we should split and take int
'''
from pydantic import BaseModel,field_validator

class Model(BaseModel):
    number:int
    lst:list[int] = []

    @field_validator("number")
    @classmethod
    def number_greater(cls,value):
        if value<0:
            raise ValueError("Value cannot be less than 0")
        return value
    
    @field_validator("lst")
    @classmethod
    def validating_unique_list(cls,value):
        if len(set(value)) != len(value):
            raise ValueError("List must contain unique values")
        return value
    
try:
    p1 = Model(number=12,lst=[11,2,4,23])
    print(p1)
except Exception as e:
    print(e)
