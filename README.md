# pyjumphash, a consistent hashing libarary implemnting the fast Jump Hash algorithm for python

## Introduction
Jump Hash is a fast, minimal memory consistent hash algorithm that can
be expressed in a fairly compact code base.  As such it is well suited
to rapid-iteration hashing requirements.  This implementation makes use
of ctypes and numpy to mimic the behavior of integers in the original C
implementation.  It is based off the work described here:
http://arxiv.org/pdf/1406.2294v1.pdf

It's also a short project in conversion and is stated to be in no way
suitable for production use.  Currently supports Python 2.6 and Python 2.7

## Installation

* install numpy
python setup.py build
sudo python setup.py install

## Documentation


## Example
Here is the most simple example of use, sending a message with the BlockingConnection adapter:

    import jumphash
    # h_id is an integer representation of the id to consistent-hash
    h_id = 43838
    buckets = 64
    bucket_assignment = jumphash.hash(h_id, buckets)

## License
pyjumphash is licensed under the Apache 2.0 license.
