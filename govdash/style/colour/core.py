from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional, cast

import colorir

RGBValue = tuple[int, int, int]


def hex_to_rgb(hex_value: str) -> RGBValue:
    alnum = hex_value.strip("#")
    channels = tuple(int(alnum[i : i + 2], 16) for i in range(1, 6, 2))
    return cast(RGBValue, channels)


def rgb_to_hex(rgb_value: RGBValue) -> str:
    return "#" + "".join([f"{v:x}".ljust(2, "0") for v in rgb_value])


@dataclass
class Gradient:

    colours: Iterable[str]
    steps: Optional[int] = None

    def __post_init__(self) -> None:
        grad = colorir.Grad(colors=self.colours)
        self.__values: list[str] = grad.n_colors(self.steps)

    @property
    def values(self) -> list[str]:
        return self.__values
