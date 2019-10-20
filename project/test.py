import unittest
import iden
import user_story

path = 'project03.ged'
iden_list = iden.read_ind_info(path)
fam_list = iden.read_fam_info(path)


class TestUserStory(unittest.TestCase):
    # test for code of us01
    def test_us01_01(self):
        result = user_story.user_story_01(iden_list,fam_list)[0]
        self.assertEqual(result, ['I4'])
        
    # test for code of us02
    def test_us02_01(self):
        test_list_ind = []
        test_list_fam = []
        test_list_ind.append(iden.Individual('I1', None, None, '1950-1-1', None, None, None, None, None))
        test_list_fam.append(iden.Family('F1', '1975-1-1', None, None, None, None, None, None))
        result = user_story.us_02(test_list_ind, test_list_fam)[0]
        self.assertEqual(result, [])

    def test_us02_02(self):
        test_list_ind = []
        test_list_fam = []
        test_list_ind.append(iden.Individual('I1', None, None, '1975-1-1', None, None, None, None, None))
        test_list_fam.append(iden.Family('F1', '1950-1-1', None, None, None, None, None, None))
        result = user_story.us_02(test_list_ind, test_list_fam)[0]
        self.assertEqual(result, ['I1'])

    # test for code of us03
    def test_us03_01(self):
        test_list_ind = []
        test_list_ind.append(iden.Individual('I1', None, None, '1950-1-1', None, None, '1999-1-1', None, None))
        result = user_story.us_03(test_list_ind)[0]
        self.assertEqual(result, [])

    def test_us03_02(self):
        test_list_ind = []
        test_list_ind.append(iden.Individual('I1', None, None, '1970-1-1', None, None, '1950-1-1', None, None))
        result = user_story.us_03(test_list_ind)[0]
        self.assertEqual(result, ['I1'])

    # test for code of us04
    def test_us04_01(self):
        result = user_story.us_04(fam_list)[0]
        self.assertEqual(result, ['F2'])

    def test_us04_02(self):
        test_list = []
        test_list.append(iden.Family('F1', '1997-1-3', '2020-3-1', None, None, None, None, None))
        test_list.append(iden.Family('F2', '1000-1-3', '2020-3-1', None, None, None, None, None))
        result = user_story.us_04(test_list)[0]
        self.assertEqual(result, [])

    def test_us04_03(self):
        test_list = []
        test_list.append(iden.Family('F1', '1997-1-3', '1973-3-1', None, None, None, None, None))
        test_list.append(iden.Family('F2', '1000-1-3', '1000-3-1', None, None, None, None, None))
        test_list.append(iden.Family('F3', '1000-1-3', '1000-1-1', None, None, None, None, None))
        result = user_story.us_04(test_list)[0]
        self.assertEqual(result, ['F1', 'F3'])

    # test for code of us05
    def test_us05_01(self):
        test_list = []
        test_list_1 = []
        test_list.append(iden.Family('F1','2000-1-1',None,'I1',None,'I2',None,None))
        test_list_1.append(iden.Individual('I1',None,None,None,None,None,'1990-1-1',None,None))
        result = user_story.user_story_5(test_list_1,test_list)[0]
        self.assertEqual(result,['I1'])

    def test_us05_02(self):
        test_list = []
        test_list1 = []
        test_list.append(iden.Family('F1','1980-1-1',None,'I1',None,'I2',None,None))
        test_list1.append(iden.Individual('I1',None,None,None,None,None,'1990-1-1',None,None))
        result = user_story.user_story_5(test_list1,test_list)[0]
        self.assertEqual(result,[])

    ## test for code of us06
    def test_us06_01(self):
        test_list = []
        test_list1 = []
        test_list.append(iden.Family('F1',None,'2000-1-1','I1',None,'I2',None,None))
        test_list1.append(iden.Individual('I1',None,None,None,None,None,'1990-1-1',None,None))
        result = user_story.user_story_6(test_list1,test_list)[0]
        self.assertEqual(result,['I1'])

    def test_us06_02(self):
        test_list = []
        test_list1 = []
        test_list.append(iden.Family('F1',None,'1980-1-1','I1',None,'I2',None,None))
        test_list1.append(iden.Individual('I1',None,None,None,None,None,'1990-1-1',None,None))
        result = user_story.user_story_6(test_list1,test_list)[0]
        self.assertEqual(result,[])

    # test for code of us07
    def test_us07_01(self):
        test_list = []
        test_list.append(iden.Individual('I1',None,None,None,170,None,None,None,None))
        result = user_story.user_story_7(test_list)[0]
        self.assertEqual(result,['I1'])

    def test_us07_02(self):
        test_list = []
        test_list.append(iden.Individual('I1',None,None,None,70,None,None,None,None))
        result = user_story.user_story_7(test_list)[0]
        self.assertEqual(result,[])

    #test for code of us08
    def test_us08_01(self):
        test_list = []
        test_list1 = []
        test_list.append(iden.Individual('I1',None,None,'1990-1-1',None,None,None,None,None))
        test_list1.append(iden.Family('F1','1980-1-1',None,'I1',None,'I2',None,{'I1','I2'}))
        result = user_story.user_story_8(test_list,test_list1)[0]
        self.assertEqual(result,[])

    def test_us08_02(self):
        test_list = []
        test_list1 = []
        test_list.append(iden.Individual('I1',None,None,'1990-1-1',None,None,None,None,None))
        test_list1.append(iden.Family('F1','1995-1-1',None,'I1',None,'I2',None,{'I1','I2'}))
        result = user_story.user_story_8(test_list,test_list1)[0]
        self.assertEqual(result,['F1'])
    
    #test for code of us09
    def test_us09_01(self):
        result = user_story.user_story_9(iden_list)[0]
        self.assertEqual(result, ['I1'])

    #test for code of us10
    def test_us10_01(self):
        result = user_story.user_story_10(iden_list, fam_list)[0]
        self.assertEqual(result, ['I1','I2','I11'])
    
    #test for code of us11
    def test_us11_01(self):
        result = user_story.user_story_11(iden_list, fam_list)[0]
        self.assertEqual(result, ['I9'])

    #test for code of us12
    def test_us12_01(self):
        result = user_story.user_story_12(iden_list)[0]
        self.assertEqual(result, ['I7','I8'])
    
    #test for code of us13
    def test_us13_01(self):
        result = user_story.user_story_13(iden_list,fam_list)[0]
        self.assertEqual(result, ['F1', 'F5'])
    
    #test for code of us14
    def test_us14_01(self):
        result = user_story.user_story_14(iden_list,fam_list)[0]
        self.assertEqual(result, ['F5'])

    #test for code of us15
    def test_us15_01(self):
        result = user_story.user_story_15(fam_list)[0]
        self.assertEqual(result, ['F5'])

    #test for code of us16
    def test_us16_01(self):
        result = user_story.user_story_16(iden_list,fam_list)[0]
        self.assertEqual(result, ['F5'])


    # test for code of us17
    def test_us17_01(self):
        result = user_story.user_story_17(fam_list)[0]
        self.assertEqual(result, ['F3', 'F5'])


    def test_us17_02(self):
        test_list_fam = []
        test_list_fam.append(iden.Family('F1', None, None, 'I2', None, 'I3', None, {'I2'}))
        test_list_fam.append(iden.Family('F3', None, None, 'I4', None, 'I5', None, {'I5'}))
        result = user_story.user_story_17(test_list_fam)[0]
        self.assertEqual(result, ['F1', 'F3'])




if __name__ == '__main__':
    unittest. main()