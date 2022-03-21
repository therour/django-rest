import os
import dotenv
from split_settings.tools import optional, include


dotenv.load_dotenv()

ENV = os.getenv("APP_ENV", "development")

_base_settings = [
    "base.py",
    optional("{0}.py".format(ENV)),
]

include(*_base_settings)
