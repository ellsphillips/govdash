from __future__ import annotations

from typing import cast

RGBValue = tuple[int, int, int]


def hex_to_rgb(hex_value: str) -> RGBValue:
    alnum = hex_value.strip("#")
    channels = tuple(int(alnum[i : i + 2], 16) for i in range(1, 6, 2))
    return cast(RGBValue, channels)


def rgb_to_hex(rgb_value: RGBValue) -> str:
    return "#" + "".join([f"{v:x}".ljust(2, "0") for v in rgb_value])
