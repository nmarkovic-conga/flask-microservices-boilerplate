import os
import re
from flask import config
from dotenv import load_dotenv

load_dotenv()
class BaseConfig:
    CACHE_TYPE = os.getenv('CACHE_TYPE')
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL')
    SECRET_KEY = os.getenv('SECRET_KEY') if os.getenv('SECRET_KEY') else None
    

config = BaseConfig 