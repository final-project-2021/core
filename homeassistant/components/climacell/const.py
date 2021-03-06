"""Constants for the ClimaCell integration."""

from homeassistant.components.weather import (
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
)

CONF_TIMESTEP = "timestep"

DAILY = "daily"
HOURLY = "hourly"
NOWCAST = "nowcast"
FORECAST_TYPES = [DAILY, HOURLY, NOWCAST]

CURRENT = "current"
FORECASTS = "forecasts"

DEFAULT_NAME = "ClimaCell"
DEFAULT_TIMESTEP = 15
DEFAULT_FORECAST_TYPE = DAILY
DOMAIN = "climacell"
ATTRIBUTION = "Powered by ClimaCell"

MAX_REQUESTS_PER_DAY = 1000

CONDITIONS = {
    "freezing_rain_heavy": ATTR_CONDITION_SNOWY_RAINY,
    "freezing_rain": ATTR_CONDITION_SNOWY_RAINY,
    "freezing_rain_light": ATTR_CONDITION_SNOWY_RAINY,
    "freezing_drizzle": ATTR_CONDITION_SNOWY_RAINY,
    "ice_pellets_heavy": ATTR_CONDITION_HAIL,
    "ice_pellets": ATTR_CONDITION_HAIL,
    "ice_pellets_light": ATTR_CONDITION_HAIL,
    "snow_heavy": ATTR_CONDITION_SNOWY,
    "snow": ATTR_CONDITION_SNOWY,
    "snow_light": ATTR_CONDITION_SNOWY,
    "flurries": ATTR_CONDITION_SNOWY,
    "tstorm": ATTR_CONDITION_LIGHTNING,
    "rain_heavy": ATTR_CONDITION_POURING,
    "rain": ATTR_CONDITION_RAINY,
    "rain_light": ATTR_CONDITION_RAINY,
    "drizzle": ATTR_CONDITION_RAINY,
    "fog_light": ATTR_CONDITION_FOG,
    "fog": ATTR_CONDITION_FOG,
    "cloudy": ATTR_CONDITION_CLOUDY,
    "mostly_cloudy": ATTR_CONDITION_CLOUDY,
    "partly_cloudy": ATTR_CONDITION_PARTLYCLOUDY,
}

CLEAR_CONDITIONS = {"night": ATTR_CONDITION_CLEAR_NIGHT, "day": ATTR_CONDITION_SUNNY}

CC_ATTR_TIMESTAMP = "observation_time"
CC_ATTR_TEMPERATURE = "temp"
CC_ATTR_TEMPERATURE_HIGH = "max"
CC_ATTR_TEMPERATURE_LOW = "min"
CC_ATTR_PRESSURE = "baro_pressure"
CC_ATTR_HUMIDITY = "humidity"
CC_ATTR_WIND_SPEED = "wind_speed"
CC_ATTR_WIND_DIRECTION = "wind_direction"
CC_ATTR_OZONE = "o3"
CC_ATTR_CONDITION = "weather_code"
CC_ATTR_VISIBILITY = "visibility"
CC_ATTR_PRECIPITATION = "precipitation"
CC_ATTR_PRECIPITATION_DAILY = "precipitation_accumulation"
CC_ATTR_PRECIPITATION_PROBABILITY = "precipitation_probability"
CC_ATTR_PM_2_5 = "pm25"
CC_ATTR_PM_10 = "pm10"
CC_ATTR_CARBON_MONOXIDE = "co"
CC_ATTR_SULPHUR_DIOXIDE = "so2"
CC_ATTR_NITROGEN_DIOXIDE = "no2"
