import json
import

_BASE_DIR = 'db'

def _path(p):
    return os.path.join(_BASE_DIR, p)

def load(key):
    with open(_path(key), 'r') as f:
        return json.load(f)

def load_default(key, default):
    try:
        return load(key)
    except OSError:
        return default

def modify(key, function):
    save(key, function(load(key)))

def save(key, value):
    with open(_path(key), 'w') as f:
        json.dump(value, f)

def delete(key):
    try:
        os.remove(_path(key))
    except OSError:
        pass
