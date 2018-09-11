#!/usr/bin/env python3
import subprocess
import sys

result=subprocess.check_output(['./hello.py'])

result2=result.decode("utf-8")

expected = "Hello\n"

# testing code
if result2 == expected:
    print("Test OK")
    sys.exit (0)
else:
    sys.exit (1)
