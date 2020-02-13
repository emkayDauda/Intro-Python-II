# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc, key):
        self.name = name
        self.desc = desc
        self.key = key
        self.d_to = {}
        self.s_to = {}
        self.a_to = {}
        self.w_to = {}
