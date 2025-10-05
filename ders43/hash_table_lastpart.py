class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    # Hash function
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 24) % len(self.data_map)
        return my_hash

    # Add an item
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # Retrieve an item
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Print table nicely
    def print_table(self):
        for i, bucket in enumerate(self.data_map):
            print(f"Index {i}: ", end="")
            if bucket is None:
                print("Empty")
            else:
                for key, value in bucket:
                    print(f"({key}: {value})", end=" ")
                print()  # new line for each bucket

    # Get all keys
    def keys(self):
        all_keys = []
        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_keys.append(pair[0])
        return all_keys

    # Get all values
    def values(self):
        all_values = []
        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_values.append(pair[1])
        return all_values

    # Get all key-value pairs
    def items(self):
        all_items = []
        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_items.append((pair[0], pair[1]))
        return all_items


# ----------------- Test -----------------
hash_table = HashTable()
hash_table.set_item('pens', 1000)
hash_table.set_item('markers', 300)
hash_table.set_item('notebooks', 12)
hash_table.set_item('books', 7)
hash_table.set_item('pencils', 238)

print("Get item 'pencils':", hash_table.get_item('pencils'))  # 238
print("\nHash Table:")
hash_table.print_table()

print("\nKeys:", hash_table.keys())
print("Values:", hash_table.values())
print("Items:", hash_table.items())