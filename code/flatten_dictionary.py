"""
Flatten a Dictionary

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it.
If a certain key is empty, it should be excluded from the output (see e in the example below).


input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
        
"""        

def flatten_dictionary(nested_dict):
  flat_dict = {} 
  flat_dict_recurse(nested_dict, flat_dict)
  return flat_dict

def flat_dict_recurse(nested_dict, flat_dict, key_path=""):
  for key, value in nested_dict.items():
    include_dot = 1 if key_path and key else 0
    # Case 1: not a nested dict, so we can add item to final output 
    if not isinstance(value, dict):
        flat_dict[key_path + ("." * include_dot) + key] = value
    # Case 2: nested dict, we recurse
    else:
        flat_dict_recurse(value, flat_dict, key_path + ("." * include_dot) + key)  
