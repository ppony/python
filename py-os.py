import binascii
import pdb
import os
import re


fn = os.path.join(os.path.dirname(__file__), 'ti')
fn1 = os.path.join(os.path.dirname(__file__), '..')
fn2 = os.path.join(os.path.dirname(__file__), 'Tracing')

print(os.path.dirname(__file__))
print(fn)
print(os.getcwd())
os.chdir(fn)
print(os.getcwd())
os.chdir(fn1)
print(os.getcwd())
os.chdir(fn2)
print(os.getcwd())
