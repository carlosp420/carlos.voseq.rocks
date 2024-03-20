import os

import environ

from .base import *  # noqa

DEBUG = False
env = environ.Env()
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["carlos.voseq.rocks"]
