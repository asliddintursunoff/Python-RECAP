'''
Docstring for Pydantic.Config

What it is

A dictionary inside your model:

model_config = { ... }


It changes default behavior of Pydantic models.

Similar to "preferences" for the model.
'''
# =============================
# 1. populate_by_name
# -----------------------------
# Accept both Python field names (snake_case)
# and aliases (camelCase) for input validation
# Example: API sends "firstName", Python field is "first_name"
# Useful when your frontend uses camelCase
# =============================

# =============================
# 2. ser_json_by_alias
# -----------------------------
# Output JSON using aliases instead of Python field names
# Ensures API responses match frontend expectations
# Example: {"firstName": "Ali"} instead of {"first_name": "Ali"}
# =============================

# =============================
# 3. extra
# -----------------------------
# Controls how unknown fields in input are handled
# Options:
#   "ignore"  -> default, extra fields are silently ignored
#   "forbid"  -> raises validation error if unknown fields exist
#   "allow"   -> keeps extra fields in the model
# Recommended: "forbid" for FastAPI request models (safer API)
# =============================

# =============================
# 4. validate_assignment
# -----------------------------
# Validates fields when updating them after model creation
# Example: user.age = "20" -> automatically validated/converted
# Useful when modifying model attributes in code
# =============================

# =============================
# 5. str_strip_whitespace
# -----------------------------
# Automatically trims whitespace from all string fields
# Example: "  Ali  " -> "Ali"
# Prevents accidental spaces in input
# =============================

# =============================
# 6. frozen
# -----------------------------
# Makes model immutable (like frozen dataclass)
# Any update attempt will raise an error
# Useful for config or constant objects
# =============================

# =============================
# 7. use_enum_values
# -----------------------------
# When using Enum fields, outputs the Enum value instead of Enum object
# Example: Status.ACTIVE -> "ACTIVE" in JSON response
# =============================

# =============================
# 8. json_encoders
# -----------------------------
# Custom serialization for types like datetime, Decimal, UUID, etc.
# Example: datetime -> "YYYY-MM-DD" format
# Ensures API returns proper JSON for non-standard types
# =============================

# =============================
# Recommended Config for FastAPI
# -----------------------------
# This covers most common use-cases
# =============================



from pydantic import BaseModel, Field

class User(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")

    model_config = {
        "populate_by_name": True,
        "extra": "forbid",
        "ser_json_by_alias": True
    }

# Input using alias
user = User(firstName="Ali", lastName="Tursunov")

# Input using python name (snake_case) works too
user2 = User(first_name="Omar", last_name="Karimov")

# Output JSON uses aliases automatically
print(user.model_dump_json())
