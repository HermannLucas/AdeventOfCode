
import unittest
import Code

class TestDay2(unittest.TestCase):

    def setUp(self):
        self.sit = Code.spreadsheet_checksum()

    def test_difference_one_line(self):

        problem = 5195
        problem = [int(i) for i in str(problem)]

        expected_result = 8

        self.assertEqual(self.sit.difference_line(problem), expected_result)

    def test_two_difference_one_line(self):

        problem = 753
        problem = [int(i) for i in str(problem)]


        expected_result = 4

        self.assertEqual(self.sit.difference_line(problem), expected_result)

    def test_three_difference_one_line(self):

        problem = 2468
        problem = [int(i) for i in str(problem)]

        expected_result = 6

        self.assertEqual(self.sit.difference_line(problem), expected_result)

    def test_example_spreadsheet(self):

        problem = [\
                    [5,1,9,5],\
                    [7,5,3],\
                    [2,4,6,8],\
                  ]

        expected_result = 18

        self.assertEqual(self.sit.get_checksum(problem, 1), expected_result)

    def test_problem(self):

        problem = [\
                    [1208,412,743,57,1097,53,71,1029,719,133,258,69,1104,373,367,365],\
                    [4011,4316,1755,4992,228,240,3333,208,247,3319,4555,717,1483,4608,1387,3542],\
                    [675,134,106,115,204,437,1035,1142,195,1115,569,140,1133,190,701,1016],\
                    [4455,2184,5109,221,3794,246,5214,4572,3571,3395,2054,5050,216,878,237,3880],\
                    [4185,5959,292,2293,118,5603,2167,5436,3079,167,243,256,5382,207,5258,4234],\
                    [94,402,126,1293,801,1604,1481,1292,1428,1051,345,1510,1417,684,133,119],\
                    [120,1921,115,3188,82,334,366,3467,103,863,3060,2123,3429,1974,557,3090],\
                    [53,446,994,71,872,898,89,982,957,789,1040,100,133,82,84,791],\
                    [2297,733,575,2896,1470,169,2925,1901,195,2757,1627,1216,148,3037,392,221],\
                    [1343,483,67,1655,57,71,1562,447,58,1561,889,1741,1338,88,1363,560],\
                    [2387,3991,3394,6300,2281,6976,234,204,6244,854,1564,210,195,7007,3773,3623],\
                    [1523,77,1236,1277,112,171,70,1198,86,1664,1767,75,315,143,1450,1610],\
                    [168,2683,1480,200,1666,1999,3418,2177,156,430,2959,3264,2989,136,110,3526],\
                    [8702,6973,203,4401,8135,7752,1704,8890,182,9315,255,229,6539,647,6431,6178],\
                    [2290,157,2759,3771,4112,2063,153,3538,3740,130,3474,1013,180,2164,170,189],\
                    [525,1263,146,954,188,232,1019,918,268,172,1196,1091,1128,234,650,420],\
                  ]

        expected_result = 54426

        self.assertEqual(self.sit.get_checksum(problem, 1), expected_result)

    def test_second_part_first_line(self):

        problem = 5928
        problem = [int(i) for i in str(problem)]

        expected_result = 4

        self.assertEqual(self.sit.evenly_divsible_line(problem), expected_result)

    def test_second_part_second_line(self):

        problem = 9473
        problem = [int(i) for i in str(problem)]

        expected_result = 3

        self.assertEqual(self.sit.evenly_divsible_line(problem), expected_result)

    def test_second_part_third_line(self):

        problem = 3865
        problem = [int(i) for i in str(problem)]

        expected_result = 2

        self.assertEqual(self.sit.evenly_divsible_line(problem), expected_result)

    def test_second_part_example(self):

        problem = [\
                    [5,9,2,8],\
                    [9,4,7,3],\
                    [3,8,6,5],\
                  ]

        expected_result = 9

        self.assertEqual(self.sit.get_checksum(problem, 2), expected_result)

    def test_second_part_problem(self):

        problem = [\
                    [1208,412,743,57,1097,53,71,1029,719,133,258,69,1104,373,367,365],\
                    [4011,4316,1755,4992,228,240,3333,208,247,3319,4555,717,1483,4608,1387,3542],\
                    [675,134,106,115,204,437,1035,1142,195,1115,569,140,1133,190,701,1016],\
                    [4455,2184,5109,221,3794,246,5214,4572,3571,3395,2054,5050,216,878,237,3880],\
                    [4185,5959,292,2293,118,5603,2167,5436,3079,167,243,256,5382,207,5258,4234],\
                    [94,402,126,1293,801,1604,1481,1292,1428,1051,345,1510,1417,684,133,119],\
                    [120,1921,115,3188,82,334,366,3467,103,863,3060,2123,3429,1974,557,3090],\
                    [53,446,994,71,872,898,89,982,957,789,1040,100,133,82,84,791],\
                    [2297,733,575,2896,1470,169,2925,1901,195,2757,1627,1216,148,3037,392,221],\
                    [1343,483,67,1655,57,71,1562,447,58,1561,889,1741,1338,88,1363,560],\
                    [2387,3991,3394,6300,2281,6976,234,204,6244,854,1564,210,195,7007,3773,3623],\
                    [1523,77,1236,1277,112,171,70,1198,86,1664,1767,75,315,143,1450,1610],\
                    [168,2683,1480,200,1666,1999,3418,2177,156,430,2959,3264,2989,136,110,3526],\
                    [8702,6973,203,4401,8135,7752,1704,8890,182,9315,255,229,6539,647,6431,6178],\
                    [2290,157,2759,3771,4112,2063,153,3538,3740,130,3474,1013,180,2164,170,189],\
                    [525,1263,146,954,188,232,1019,918,268,172,1196,1091,1128,234,650,420],\
                  ]
        expected_result = 333

        self.assertEqual(self.sit.get_checksum(problem, 2), expected_result)


if __name__ == '__main__':
    unittest.main()
