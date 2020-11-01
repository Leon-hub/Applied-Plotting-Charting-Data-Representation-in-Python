#!/usr/bin/env python3
import os, stat
import sys

filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename,'w') as f:
        f.write("#!/usr/bin/env python3\n")
    os.chmod(os.path.abspath(filename),stat.S_IRWXU)
else:
    print('Error, the file {} already exist!'.format(filename))
    sys.exit(1)