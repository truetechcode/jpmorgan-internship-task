import unittest
from client import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock = quote['stock']
    bid_price = quote['top_bid']['price']
    ask_price = quote['top_ask']['price']
    price = (bid_price + ask_price)/2
    dataPoint = (stock, bid_price, ask_price, price)
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),dataPoint)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock = quote['stock']
    bid_price = quote['top_bid']['price']
    ask_price = quote['top_ask']['price']
    price = (bid_price + ask_price)/2
    dataPoint = (stock, bid_price, ask_price, price)
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),dataPoint)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculatePriceRatio(self):
    price_a = 119
    price_b = 120
    ratio = price_a/price_b
    self.assertEqual(getRatio(price_a, price_b), ratio)

  def test_getRatio_calculatePriceRatioPriceEqualZero(self):
    price_a = 119
    price_b = 0
    ratio = price_b
    self.assertEqual(getRatio(price_a, price_b), ratio)

if __name__ == '__main__':
    unittest.main()
