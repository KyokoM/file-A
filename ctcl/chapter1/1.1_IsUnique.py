import unittest
# O(N)
# TODO(@KyokoM)
# take care whether the string is ASCII (128 characters)　or Unicode
# check whether len(string) is over 128(if you have more length than the kind of word, it will fail)
def unique(string):
    character={}
    for st in string:
        if st in character:
            return False
        else:
            character[st]=1
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()