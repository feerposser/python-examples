
import sys

for num, value in enumerate(sys.argv):
    print(num, "-", value)

print("-"*20)

for arg in range(1, len(sys.argv)):
    print(sys.argv[arg])