import unittest
import iden

path = 'project03.ged'
iden_list = iden.read_ind_info(path)
fam_list = iden.read_fam_info(path)


class TestUserStory(unittest.TestCase):
    def test_us04_01(self):
        result = iden.us_04(fam_list)
        self.assertEqual(result, ['F2'])

    def test_us04_02(self):
        test_list = []
        test_list.append(iden.Family('F1', '1997-1-3', '2020-3-1', None, None, None, None, None))
        test_list.append(iden.Family('F2', '1000-1-3', '2020-3-1', None, None, None, None, None))
        result = iden.us_04(test_list)
        self.assertEqual(result, [])

    def test_us04_03(self):
        test_list = []
        test_list.append(iden.Family('F1', '1997-1-3', '1973-3-1', None, None, None, None, None))
        test_list.append(iden.Family('F2', '1000-1-3', '1000-3-1', None, None, None, None, None))
        test_list.append(iden.Family('F3', '1000-1-3', '1000-1-1', None, None, None, None, None))
        result = iden.us_04(test_list)
        self.assertEqual(result, ['F1', 'F3'])



if __name__ == '__main__':
    unittest.main()