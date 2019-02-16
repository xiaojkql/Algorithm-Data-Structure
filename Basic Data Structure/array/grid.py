# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 10:52:36
'''

from array_ import Array


class Grid:
    def __init__(self, rows, cols, fillValue=None):
        self._rows = rows
        self._cols = cols
        self._fillValue = fillValue
        self._data = Array(self._rows)
        for i in range(self._rows):
            self._data[i] = Array(cols, fillValue=self._fillValue)

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        result = ""
        for i in range(self._rows):
            for j in range(self._cols):
                result += self._data[i][j] + " "
            result += "\n"
        return result


if __name__ == "__main__":
    grid = Grid(4, 5, 100)
    print(grid[1][1])
