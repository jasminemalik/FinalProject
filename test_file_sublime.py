import unittest
from classes import *


#RECIEVE CORRECT INPUTS AND RETURN CORRECT OUTPUTS

class TestingClass(unittest.TestCase):
    '''
    This is a class that imports unittest and the die classes to
    create unit tests for each method, which are below.
    '''
    
    def test_die(self):
        '''
        Creates a die object, tests the insertion of faces
        '''
        faces = [1,2,3]
        test_die = Die(faces)
        
        self.assertEqual(test_die.faces, faces)

        
    def test_change_weight(self):
        """
        This method tests the change_weight method on a die object.
        It inputs an invalid face value, and then also an invalid weight value.
        """
        faces = [1,2,3]
        test_die = Die(faces)

        incorrect_face = test_die.change_weight(4,1)
        expect_ed = 'The number inputed is not a face in the die'

        self.assertEqual(incorrect_face, expect_ed)

        incorrect_weight = test_die.change_weight(1,"t")
        expect_ed = 'Enter a numeric for weight'
        
        self.assertEqual(incorrect_weight, expect_ed)

    def test_show_die(self):
        """
        This method tests the show_die method. 
        Tests it by changing the weight and then testing
        to see if the weight has updated in the dataframe.
        """
        faces = [1,2,3]
        test_die = Die(faces)
        test_die.change_weight(1,5)
        testdf = test_die.show_die()

        self.assertEqual(testdf.at[0,'weights'], 5)

    def test_roll(self):
        '''
        Tests the roll method in the die class, ensures
        that the proper data type is returned and that the 
        correct values are in the list
        '''
        faces = [3]
        test_die = Die(faces)
       
        rolls_list = test_die.roll_die(3)

        self.assertEqual(len(test_die.roll_die(3)), 3)
        self.assertEqual(type(rolls_list), list)
        self.assertTrue(rolls_list[0]==3)


#Testing the Game Class methods

    def test_game_init(self):
        '''
        Tests the creation of a game object.
        '''
        faces = [1,2,3,4,5,6]
        faces2 = [1,2,3,4,5,6]
        
        test_die = Die(faces)
        test_die2 = Die(faces2)

        dielist = [test_die, test_die2]
        testgame = Game(dielist)

        self.assertEqual(testgame.dies, dielist)


    def test_play(self):
        '''
        Tests the play method in the game class. Ensures that a dataframe is outputed,
        and that it is of the right size.
        '''
        faces = [1,1,1]
        faces2 = [6,6,6]
        
        test_die = Die(faces)
        test_die2 = Die(faces2)

        dielist = [test_die, test_die2]
        testgame = Game(dielist)
        testgame.play(5)

        testdf = testgame.show()

        self.assertEqual(len(testdf), 5)
        self.assertEqual(testdf.values[0][0],1)
        self.assertEqual(type(testdf), pd.DataFrame)


    def test_show(self):
        '''
        This tests shows the show() metohd in the Game class. We test to make sure 
        the dataframe sizes and values are correct based off of the face values on 
        die objects in the game.
        '''
        faces = [1,1,1]
        faces2 = [2,2,2]
        
        test_die = Die(faces)
        test_die2 = Die(faces2)

        dielist = [test_die, test_die2]
        testgame = Game(dielist)
        testgame.play(5)

        testshowdf = testgame.show()

        self.assertEqual(len(testgame.show()), 5)
        self.assertEqual(len(testgame.show(form = "narrow")), 10)
        self.assertEqual(testshowdf.values[0][0], 1)


#Test methods for the Analyzer class 

    def test_analyzer_init(self):
        '''
        This tests the Analyzer initializer method. If the game attribute 
        is accurate for the object.
        '''
        faces = [1,2,3,4,5,6]
        faces2 = [1,2,3,4,5,6]
        
        test_die = Die(faces)
        test_die2 = Die(faces2)

        dielist = [test_die, test_die2]
        testgame = Game(dielist)
        testgame.play(5)

        test_analyzer = Analyzer(testgame)

        self.assertEqual(test_analyzer.game, testgame)
        self.assertTrue(type(test_analyzer), Analyzer)

    def test_analyzer_face_counts(self):
        '''
        Tests the face_counts method in the Analyzer class. Tests for correct values,
        type of return and size of expected object to be returned.
        '''
        faces = [1,1]
        faces2 = [4,4]
        
        test_die = Die(faces)
        test_die2 = Die(faces2)

        dielist = [test_die, test_die2]
        testgame = Game(dielist)
        testgame.play(5)

        test_analyzer = Analyzer(testgame)
        test_analyzer.face_counts()

       
        self.assertEqual(len(test_analyzer.face_df.columns), 2)
        self.assertEqual(test_analyzer.face_df.values[0][0], 1)

    def test_analyzer_combo(self):
        '''
        This method tests the combo method in the analyzer class. It returns a dataframe 
        and this method will test for the correct values and size for the dataframe. 
        '''
        faces = [1,1,1,1]
        test_die = Die(faces)
      
        faces2 = [1,1]
        test_die2 = Die(faces2)
        
        dielist = [test_die, test_die]
        
        testgame1 = Game(dielist)
        testgame1.play(5)

        test_analyzer1 = Analyzer(testgame1)
        test_analyzer1.combo()

        self.assertTrue(len(test_analyzer1.combo_df), 5)

    def test_analyzer_jackpot(self):
        '''
        This method tests the jackpot method in the analyzer class. Tests for the correct 
        output for the method and the right amount of columns
        '''
        faces = [1,2,3,4,5,6]
        faces2 = [1,2,3,4,5,6]
        
        test_die = Die(faces)
        test_die2 = Die(faces2)

        dielist = [test_die, test_die2]
        testgame = Game(dielist)
        testgame.play(5)

        test_analyzer = Analyzer(testgame)
        jp = test_analyzer.jackpot()
        self.assertEqual(type(jp), int)

        jp_df = test_analyzer.final_jp_df

        self.assertEqual(len(jp_df.columns),1)




if __name__ == '__main__':
    unittest.main(verbosity=3)

