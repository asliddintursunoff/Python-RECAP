'''
Docstring for Pydantic.strictTypes

Pydantic has special types for real-world data.

from pydantic import BaseModel, EmailStr, HttpUrl

class Contact(BaseModel):
    email: EmailStr
    website: HttpUrl
Input
Contact(email="test@gmail.com", website="https://google.com")

Invalid Example:
Contact(email="not_email", website="hello")


!Raises error automatically! You don’t need custom validator.

🔐 Strict Types (force exact type)

Use when you want 0 → error, not “convert automatically”.

from pydantic import BaseModel, StrictStr, StrictInt

class User(BaseModel):
    name: StrictStr
    age: StrictInt

📌 Example Behavior
User(name=123)   # ❌ error (not auto converted)
User(age="12")   # ❌ error (must be int)
'''