from __future__ import annotations

from dataclasses import dataclass

from govdash.geo.exceptions import InvalidGeography
from govdash.geo.typings import CATALOGUE, GeographyLevel


@dataclass
class GeoLocation:

    name: str

    def __post_init__(self) -> None:
        pass

    @property
    def level(self) -> GeographyLevel:
        for entry, areas in CATALOGUE.items():
            if self.name in areas:
                return entry

        raise InvalidGeography(f"Unknown geography name {self.name}")

    def to(self) -> GeoLocation:
        pass

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"[{self.level.name}] {self.name}"
