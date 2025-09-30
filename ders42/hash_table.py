class HashTable:
    def __init__(self,size=7):
        self.data_map = [None] * size

    # sifreleme metodum
    def __hash(self,key): # pens --> 2
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) *24) % len(self.data_map)
        print(my_hash)
        return my_hash
    
    # item eklemek
    def set_item(self,key,value): # pens:1000
        index = self.__hash(key)

        # eger daha once eleman yok ise veya bos ise
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self.__hash(key)


    def print_table(self):
        # for key,value in enumerate(self.data_map):
        #     print(key,':',value)
        print(self.data_map)


hash_table = HashTable()
hash_table.set_item('pens',1000)
hash_table.set_item('markers',300)
hash_table.set_item('notebooks',12)
hash_table.set_item('books',7)
hash_table.set_item('pencils',238)

hash_table.get_item('pencils') # 238 almayi bekliyorum 
hash_table.print_table()