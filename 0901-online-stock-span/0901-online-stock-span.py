class StockSpanner:

    def __init__(self):
        self.prices = []
        self.count = 0
        self.max, self.min = 0, 100001
    def next(self, price: int) -> int:
        self.prices.append(price)
        if len(self.prices) == 1:
            self.max, self.min = price, price
            self.count = 1
            return self.count
        
        if price >= self.max:
            self.max = price
            self.count = len(self.prices)
            #print(price, self.max)
            return self.count
        elif price < self.min:
            print(price)
            self.min = price
            self.count = 1
            return self.count
        
        if price == self.prices[-2]:
            self.count += 1
            return self.count
        else:
            i = len(self.prices)-2
            self.count = 1
            while i>=0:
                if self.prices[i] <= price:
                    self.count += 1
                    i -= 1
                else:
                    break
            return self.count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)