# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 09:21:59
'''

from profier import Profier
from algorithms import selectSort

p = Profier()
p.test(selectSort, size=100)
