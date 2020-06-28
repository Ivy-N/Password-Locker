import unittest # Importing the unittest module
from accountcredential import Accountcredential 

class TestAccountcredential(unittest.TestCase):

    def setUp(self):
        self.new_accountcredential = Accountcredential("Instagram","James","jaymo") 

    def tearDown(self):
        Accountcredentials.accountcredentials_list = []

    def test_init(self):
        self.assertEqual(self.new_accountcredential.account,"Instagram")
        self.assertEqual(self.new_accountcredential.username,"James")
        self.assertEqual(self.new_accountcredential.password,"jaymo")

    def test_save_accountcredential(self):
        self.new_accountcredential.save_accountcredential()
        self.assertEqual(len(Accountcredential.accountcredential_list),1)

    def test_save_multiple_accountcredential(self):
        self.new_accountcredential.save_accountcredential()
        test_accountcredential = Accountcredential("Testaccount","Testusername","Testpassword")
        test_accountcredential.save_accountcredential
        self.assertEqual(len(Accountcredential.accountcredential_list),2)

    def test_delete_accountcredential(self):
            
        self.new_accountcredential.save_accountcredential()
        test_accountcredential = Accountcredential("Testaccount","Testusername","Testpassword") # new accountcredential
        test_accountcredential.save_accountcredential()

        self.new_accountcredential.delete_accountcredential()# Deleting a accountcredential object
        self.assertEqual(len(Accountcredential.accountcredential_list),1)

    def test_find_by_number(self):

        self.new_accountcredential.save_accountcredential()
        test_accountcredential = Accountcredential("Testaccount","Testusername","Testpassword") # new accountcredential
        test_accountcredential.save_accountcredential()

        found_accountcredential = Accountcredential.find_by_number("Testaccount")

        self.assertEqual(found_accountcredential.email,test_accountcredential.email)

    def test_accountcredential_exists(self):

        self.new_accountcredential.save_accountcredential()
        test_accountcredential = Accountcredential("Testaccount","Testusername","Testpassword") # new accountcredential
        test_accountcredential.save_accountcredential()

        accountcredential_exists = Accountcredential.accountcredential_exist("Testaccount")

        self.assertTrue(accountcredential_exists)

if __name__ == '__main__':
    unittest.main()

