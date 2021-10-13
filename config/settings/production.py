from pathlib import Path
import os

DEBUG = False

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['0.0.0.0', 'production']


