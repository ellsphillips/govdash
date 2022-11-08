from dataclasses import dataclass


@dataclass
class InvalidGeography(Exception):
    """
    Exception to raise when provided an invalid geographic property.
    """

    message: str

    def __str__(self) -> str:
        return self.message
