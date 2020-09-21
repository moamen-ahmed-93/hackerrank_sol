#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

print("\n".join(k+" "+str(v) for k,v in Counter(sorted(input())).most_common(3)))




