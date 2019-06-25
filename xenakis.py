import hmac, hashlib
import time, bson
from collections import OrderedDict

def get_secret():
    # get some secret key, stored somewhere
    return b'932847-9304-049234-32024-320948'

def get_info():
    return {
        "bid" : 728,
        "dtm" : int(time.time()),   
        "lid" : 12,
        "lat" : 37.4224764,
        "lng" : -122.0842499,
        "vid" : 56,
        "vsn" : "A9483324",
    }

def pack(data):
    data = OrderedDict(sorted(data.items()))
    bdata = bson.dumps(data)
    h = hmac.new(get_secret(), bdata, hashlib.sha256 )
    data["mac"] = h.hexdigest()
    bdata = bson.dumps(data)
    return bdata

def unpack(data):
    tmp = bson.loads(data)
    mac = tmp.pop("mac")
    bdata = bson.dumps(tmp)
    h = hmac.new(SECRET_KEY, bdata, hashlib.sha256 ).hexdigest()
    if(h != mac): raise Exception("Security Error!")
    return bson.loads(data)

if __name__ == "__main__":
    info = get_validation_info()
    a = pack_data(info)
    b = unpack_data(a)
    print(a)
    print(b)