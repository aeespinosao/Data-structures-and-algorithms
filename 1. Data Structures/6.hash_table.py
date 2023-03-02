class HashTable:
    
    def __init__(self, size: int = 7) -> None:
        self.data_map = [None] * size
        
    def __hash(self, key) -> int:
        hash = 0
        
        for letter in key:
            hash = (hash + ord(letter) * 23) % len(self.data_map)
        
        return hash
    
    def print_table(self):
        
        for i, element in enumerate(self.data_map):
            print(f"{i}: {element}")
            
    def set_item(self, key, value):
        index = self.__hash(key)
        
        if self.data_map[index] == None:
            self.data_map[index] = []
            
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        
        if self.data_map[index]:
            for value in self.data_map[index]:
                if value[0] == key:
                    return value[1]
        
        return None
    
    def keys(self):
        all_keys = []
        
        for index in self.data_map:
            if index:
                for element in index:
                    all_keys.append(element[0])
                
        return all_keys