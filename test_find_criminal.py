from find_criminal import *
import unittest
import random as rd
import statistics as st

# SequenceDatabase PARAMS
S_STRING_LEN = 6  # the maximum length of string to insert (4^STRING_LEN should be ~TEST_NUM for good tests)
S_TEST_NUM = 500  # the number of tests to run per database
S_DATABASE_NUM = 100  # the number of databases to test

# OrfFinder PARAMS
O_STRING_LEN = 300  # length of the genome
O_TEST_NUM = 200  # number of tests per genome
O_DATABASE_NUM = 100  # number of genomes to test
O_INV_HAS_ADFIX_CHANCE = 10  # 1/chance that adfix isnt guaranteed to be in genome.
O_ADFIX_SCALING = 4  # exponential scaling applied to adfix length to make adfixes more likely to be shorter.

class TestAssignment3(unittest.TestCase):
    @staticmethod
    def listFailures(failures, test_num):
        if len(failures):
            print('\n The following failures arose:\n', *failures)
            raise AssertionError(f" - {len(failures)} failures out of {test_num} tests.")

    def testEdgeCases(self):
        print("\nTest Edge Cases", end="")
        failures = []
        # SequenceDatabase
        db = SequenceDatabase()
        tests = [
            [SequenceDatabase().query(""), None],  # empty database, empty query
            [SequenceDatabase().query("A"), None],  # empty database, non-empty query
            [SequenceDatabase().query("D"), None],  # empty databse, non-empty query
            [db.addSequence("A"), None],  # single letter database queries
            [db.query("A"), "A"],         #  |
            [db.query("B"), None],        #  |
            [db.query("C"), None],        #  |
            [db.query("D"), None] ,       #  |
            [db.addSequence("AA"), None],    # Prefixed database queries
            [db.addSequence("AAA"), None],   # |
            [db.addSequence("AAAA"), None],  # |
            [db.query("A"), "A"] ,           # |
            [db.query("AA"), "AA"] ,         # |
            [db.addSequence("AAA"), None],   # |
            [db.query("A"), "AAA"]           # |
        ]
        for t in tests:
            try:
                self.assertEqual(t[0], t[1])
            except AssertionError as e:
                failures.append(str(e))

        self.listFailures(failures, 15 + 8)

    def testGivenTests(self):
        print("\nTest Provided Tests", end="")
        failures = []
        # SequenceDatabase
        db = SequenceDatabase()
        tests = [
            [db.addSequence("ABCD"), None],
            [db.addSequence("ABC"), None],
            [db.addSequence("ABC"), None],
            [db.query("A"), "ABC"],
            [db.addSequence("ABCD"), None],
            [db.query("A"), "ABC", None],
            [db.addSequence("ABCD"), None],
            [db.query(""), "ABCD"],
            [db.query("A"), "ABCD"],
            [db.query("B"), None],
        ]
        for t in tests:
            try:
                self.assertEqual(t[0], t[1])
            except AssertionError as e:
                failures.append(str(e))

        self.listFailures(failures, 20)

    def testSequenceDatabase(self):
        print()
        STRING_LEN = S_STRING_LEN  # the maximum length of string to insert (4^STRING_LEN should be ~TEST_NUM for good tests)
        TEST_NUM = S_TEST_NUM  # the number of tests to run per database
        DATABASE_NUM = S_DATABASE_NUM  # the number of databases to test
        failures = []
        for d in range(DATABASE_NUM):
            print("\rTest SequenceDatabase -", d+1, "/", DATABASE_NUM, end="")
            db = SequenceDatabase()
            strings = []
            for _ in range(TEST_NUM):
                strings.append("".join(rd.choices("ABCD", k=rd.randint(1, STRING_LEN))))
                s = "".join(rd.choices("ABCD", k=rd.randint(0, len(strings[-1]))))
                db.addSequence(strings[-1])
                try:
                    self.assertEqual(db.query(s), min(st.multimode(max([x for x in strings if x.startswith(s)], [None], key=lambda x: len(x)))))
                    # failures.append("\n\n\nLast Added String: " + strings[-1])
                except AssertionError as e:
                    failures.append("\n\n\nLast Added String: " + strings[-1] + "\nQueried String: " + s + " \n" + str(e))
        self.listFailures(failures, DATABASE_NUM*TEST_NUM)

if __name__ == "__main__":
    rd.seed()
    unittest.main()