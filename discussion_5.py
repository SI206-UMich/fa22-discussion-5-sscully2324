import unittest


def count_a(sentence):
	count = 0
	for letter in sentence:
		if letter == 'a':
			count += 1
	return count




class Item:
	
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

class Warehouse:

	def __init__(self, items = []):
		self.items = items[:]

	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	def add_item(self, item):
		self.items.append(item)
	
	def get_max_stock(self):
		return max(self.items, key = lambda item: item.stock)
	
	def get_max_price(self):
		return max(self.items, key=lambda item: item.price)

class TestAllMethods(unittest.TestCase):

	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	def test_count_a(self):
		self.assertEqual(count_a(self.item1.name), 0, "count_a failed on item1")
		self.assertEqual(count_a(self.item2.name), 0, "count_a failed on item2")
		self.assertEqual(count_a(self.item3.name), 1, "count_a failed on item3")
		self.assertEqual(count_a(self.item4.name), 2, "count_a failed on item4")
		self.assertEqual(count_a(self.item5.name), 2, "count_a failed on item5")

	def test_warehouse_add_item(self):
		warehouse = Warehouse()
		warehouse.add_item(self.item1)
		warehouse.add_item(self.item2)
		warehouse.add_item(self.item3)
		warehouse.add_item(self.item4)
		warehouse.add_item(self.item5)
		self.assertEqual(len(warehouse.items), 5, "add_item failed")

	def test_warehouse_get_max_stock(self):
		warehouse = Warehouse()
		warehouse.add_item(self.item1)
		warehouse.add_item(self.item2)
		warehouse.add_item(self.item3)
		warehouse.add_item(self.item4)
		warehouse.add_item(self.item5)
		self.assertEqual(warehouse.get_max_stock(), self.item3, "get_max_stock failed")
	
	def test_warehouse_get_max_price(self):
		warehouse = Warehouse()
		warehouse.add_item(self.item1)
		warehouse.add_item(self.item2)
		warehouse.add_item(self.item3)
		warehouse.add_item(self.item4)
		warehouse.add_item(self.item5)
		self.assertEqual(warehouse.get_max_price(), self.item1, "get_max_price failed")
	
def main():
	unittest.main()

if __name__ == "__main__":
	main()