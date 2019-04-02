import os


def sys_url(url):
    return os.path.expanduser(os.path.normpath(url))
