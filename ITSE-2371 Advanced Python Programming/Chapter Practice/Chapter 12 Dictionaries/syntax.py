"""
Basic examples of syntax and instantiation of dictionaries

Author: Samuel Garza
"""

# Code for creating dictionaries
# The syntax for creating a dictionary --> dictionary_name = {key1:value1, key2:value2 ...}
# Strings and keys and values
countries = {"CA": "Canada",
             "US": "United States",
             "GB": "Great Britian",
             "MX": "Mexico"}

# Numbers as keys, strings as values
numbers = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

# An empty dictionary 
book_catalog = {}
""" 
• Unlike a list, which is an ordered collection of items, a dictionary is an unordered 
  collection of items. As a result, there’s no guarantee that the items in a dictionary 
  remain in the same order.
• In a dictionary, each item consists of a key/value pair where each value in the 
  dictionary is indexed by a unique key.
• The key can be any immutable data type, but it’s usually a string. 
• The value that corresponds to a key can be a simple data type such as number or a 
  string. Or, it can be a complex data type such as a list or another dictionary.
• Whitespace is ignored between dictionary items. As a result, you can use 
  whitespace to format a dictionary so the code is easier to read.
• In some languages, dictionaries are called associative arrays. 
"""



# Code for accessing a value
# The syntax for accessing a value --> dictionary_name[key]
country = countries["MX"]                                               # "Mexico"
country = countries["IE"]                                               # KeyError: Key doesn't exist

# Code that sets a value if the key is in the dictionary
countries["GB"] = "United Kingdom"

# Code that adds a key/value if the key isn't in the dictionary 
countries["FR"] = "France"

# Code for checking if a key is in a dictionary 
# Syntax for checking if key is in a dictionary --> key in dictionary 
code ="IE"
if code in countries:
    country = countries[code]
    print(country)
else:
    print(f"There is no country for this code: {code}")
    
# Code that uses the get() method to access an item
# Syntax for get() method --> get(key, defaultValue)
country = countries.get("MX")                                           # "Mexico"
country = countries.get("IE")                                           # "None"
country = countries.get("IE", "Unknown")                                # "Unknown"
"""
• Attempting to get a value for a key that isn’t in the dictionary causes a KeyError. 
• If you set a value for an existing key, Python updates the old value with the new value.
• If you set a value for a key that doesn’t exist, Python adds a new key/value pair to the dictionary.
• To prevent a KeyError from occurring, you can use the get() method of a dictionary.
"""



# Code that deletes items from a dictionary
# Syntax for deleting an item --> del dictionary_name[key]
del countries["MX"]
del countries["IE"]                                                     # KeyError: Key doesn't exist

# Code that checks if a key is in a dictionary before deleting the item
code = "IE"
if code in countries:
    country = countries[code]
    del countries[code]
    print(f"{country} was deleted.")
else:
    print(f"There is no country for this code: {code}")

# Code that uses the pop() method for deleting an item
# Syntax for pop() method --> pop(key, default value)
country = countries.pop("US")                                            # "United States"
country = countries.pop("IE")                                            # KeyError: Key doesn't exist
country = countries.pop("IE", "Unknown")                                 # "Unknown"

# Code that uses the pop() method to prevent a KeyError from occuring
code = "IE"
country = countries.pop(code, "Nothing")
print(f"{country} was deleted.")

# Code that uses the clear() method to delete all items
countries.clear()
"""
• You can use the del keyword or the pop() and clear() methods to delete items from a dictionary.
"""



# Code for looping through dictionaries using keys(), items(), and values() methods
# Code for using keys() method to loop through all keys and values
for code in countries.keys():
    print(f"{code}    {countries[code]}")
    
# Another way to get the same result since the default iterator contains keys
for code in countries:
    print(f"{code}      {countries[code]}")
    
# Code that unpacks a tuple as it loops through all keys and values
for code, name in countries.items():
    print(f"{code}     {name}")
    
# Code that loops through all values
for name in countries.values():
    print(name)
"""
• These methods return a view object. Since a view object is an iterator, you can iterate through 
  its contents with a for loop.
• You can use tuple unpacking to loop through the key/value pairs in the view object. 
• If a dictionary is updated, the corresponding keys or values in the view object are also updated. 
  If you don’t want these automatic updates, you can use the built-in list() constructor to convert the 
  view object to a list as shown in the next figure.
"""



# Code for converting between lists and dictionaries
# Syntax for converting a dictionary to a list --> list(view_object)
# Syntax for converting a list to a dictionary --> dict(list)
# Code to convert the keys of a dictionary to a list and sorts them
codes = list(countries.keys())
codes.sort()
for code in codes:
    print(f"{code})     {countries[code]}")
    
# Code that converts a two-dimensional list to a dictionary
countries = [["GB," "United Kingdom"],
             ["NL", "Netherlands"],
             ["DE", "Germany"]]
countries = dict(countries)
print(countries)
"""
• You can use two built-in constructors to convert between dictionaries and lists.
"""