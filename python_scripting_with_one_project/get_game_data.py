import os
import json
import shutil
import subprocess import PIPE, run
import sys


if __name__ == "__main__":
    args = sys.argv
    print(args)
https://youtu.be/dQlw1Cdd3pw?t=693
# - Find all game directories from /data
# - Create a new /games directory 
# - Copy and remove the "game" suffix of all games into the /games directory
# - Create a .json file with the information about the games
# - Compile all of the game code 
# - Run all of the game code-