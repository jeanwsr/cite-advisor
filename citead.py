import sys
sys.path.append('.')
from wfn import *

if '__main__' == __name__:

    method_req = sys.argv[1]

    for k,v in WFNLIT.items():
        if method_req in k:
            print(k,v)

