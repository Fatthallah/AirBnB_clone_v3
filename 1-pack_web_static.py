#!/usr/bin/python3
"""
    The Comment I have to write
"""
from fabric.api import local
from datetime import datetime



def do_pack():
    """
        The Comment I have to write
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None
