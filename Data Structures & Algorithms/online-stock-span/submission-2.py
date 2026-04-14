class StockSpanner:

    def __init__(self):
        self.days=[]

    def next(self, price: int) -> int:
        span=self.find_span(price)
        return span


    def find_span(self, price):
        span=1
        while self.days and self.days[-1][1]<=price:
            span+=self.days[-1][0]
            self.days.pop()
        self.days.append([span,price])
        return span
    """
    Naive
    """
    # def find_span(self, price):
    #     stack=[]
    #     #[100]
    #     """
    #     []
    #     [80]
    #     """
    #     stack = []
    #     for number in reversed(self.days):
    #         if number <= price:
    #             stack.append(number)
    #         else:
    #             break
    #     return len(stack) + 1
 


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)