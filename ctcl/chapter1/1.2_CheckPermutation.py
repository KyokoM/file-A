import unittest
from collections import Counter
## O(NlogN)
## find O(N) way using countertttgtt
def check_permutation(str1, str2):
    list1=list(str1)
    list2=list(str2)
    if (''.join(sorted(list1)))==(''.join(sorted(list2))):
        return True
    return False

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()