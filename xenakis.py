#!/usr/bin/python3

import hmac, hashlib
import time, bson
from collections import OrderedDict

class InvalidSignature(Exception):
    pass

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
    tmp = OrderedDict(sorted(tmp.items()))
    mac = tmp.pop("mac")
    bdata = bson.dumps(tmp)
    h = hmac.new(get_secret(), bdata, hashlib.sha256 ).hexdigest()
    if(h != mac): raise InvalidSignature("Signature did not match.")
    return bson.loads(data)

if __name__ == "__main__":
    info = get_info()
    a = pack(info)
    b = unpack(a)
    print("Binary:", a)
    print("Plain:",b)
