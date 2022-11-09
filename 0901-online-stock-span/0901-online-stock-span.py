class StockSpanner:
    
    # Monotonic Stack
    def __init__(self):
        self.stack = [(100001, 0)]
        self.day = 0
    def next(self, price: int) -> int:
        self.day += 1
        while price >= self.stack[-1][0]:
            self.stack.pop()
        self.stack.append((price, self.day))
        sallest = self.stack[-1]
        second_smallest = self.stack[-2]
        return self.stack[-1][1] - self.stack[-2][1]
        #third_smallest = self.stack[-3]
        #span = sallest[1] - self.stack[-3][1]\
        #if sallest[0] == second_smallest[0] else sallest[1] - second_smallest[1]
        #print(self.stack)
        #return span
    
    #def __init__(self):
    #    self.prices = []
    #    self.count = 1
    #    self.max, self.min = 0, 100001
    #def next(self, price: int) -> int:
    #    self.prices.append(price)
    #    len_prices = len(self.prices)
    #    if len_prices == 1:
    #        self.max, self.min = price, price
    #        return self.count
    #    
    #    if price >= self.max:
    #        self.max = price
    #        self.count = len_prices
    #        return self.count
    #    elif price < self.min:
    #        self.min = price
    #        self.count = 1
    #        return self.count
    #    
    #    if price == self.prices[-2]:
    #        self.count += 1
    #        return self.count
    #    else:
    #        i = len_prices-2
    #        self.count = 1
    #        while i >= 0 and self.prices[i] <= price:
    #            self.count += 1
    #            i -= 1
    #        return self.count

#

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)