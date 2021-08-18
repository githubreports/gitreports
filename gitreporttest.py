import unittest
import gitreport
import requests
import responses


class Mytest(unittest.TestCase):
   def test_user(self):
       actual = gitreport.get_user_details(headers = {'Authorization': 'token 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'})
       expected = {'login': 'kiran007', 'name': 'Kiran Reddy', 'email': 'kiran.yerram139@gmail.com'}
       self.assertEqual(actual, expected)

   def test_getlanguages(self):
       actual = gitreport.get_all_languages(headers={'Authorization': 'token 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'}, repo="myrepo", org="githubreports")
       expected = ["Java", "Python"]
       self.assertEqual(actual, expected)

   def test_generatecsv(self):
       actual = gitreport.generate_csv_report({'login': 'kiran007', 'name': 'Kiran Reddy',\
                                            'email': 'kiran.yerram139@gmail.com', \
                                            "repos":"python_project,myrepo", "languages":"java,python,go"})
       expected = "Success"
       self.assertEqual(actual, expected)

