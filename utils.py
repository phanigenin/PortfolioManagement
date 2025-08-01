def get_os_name():
    import platform
    return platform.system().upper()

def is_windows():
    return True if get_os_name()=='WINDOWS' else False