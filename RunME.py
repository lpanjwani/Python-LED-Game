# Import system modules and custom libraries
import time, GameBootHandler, GameController, keyboard
# Starts the Game which can be called multiple times 
def LetsPlay():
    #  Run Game Boot Handler for start information
    GameBootHandler.Start()
    # waits 5 secs before next excecution 
    time.sleep(5)
    # Run StartGame Function inside GameController
    GameController.StartGame()
# Run function Once    
LetsPlay()

# Continuous Loop for anytime game restart
while True:
    # Waits for user to press the Space bar 
    keyboard.wait('space')
    # Start Game after Space Button Press
    LetsPlay()
