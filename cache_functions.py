import json as JSON
from json import JSONEncoder
import numpy as np

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
        
def open_cache():
    ''' opens the cache file if it exists and loads the JSON into
    the FIB_CACHE dictionary.

    if the cache file doesn't exist, creates a new cache dictionary
    
    Parameters
    ----------
    None

    Returns
    -------
    The opened cache
    '''
    try:
        cache_file = open('cache.json', 'r')
        cache_contents = cache_file.read()
        cache_dict = JSON.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict

def save_cache(cache_dict):
    ''' saves the current state of the cache to disk
    Parameters
    ----------
    cache_dict: dict
        The dictionary to save
    Returns
    -------
    None
    '''
    dumped_json_cache = JSON.dumps(cache_dict, cls=NumpyArrayEncoder)
    fw = open('cache.json',"w")
    fw.write(dumped_json_cache)
    fw.close()