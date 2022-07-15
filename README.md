# FinalProject

## MetaData

  #### Jasmine Malik  
  #### DS 5100 Final Project, Monte Carlo Simulator

## Synopsis

#### Installing Classes

    add info here

#### Importing Classes

    import pandas as pd
    import numpy as np
    import random
    from classes import *

#### Creating a Die Object with Int Faces

    face_list = [1,2,3,4,5,6]
    die_object = Die(face_list)
    
#### Creating a Die Object with Char Faces

    face_list = ['H','T']
    die_object = Die(face_list)
    
#### Playing a game with the Game Object
    
      #create a list of die objects to be used in the game
      
      die_list = [die_object, die_object]
      my_game = Game(die_list)
      
      # The Play method will roll each die a specified amount of times,
      # and creates a private dataframe with the results
      
      my_game.play(3)
      
      # The show method will display the dataframe made from play method.
      # Takes a parameter of form, that can be set to either 'narrow' or wide, which is the default, changes the setup of the dataframe.
      
      my_game.show()
      
      my_game.show(form = 'narrow')
      
      
#### Analyzing a game with the Analyzer Class

      # An analyzer object is created with one parameter, a game object.
      # The analyzer will have a game attribute 
      
      my_analyzer = Analyzer(my_game)
      
      # The face_counts() method in analyzer will compute the number
      # of times each face has been rolled per roll out of all of the die.
      #Takes no parameters, returns a dataframe with columns with each face and each roll per row.
      
      my_analyzer.face_counts()
      
      # The jackpot() method counts the amount of times a roll has resulted in all of the faces being the same.
      # Returns an integer of the number of times a jackpot has occured.
      # Creates a dataframe object as well.
      
      my_analyzer.jackpot()
      
      # The combo method will compute all of the combinations of faces rolled and return a dataframe of the results.
      
      my_analyzer.combo()
      
  
 ## API Description
 
A list of all classes with their public methods and attributes.
Each item should show their docstrings.
All paramters (with data types and defaults) should be described.
All return values should be described.
Do not describe private methods and attributes.
  
#### Die Init() method 
    
    face_list = [1,2,3,4,5,6]
    die_object = Die(face_list)
  
  
  
  
  
  
  

