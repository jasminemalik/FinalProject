# A code block with your classes.
import pandas as pd
import numpy as np
import random

class Die:
    
    """
    A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 
    The die has one behavior, which is to be rolled one or more times.
    """
    
    def __init__(self, faces):
        """
        Initializes a die object. Takes in a list of faces as either numbers or strings.
        Returns None and just initializes an object. 
        Has faces, a list of the die faces as an attribute
        Has weights that are set to 1 for each face, list
        creates a dataframe with faces and weights
        """


        self.faces = faces
        self.weights = np.ones(len(faces))
        self._df = pd.DataFrame({'faces':self.faces,
                               'weights':self.weights})
    def change_weight(self, die_face, new_weight):
        """
        This method changes a weight of one face of a die.
        It has two params, the face to change, and the new weight.
        It will return the new dataframe with the updated weight.

        Checks to make sure a valid weight is entered
        """
        if type(new_weight) == int or type(new_weight) == float:
            if die_face in self.faces:
                ind = self.faces.index(die_face)

                if type(float(new_weight)) == float:
                        oldweight = self._df['weights'][ind]
                        self._df.at[ind,'weights'] = new_weight
                        #return self.df
                else:
                    return "Weight cannot be converted into a float"

            else:
                return "The number inputed is not a face in the die"
        else:
            return "Enter a numeric for weight"
        
        
        
    def show_die(self):
        '''
        Shows the current die, faces with current weights. Takes no parameters and returns the dataframe.
        '''
        return self._df
    
    def roll_die(self,n=1):
        '''
        This method takes a random face from the die object, according to the weights to each face.
        It has one parameter, number of rolls and will return a list of the rolls. 
        '''
        rolls = []
        for i in range(n):
            x = random.choices(self.faces, weights = self._df['weights'])
            rolls = np.append(rolls, x)
        return list(rolls)
               
class Game:
    '''
    A game consists of rolling of one or more dice of the same kind one or more times. 
    By “same kind” and “similarly defined” we mean that each die in a given game has the
    same number of sides and associated faces, but each die object may have its own weights.
    '''
    def __init__(self, dies):
        """
        Creates a game. Has parameter of a list of die. Checks to ensure that die are similar. 
        Returns nothing, creates the attribute of dies.
        """
        
        for i in range(len(dies)-1):
            if len(dies[i].faces) != len(dies[i+1].faces):
                print("All dies entered must have the same number of faces")
            else:
                break
        

        for i in range(len(dies)-1):
            if type(dies[i].faces[0]) != type(dies[i+1].faces[0]):
                print("All dies entered must be of the same type of faces")
            else:
                self.dies = dies
    
    
    #Dies are the columns
    def play(self, rolls):
        '''
        The play method takes one parameter, the number of rolls each die should be rolled.
        Saves the result ot a private dataframe.
        '''
        
        final_df = pd.DataFrame()
        count = 1
        num = 1
        rolls_list = []
        
        for die in self.dies:
            
            val = die.roll_die(rolls)
            final_df['Die ' + str(count)] = val
            count += 1

        for i in range(rolls):
            rollname = "Roll " + str(num)
            rolls_list = np.append(rolls_list, rollname)
            num += 1
        
        final_df.index = rolls_list
        final_df.index.name = 'Roll Number'
        self._widedf = final_df
        #return self._widedf 
        
    def show(self, form = "wide"):
        """
        A method to show the user the results of the most recent play.
        Has one parameter, set to wide that is a dataframe with rows x die.
        The other valid form is narrow, which is the dataframe, stacked.
        """
        if form == "wide" or form == "narrow":
            if form == "narrow":
                df_narrow = pd.DataFrame(self._widedf.stack(), columns = ['Face Value'])                   
                return df_narrow
            
            else:
                return self._widedf
       
        else:
            return "Please enter either 'wide' or 'narrow' as a valid form"

class Analyzer:
    """
    An analyzer takes the results of a single game and computes various descriptive 
    statistical properties about it. These properties results are available as 
    attributes of an Analyzer object.
    """
    
    def __init__(self, game):
        '''
        Creates an analyzer object, that has a game object as a parameter. 
        '''
        self.game = game
        
    def face_counts(self):
        '''
        Compute how many times a given face is rolled in each event.
        Stores the results as a dataframe in a public attribute.
        The dataframe has an index of the roll number and face values
        as columns (i.e. it is in wide format).

        '''
        ansdf = pd.DataFrame()
        faces_list = self.game.dies[0].faces
        count = 0
        
        for row in self.game._widedf.iterrows():
            x = row[1]
            y = x.value_counts()
            ansdf = pd.concat([ansdf, y], axis = 1)
            ansdf = ansdf.fillna(0)
        
        self.face_df = ansdf.T
        #return self.ansdf.T
    
    def combo(self):
        '''
        Computes the distinct combinations of faces rolled, along with their counts and puts in a
        dataframe.
        '''
        self.combo_df = self.game.show().apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('n')   
        #return combo_df
    
    def jackpot(self):
        '''
        Method to compute how many times the game resulted in all faces being identical.
        Returns an integer for the number times to the user.
        Stores the results as a dataframe of jackpot results in a public attribute.
        '''
        iterate_df = self.game.show()
        final_jp_df = pd.Series(dtype=int)
        count = 0
        
        for row in iterate_df.iterrows():
            x = row[1]
            y = x.unique()
            
            if len(y) == 1:
                count += 1
                row_number = row[0]
                new_df = pd.Series({row_number:y[0]}, index=[row_number])
                final_jp_df = pd.concat([final_jp_df, new_df], axis = 0)
                final_jp_df = pd.DataFrame(final_jp_df, columns = ['Face Value'])
                self.final_jp_df = final_jp_df.dropna()

            else:
                self.final_jp_df = pd.DataFrame({'Jackpot':[0]})
                
        return count






