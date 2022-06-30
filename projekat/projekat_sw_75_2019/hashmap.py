class HashMap(object):
    def __init__(self, capacity):
        self._data = capacity * [None]
        self._capacity = capacity
        self._size = 0

    @staticmethod
    def _hash(value):
        hashed_value = value % 64
        return hashed_value

    def add(self, key, value):
        hashed_key = self._hash(key)
        self._data[hashed_key] = value

    def replace(self, key1, key2):
        hashed_key_one = self._hash(key1)
        hashed_key_two = self._hash(key2)
        self._data[hashed_key_one], self._data[hashed_key_two] = self._data[hashed_key_two], self._data[hashed_key_one]

    def __len__(self):
        return self._capacity

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        hashed_key = self._hash(key)
        self._data[hashed_key] = value