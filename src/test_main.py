import unittest
import function
from typing import OrderedDict


class TestFunction(unittest.TestCase):

	@classmethod
	def setUp(cls):
		cls.testDict = OrderedDict()
		cls.testDict['Student Number'] = 50050170
		cls.testDict['Student Name'] = 'Bob Marley'
		cls.testDict['Programming'] = 75
		cls.testDict['Computing Foundations'] = 57
		cls.testDict['Databases'] = 75
		cls.testDict['Web Development'] = 89
		cls.testDict['Software Engineering'] = 67
		cls.testDict['Data Analysis'] = 76
		cls.testDict['User Experience'] = 88
		cls.testDict['Cloud Computing'] = 88

	def test_upper(self):
		self.assertIsNotNone(self.testDict)


if __name__ == '__main__':
	unittest.main()
