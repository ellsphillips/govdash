from enum import Enum

from . import data


class GeographyLevel(Enum):
    NATIONAL = "national"
    REGIONAL = "regional"
    LAD = "lad"
    LTLA = "ltla"
    UTLA = "utla"
    MSOA = "msoa"
    LSOA = "lsoa"


CATALOGUE: dict[GeographyLevel, list[str]] = {
    GeographyLevel.NATIONAL: data.NATIONS,
    GeographyLevel.REGIONAL: data.REGIONS,
    GeographyLevel.LAD: data.LOCAL_AUTHORITY_DISTRICTS,
    GeographyLevel.LTLA: data.LOWER_TIER_LOCAL_AUTHORITIES,
    GeographyLevel.UTLA: data.UPPER_TIER_LOCAL_AUTHORITIES,
    GeographyLevel.MSOA: data.MIDDLE_SUPER_OUTPUT_AREAS,
    GeographyLevel.LSOA: data.LOWER_SUPER_OUTPUT_AREAS,
}
