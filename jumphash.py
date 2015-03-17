#!/usr/bin/env python
import numpy as np
import sys
import ctypes

def hash(key, buckets):
    if np.int32(buckets) <= 0:
        buckets = 1
    b = np.int64(-1)
    j = 0
    while j < buckets:
        b = j
        key = ctypes.c_uint64(key * 2862933555777941757 + 1).value
        j = np.int64(np.double(b + 1) * (2147483648.0 / ctypes.c_double((key >> 33) + 1).value))
    return b

def main(argv = None):
    if argv is None:
        argv = sys.argv[1:]
    try:
        key = int(argv[0])
        buckets = int(argv[1])
        result = hash(key, buckets)
        print "%s" % result
    except:
        return 1

if __name__ == "__main__":
    sys.exit(main())
