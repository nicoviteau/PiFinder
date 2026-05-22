# config_display.py
# Configuration file to choose local display, remote display or both

# Constants representing the available display modes

DISPLAY_MODE_LOCAL = "local"
DISPLAY_MODE_REMOTE = "remote"
DISPLAY_MODE_MIRROR = "mirror"  # Display is duplicated both locally and remotely (mirror mode)

# Active display mode
# LOCAL is chosen as the default (compaibility with "standard" PiFinder)
DISPLAY_MODE = DISPLAY_MODE_LOCAL
