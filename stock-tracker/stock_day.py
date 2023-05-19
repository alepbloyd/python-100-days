class StockDay():
  def __init__(self, day_json):
    self.date = day_json[0]
    self.stock_info = day_json[1]
    self.open_price = float(self.stock_info['1. open'])
    self.high_price = float(self.stock_info['2. high'])
    self.low_price = float(self.stock_info['3. low'])
    self.close_price = float(self.stock_info['4. close'])
    self.adjusted_close_price = float(self.stock_info['5. adjusted close'])
    self.volume = int(self.stock_info['6. volume'])
    self.dividend_amount = float(self.stock_info['7. dividend amount'])
    self.split_coefficient = float(self.stock_info['8. split coefficient'])