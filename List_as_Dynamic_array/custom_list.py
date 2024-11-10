import ctypes
class CustomList:
    def __init__(self):
        initial_capacity = 1
        self.capacity = initial_capacity
        self.size = 0
        self.array = self.__create_array(self.capacity)
    
    def __create_array(self, capacity):
        #Create a new array with given capacity
        return (ctypes.py_object * capacity)()
    
    def __resize(self, new_capacity):
        new_array = self.__create_array(new_capacity)
        
    def append(self, item):
        if self.size == self.capacity:
            self.__resize(2*self.capacity)