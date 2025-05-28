# Pygame Shooter Game

This is a simple vertical scrolling shooter game created using Pygame. The player controls a rocket ship and shoots at falling UFOs, gasoline canisters, and asteroids.

## How to Play

-   Use the 'A' and 'D' keys to move the rocket ship left and right.
-   Press the 'SPACE' bar to shoot bullets.
-   The goal is to shoot down the UFOs to earn points.
-   Avoid colliding with the falling objects (UFOs and asteroids), as this will decrease your life.
-   Collecting gasoline canisters will increase your life.
-   The game ends when you have 20 misses (objects pass without being hit) or your life reaches zero.

## Game Elements

-   **Player:** A rocket ship that the user controls.
-   **Enemies:**
    -   UFOs: Shooting these earns points. Colliding with them reduces life.
    -   Gasoline Canisters: Collecting these increases life.
    -   Asteroids: Colliding with these reduces life.
-   **Bullets:** Projectiles fired by the player to destroy enemies.
-   **Score:** Tracks the number of UFOs shot down (points).
-   **Life:** Represents the player's health.
-   **Strikes:** Counts the number of enemies that pass the player without being hit.

## Setup

To run this game, you need to have Pygame installed. If you don't have it, you can install it using pip:

```bash
pip install pygame
Save the provided code as a Python file (e.g., shooter.py) and ensure the image files (galaxy.jpg, gameover.jpg, rocket.png, ufo.png, png-transparent-gasoline-others-miscellaneous-jerrycan-canister-thumbnail-removebg-preview.png, png-transparent-hayabusa2-asteroid-162173-ryugu-space-probe-asteroid-spacecraft-outer-space-nasa-removebg-preview.png, and bullet.png) are in the same directory.

Running the Game
Navigate to the directory where you saved the file in your terminal and run:

Bash

python shooter.py
Enjoy playing!
