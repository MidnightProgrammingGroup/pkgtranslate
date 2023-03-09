import os
confpath = os.getenv("HOME") + ".config/pkgtranslate.yml"

# Check if config file exists
def __init__():
    if not os.path.exists(confpath):
        os.popen("mkdir" + os.getenv("HOME") + "/.config")
        open(confpath, "w").close()


def get_value(key):
    with open(confpath, "r") as conf:
        for ln in conf.readlines():
            if key + ": " in ln:
                return ln[ln.find(": ") + 1:]