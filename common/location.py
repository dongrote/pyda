class Location(object):
    address = 0x0 # address in the loaded memory image
    name = '' # name given to this location
    represents = None # what this location represents(function, dword, etc.)
    xrefs = [] # list of xrefs from this location
    value = None # what, if any, value this location has

    def __init__(self):
        pass

