# python3_kadai

import so
import sys
MAX = 2
print(sys.getdefaultencoding())
print(so.path.basename(so.getcwd()))
for i in range(3):
    print(i, end=" ")
    if MAX > i:
        print(MAX)
    else:
        print ("#")
