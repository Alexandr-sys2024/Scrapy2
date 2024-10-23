# -*- coding: utf-8 -*-
import sys
import codecs
from os import path

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Просто выводим путь
print(path.abspath('.'))