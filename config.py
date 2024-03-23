import os
import time
from os import environ

#MOMGO DATABASE
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")
