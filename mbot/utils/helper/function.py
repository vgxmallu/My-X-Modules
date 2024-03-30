import base64
import os
import random
import string
import time

import matplotlib

def random_string(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
