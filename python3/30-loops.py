#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
print("\n".join([str(n)+" x "+str(i)+" = "+str(n*i) for i in range(1,11)]))
