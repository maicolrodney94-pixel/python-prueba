from dataclasses import dataclass, field
from uuid import UUID,uuid4
@dataclass
class User:
    fname: str
    lname: str
    age: int
    email: str 
    uuid: uuid =field(default_factory=uuid4)
    