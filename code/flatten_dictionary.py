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

# O(n) time, where n is the number of keys in the input dictionary
# O(n) space
def flatten_dictionary(nested_dict):
  flat_dict = {}
  flat_dict_recurse(nested_dict, flat_dict)
  return flat_dict

def flat_dict_recurse(nested_dict, flat_dict, path=""):
  for key, value in nested_dict.items():
    include_dot = 1 if path and key else 0
    updated_path = path + "." * include_dot + key
    if not isinstance(value, dict):
      flat_dict[updated_path] = value
    else:
      flat_dict_recurse(value, flat_dict, updated_path)


# Another way of solving the problem
def flatten_dictionary(nested_dict):
  if not isinstance(nested_dict, dict):
    return {"": nested_dict}
  
  flat_dict = {}
  
  for key, value in nested_dict.items():
    flat_items = flatten_dictionary(value)
    for key_of_flat_item, value_of_flat_item in flat_items.items():
      add_dot = 1 if key and key_of_flat_item else 0
      concat_key_of_flat_item = key + ("." * add_dot) + key_of_flat_item
      flat_dict[concat_key_of_flat_item] = value_of_flat_item
    
  return flat_dict
