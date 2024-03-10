#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(5, None))
try:
    print(add_integer(None, None))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

