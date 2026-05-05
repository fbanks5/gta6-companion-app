# Import Limiter from SlowAPI
# Limiter is responsible for tracking and enforcing request limits.
from slowapi import Limiter

# Import get_remote_address
# This tells SlowAPI to identify each client by their IP address.
from slowapi.util import get_remote_address

# Create one shared limiter instance for the whole application.
# We keep it in this separate file to avoid circular imports between main.py and route files.
limiter = Limiter(key_func=get_remote_address)