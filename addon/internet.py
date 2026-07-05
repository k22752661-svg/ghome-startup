import xbmc

def is_online():
    return xbmc.getCondVisibility("System.HasNetwork")
