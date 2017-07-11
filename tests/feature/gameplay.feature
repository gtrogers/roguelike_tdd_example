Feature: Game play

    Scenario: Creating the window
        Given a new game
         When the game starts
         Then a window is created

    Scenario: Drawing the player
        Given a new game
         When the game starts
         Then the player gets drawn
