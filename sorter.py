# making a python class for the whole work..
class DictionarySort:
    def __init__(self, dictionary:dict) -> None:
        '''Constructor. Takes a dictionary as its parameter to compile key and values to python string and to make accesible to other methods of this class.'''
        self.input:dict = {}
        for key, value in dictionary.items():# Storing all keys in key and all values in value variable.
            self.input[str(key)] = str(value)# make all keys and value python strings..

    def sortbykeys(self):
        '''The key method . It does the stuff of sorting through keys.'''
        sortedDict = sorted(self.input.items())# sorting the list form of the dictionary
        return dict(sortedDict)
    def KeyValueInterchanger(self):
        '''For interchanging keys and values. Example: {a:1}->{1:a}'''
        newdict = {}# a new dictionary as new result
        for key, value in  self.input.items():
            if value in newdict.keys():# whether the key is already available..
                newdict[value].append(key)# appending value with the previous ones.
            else:# whether the key is not present currently..
                newdict[value] = [key]# create new key with new value..
        return newdict
    def sortedbyvalues(self):
        '''Another key method . It does the stuff of sorting through values.'''
        newdict = self.KeyValueInterchanger()# calling "KeyValueInterchanger" method to get the interchanged dictionary!
        sortedDict = sorted(newdict.items())# sorting like the second method of this class!
        return dict(sortedDict)
        

# A dictionary with various types of key and value for our code test whether it is working or not
dictionary = {
    "a" : 100,
    "b" : 500,
    "f" : "lol",
    "c" : 10.4,
    "d" : "hello",
    "e" : '1',
    "f" : [1,2,3]
}

sorting = DictionarySort(dictionary) #instantiation
print(sorting.sortbykeys())# Output : {'a': '100', 'b': '500', 'c': '10.4', 'd': 'hello', 'e': '1', 'f': '[1, 2, 3]'}
print(sorting.sortedbyvalues())# Output : {'1': ['e'], '10.4': ['c'], '100': ['a'], '500': ['b'], '[1, 2, 3]': ['f'], 'hello': ['d']}
