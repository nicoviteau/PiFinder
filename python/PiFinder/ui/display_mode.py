
from .config_display import DISPLAY_MODE

def is_local():
    return DISPLAY_MODE == "local"

def is_remote():
    return DISPLAY_MODE == "remote"

def is_mirror():
    return DISPLAY_MODE == "mirror"
