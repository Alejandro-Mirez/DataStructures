class Map:

    def __init__(self, my_map = {}):
        self.my_map = my_map

    def set(self, key, value):
        return self.my_map.setdefault(key, value)

    def get(self, key):
        return self.my_map.get(key)

    def keys(self):
        keys_list = list(self.my_map.keys())
        return keys_list

    def display_values(self):
        values_list = list(self.my_map.values())
        return values_list