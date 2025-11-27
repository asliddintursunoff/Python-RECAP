from pydantic import BaseModel,field_serializer,Field
from datetime import datetime

class Rounder(BaseModel):
    number:float|None = None
    date : datetime = Field(default_factory=lambda:datetime.now())
    @field_serializer('number')
    def serialize_float(self,value):
        return round(value,2)
    
    @field_serializer('date',when_used="json-unless-none")
    def serialize_date(self,val:datetime):
        return val.strftime("%d/%m/%Y")
    




data = f'''{{
    "number": "123",
    "date": "{datetime.now().isoformat()}"
}}'''

print(data)
a = Rounder.model_validate_json(data)

print(a.model_dump_json())

r1 = Rounder(number=1/3)
print(r1.model_dump_json())
 