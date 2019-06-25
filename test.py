import unittest
from activity_selector import ActivitySelection,ActivitySelectionRecursive,sortEvents

class ActivityTest(unittest.TestCase):
	def test_selection(self):
		events = [[1,4],[3,5],[0,6],[5,7],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]]
		index = [0,3,7,10]
		self.assertListEqual(ActivitySelection(events,0),index)
		
	def test_selection_recursive(self):
		events = [[1,4],[3,5],[0,6],[5,7],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]]
		index = [0,3,7,10]
		self.assertListEqual(ActivitySelectionRecursive(events,0,0,len(events)),index)

if __name__=="__main__":
	unittest.main()