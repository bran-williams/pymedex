import os


def sys_url(url):
    """
    Formates a URL to the systems preferred. Also resolves the '~' token.
    :param url: The URL to modify.
    :return: The modified URL.
    """
    return os.path.expanduser(os.path.normcase(url))
