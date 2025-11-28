'''
Docstring for Pydantic.model_validator
Sometimes validation depends on multiple fields together.

Runs after all fields are validated individually.

Useful when two fields rely on each other.
'''
from pydantic import BaseModel,model_validator
class Register(BaseModel):
    password :str
    confirm:str

    @model_validator(mode="after")
    def password_confirmation(self):
        if self.password != self.confirm:
            raise ValueError("Password do not match!")
        return self
    

p1 = Register(password="HelloWorld",confirm="HelloWorld")
print(p1)
