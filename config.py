import os
import time
from os import environ

#MOMGO_DATABASE
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")

#LOGS_CHANNEL
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))

#AUTHENTICATED_USERS
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
