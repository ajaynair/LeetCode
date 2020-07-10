class HashTable:
    def __init__(self):
        self._hashtable: {str:str} = {}

    def get_val(self, key: str) -> str:
        if key not in self._hashtable.keys():
            return None

        return self._hashtable[key]

    def set_val(self, key: str, val: str) -> None:
        self._hashtable[key] = val