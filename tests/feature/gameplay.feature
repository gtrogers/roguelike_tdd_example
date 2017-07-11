Feature: Game play

    Scenario: Moving the player
        Given a new game
         When the down key is pressed
         Then the player moves down
          And the NPC gets drawn
