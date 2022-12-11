# Written by chat gpt (gpt3)
## Read the input data
#n, s = map(int, input().split())
#
## Compute the value of x
#x = s // n
#
## Print the value of x
#print(x)

# Improved by neomind
import sys

for line in sys.stdin.readlines():
    n, s = map(int, line.split())

    # Compute the value of x
    x = s // (n+1)

    # Print the value of x
    print(x)
