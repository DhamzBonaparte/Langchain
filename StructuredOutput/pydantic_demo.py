from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Person(BaseModel):
    name: str = "Sulav"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(
        gt=0,
        lt=10,
        default=5,
        description="A decimal value repesenting the cgpa of the student",
    )


# Me = Person(name=44)  # invalid
# Me = Person(name="Sulav") #valid
Me = Person(age="33", email="abc@hgj.c")
dict_stu = dict(Me)
json_stu = Me.model_dump_json()

print(dict_stu["email"])
