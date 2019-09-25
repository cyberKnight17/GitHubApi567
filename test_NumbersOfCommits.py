import NumberOfCommits
import unittest


class TestNumberOfCommits(unittest.TestCase):
    def get_repo_list_1(self):
        self.assertIn("GitHubApi567", NumberOfCommits.get_repo_list("dingtongwang0"))

    def get_repo_list_2(self):
        self.assertIn("helloflask", NumberOfCommits.get_repo_list("dingtongwang0"))

    def get_repo_list_3(self):
        self.assertIn("LeetCode", NumberOfCommits.get_repo_list("dingtongwang0"))

    def get_get_com_num_1(self):
        self.assertEqual(271, NumberOfCommits.get_com_num("dingtongwang0", "helloflask"))

    def get_get_com_num_2(self):
        self.assertEqual(121, NumberOfCommits.get_com_num("dingtongwang0", "SSW-555-GEDCOM"))

    def get_get_com_num_3(self):
        self.assertEqual(5, NumberOfCommits.get_com_num("dingtongwang0", "watchlist"))


if __name__ == '__main__':
    unittest.main()
