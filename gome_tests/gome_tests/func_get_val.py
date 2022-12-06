def get_val(collection, key, default=None) -> str:
    collection = dict(collection)
    
    if key in collection.keys():
        return collection[key]
    
    elif key not in collection.keys():
        return default
    

get_val({"hello": "world"}, "hello")
get_val({"hello": "world"}, "hello", "python")
get_val({}, "hello","python")
    
