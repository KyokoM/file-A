# O(N)
import unittest
## TODO(@KyokoM)
## use zip
def one_away(s1, s2):
    if len(s1)==len(s2):
        return isOneDiff(s1,s2)
    if len(s1)+1==len(s2):
        return isOneDel(s1,s2)
    if len(s2)+1==len(s1):
        return isOneDel(s2,s1)
    return False
def isOneDiff(s1,s2):
    diff=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            diff=diff+1
            if diff>1:
                return False
    return True

def isOneDel(s1,s2):
    i=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            break
    if i==len(s1)-1 and s1[i]==s2[i]:
        return True
    for j in range(i,len(s1)):
        if s1[j]!=s2[j+1]:
            return False
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()