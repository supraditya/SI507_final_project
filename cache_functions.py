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

def is_entry_in_cache(cache_dict, entry_to_be_added):
    '''
    Function checkes whether an entry is already present within the cache

    PARAMETERS
    ==============================
    cache_dict: dict
    A dictionary containing the application cache, as passed by the calling function

    entry_to_be_added: dict, list
    A value which needs to be searched for within the application cache

    RETURNS
    =============================
    boolean
    True if entry is found
    False otherwise


    '''
    if entry_to_be_added not in cache_dict.items():
        return False
    return True