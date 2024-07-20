from dataclasses import dataclass
from environs import Env


@dataclass
class Api_weather:
    token: str


@dataclass
class Config:
    api_w: Api_weather

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(api_w=Api_weather(token=env('TOKEN')))