#!/bin/python3

import math
import os
import random
import re
import sys



def wierd(n):
    if n % 2 == 1 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')


wierd(int(input()))