from RPS import *

class TestRPSMethods(unittest.TestCase):
    
    def setup_method(self):
        self.gui = GUI()
    
    def teardown_method(self):
        del self.gui
    
    def test_init(self):
        assert self.gui.__str__() == "Hands Thrown = 0, User Score = 0, Computer Score = 0"
    
    def test_playGame(self):
        assert self.gui.__str__() == "Hands Thrown = 0, User Score = 0, Computer Score = 0"
        self.gui.playGame(1, 2)
        assert self.gui.__str__() == "Hands Thrown = 1, User Score = 0, Computer Score = 1"
        self.gui.playGame(2, 1)
        assert self.gui.__str__() == "Hands Thrown = 2, User Score = 1, Computer Score = 1"
        self.gui.playGame(1, 3)
        assert self.gui.__str__() == "Hands Thrown = 3, User Score = 2, Computer Score = 1"
        self.gui.playGame(1, 1)
        assert self.gui.__str__() == "Hands Thrown = 4, User Score = 2, Computer Score = 1"
        self.gui.playGame(2, 2)
        assert self.gui.__str__() == "Hands Thrown = 5, User Score = 2, Computer Score = 1"
        self.gui.playGame(2, 3)
        assert self.gui.__str__() == "Hands Thrown = 6, User Score = 2, Computer Score = 2"
        self.gui.playGame(3, 1)
        assert self.gui.__str__() == "Hands Thrown = 7, User Score = 2, Computer Score = 3"
        self.gui.playGame(3, 2)
        assert self.gui.__str__() == "Hands Thrown = 8, User Score = 3, Computer Score = 3"
        self.gui.playGame(3, 3)
        assert self.gui.__str__() == "Hands Thrown = 9, User Score = 3, Computer Score = 3"
    
    def test_checkChoice(self):
        self.assertEqual(checkChoice("rock"), 1)
        self.assertEqual(checkChoice("rOcK"), 1)
        self.assertEqual(checkChoice("   rock   "), 1)
        self.assertEqual(checkChoice("paper"), 2)
        self.assertEqual(checkChoice("scissors"), 3)

if __name__ == '__main__':
    unittest.main()