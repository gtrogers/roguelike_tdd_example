Feature: Game play

    Scenario: Drawing the player and NPC
        Given a new game
         When the game starts
         Then the player and npc are drawn

    Scenario: Moving the player
        Given a new game
         When the game starts
          And the down key is pressed
         Then the player moves down

    Scenario: Drawing the map
        Given a new game
         When the game starts
         Then the map gets drawn

    Scenario: Walls
       Given a game with walls
        When the player walks into a wall
        Then they should not move
