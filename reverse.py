import unittest

def reverse(oristr):
        # print(str)
        strList = oristr.split(" ")
        # print(strList)
        resultList = []
        for strs in strList:
            if (strs != ""):
                resultList.append(strs[::-1])
        # print(resultList)
        result = " ".join(resultList)
        return result

class ReverseTestCase(unittest.TestCase):
    def test_sample(self):
        expected = 'deppilf moorssalc si tnatropmi'
        result = reverse('flipped classroom is important')
        self.assertEqual(expected, result)
        expected = 'ymedacaiynuj'
        result = reverse('junyiacademy')
        self.assertEqual(expected, result)

    def test_empty_string(self):
        expected = ''
        result = reverse('')
        self.assertEqual(expected, result)

    def test_single_string(self):
        expected = 'olleh'
        result = reverse('hello')
        self.assertEqual(expected, result)
    
    def test_character(self):
        expected = 'h e l l o'
        result = reverse('h e l l o')
        self.assertEqual(expected, result)

    def test_character(self):
        expected = 'h e l l o'
        result = reverse('h e l l o')
        self.assertEqual(expected, result)

    def test_whitespace(self):
        expected = 'h e l l o'
        result = reverse(' h e l l o ')
        self.assertEqual(expected, result)

suite = unittest.TestSuite()
suite.addTest(ReverseTestCase('test_sample'))
suite.addTest(ReverseTestCase('test_empty_string'))
suite.addTest(ReverseTestCase('test_single_string'))
suite.addTest(ReverseTestCase('test_character'))
suite.addTest(ReverseTestCase('test_whitespace'))

unittest.TextTestRunner(verbosity=2).run(suite)