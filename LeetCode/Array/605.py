class Solution:
    def canPlaceFlowers_error(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # 应用了 or 的功能，就不必要将i==first 与 i== last独立出来
        count = 0
        for i in range(len(flowerbed)):
            if ((flowerbed[i] == 0)  # 判断本地是否为零
                and (i == 0 or flowerbed[i-1] == 0)  # 判断前面是否为零
                    and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):  # 满足三个条件才种植
                count += 1
                flowerbed[i] = 1
        return True if count >= n else False

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0,0)
        flowerbed.append(0)
        count = 0
        for f in flowerbed:
            if f == 0:
                count += 1
            if f == 1:
                count = 0
            if count == 3:
                n -= 1
                count = 1 # 有了1以后只需要间隔两颗就可以
            if n == 0:
                return True
        return False
