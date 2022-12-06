def get_val(collection=None, key=None, default=None) -> str:
    collection = dict(collection)
    
    if key in collection.keys():
        return print(collection[key])
    
    elif key not in collection.keys():
        return print(default)
    
    
get_val({}, "hello","python")
    