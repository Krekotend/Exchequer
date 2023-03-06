from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass()
class PsQL:
    host: str
    user: str
    password: str
    db_name: str


@dataclass
class Config:
    tg_bot: TgBot
    db: PsQL


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')),
                  db=PsQL(host=env('HOST'),
                          user=env('USER'),
                          password=env('PASSWORD'),
                          db_name=env('DB_NAME')))
