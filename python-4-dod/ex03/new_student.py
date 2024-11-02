from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: int = 0  # Default value
    login: str = field(init=False)  # Mark as not initializable
    id: str = field(init=False)  # Mark as not initializable

    def __post_init__(self):
        self.id = generate_id()
        self.login_generator()

    def login_generator(self) -> None:
        # Using self to access instance attributes
        self.login = self.name[:1] + self.surname[1:]
