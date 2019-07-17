# O(NxN)
import unittest
# TODO rotates a matrix 90 degrees clockwise instead of using a new two-dimensional list.

def rotate_matrix(matrix):
    n=len(matrix)
    rotateMatrix=[]
    for i in range(n):
        rotateMatrix.append([matrix[n-1][i]])
    for j in range(n-2,-1,-1):
        for i in range(n):
            rotateMatrix[i].append(matrix[j][i])
    return rotateMatrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)
  
if __name__ == "__main__":
    unittest.main()