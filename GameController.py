# Import system modules and custom libraries
import opc, time, sys, keyboard, threading, random
# number of LEDs on the board
numLEDs = 360
# Server address and port          
client = opc.Client('localhost:7890')
# Predefined color values
red = (255,0,0)
black = (0,0,0)
white = (255, 255, 255)
blue = (0,0,255)
green = (0,255,0)
# Initialize all pixels as "black"
pixels = [ black ] * numLEDs
userLocation = 0
GameRunning = True

# Using "initGame" as a function to start the game at any time
def initGame():
    # To access outer variables in the function
    global pixels, black, userLocation, GameRunning
    # Initialize all pixels as "black"
    pixels = [ black ] * numLEDs
    # Send pixel information/properties for display
    client.put_pixels(pixels)
    # Ball spawning at random locations at row six 
    userLocation = random.randint(300,359)
    # Making the Ball White in color 
    pixels[userLocation] = white
    # Send pixel information/properties for display
    client.put_pixels(pixels)
    # Decides whether the game is running or not
    GameRunning = True
# Handles arrow up press
def goAbove():
    # To access outer variables in the function
    global pixels,userLocation,client
    # Tries to execute statements without exceptions
    try:
        # Makes the previous location of the White ball to black
        pixels[userLocation] = black
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        # Makes the ball go one row above
        userLocation -= 60
        # Make the current position to "white"
        pixels[userLocation] = white
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        return
    # Exception Handler
    except:
        # Brings the Ball to the bottom row
        userLocation += 360
        # Makes the current location to white
        pixels[userLocation] = white
        # Send pixel information/properties for display
        client.put_pixels(pixels)
# Keyboard input handler to go up with either the "Up arrow" key Or "W" key
keyboard.add_hotkey('up', goAbove)
keyboard.add_hotkey('w', goAbove)
# Handles arrow down press
def goBelow():
    # To access outer variables in the function
    global pixels,userLocation,client
    # Tries to execute statements without exceptions
    try:
        # Makes the previous location of the White ball to black
        pixels[userLocation] = black
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        # Makes the ball go one row above
        userLocation += 60
        # Make the current position to "white"
        pixels[userLocation] = white
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        return
    # Exception Handler
    except:
        # Brings the Ball to the top row
        userLocation -= 360
        # Makes the current location to white
        pixels[userLocation] = white
        # Send pixel information/properties for display
        client.put_pixels(pixels)
# Keyboard input handler to go up with either the "Down arrow" key Or "S" key        
keyboard.add_hotkey('s', goBelow)
keyboard.add_hotkey('down', goBelow)
# Handles arrow left press
def goLeft():
    # To access outer variables in the function
    global pixels,userLocation,client
    # Tries to execute statements without exception
    try:
        # Makes the previous location of the White ball to black
        pixels[userLocation] = black
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        # Moves the Ball LED to the left
        userLocation -= 1
        # Make the current position to "white"
        pixels[userLocation] = white
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        return
    # Exception Handler
    except:
        # Moves the Ball LED to the right
        userLocation += 1
        # Makes the current location to white
        pixels[userLocation] = white
        # Send pixel information/properties for display
        client.put_pixels(pixels)
# Keyboard input handler to go up with either the "Left arrow" key Or "A" key        
keyboard.add_hotkey('a', goLeft)
keyboard.add_hotkey('left', goLeft)
# Handles arrow right press
def goRight():
    # To access outer variables in the function
    global pixels,userLocation,client
    # Tries to execute statements without exception
    try:
        # Tries to execute statements without exception
        pixels[userLocation] = black
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        # Moves the Ball LED to the right
        userLocation += 1
        # Make the current position to "white"
        pixels[userLocation] = white
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        return
    # Exception Handler
    except:
        # Moves the Ball LED to the left
        userLocation -= 1
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        # Makes the current location to white
        pixels[userLocation] = white
# Keyboard input handler to go up with either the "Right arrow" key Or "D" key        
keyboard.add_hotkey('d', goRight)
keyboard.add_hotkey('right', goRight)
# Shows the "GAME OVER" screen
def EndGame():
    # To access outer variables in the function
    global pixels, red, black, green, GameRunning
    # Stops the game from running 
    GameRunning = False
    # Initialize 0 for loop control
    exitCounter = 0
    # Run Loop / Show Game Over Text with Strobe Effects for 4 Seconds
    while exitCounter < 4:
        # Reset all pixels to Black / Null
        pixels = [ black ] * 360
        client.put_pixels(pixels)
        time.sleep(0.1)
        # Lighting up Indivuals LEDs to display Game Over Message
        # Letter G
        pixels[1] = red
        pixels[2] = red
        pixels[3] = red
        pixels[4] = red
        pixels[5] = red
        pixels[6] = red
        pixels[61] = red
        pixels[121] = red
        pixels[123] = red
        pixels[124] = red
        pixels[125] = red
        pixels[126] = red
        pixels[181] = red
        pixels[186] = red
        pixels[241] = red
        pixels[246] = red
        pixels[301] = red
        pixels[302] = red
        pixels[303] = red
        pixels[304] = red
        pixels[305] = red
        pixels[306] = red

        # Letter A

        pixels[8] = green
        pixels[9] = green
        pixels[10] = green
        pixels[11] = green
        pixels[12] = green
        pixels[13] = green
        pixels[68] = green
        pixels[73] = green
        pixels[128] = green
        pixels[133] = green
        pixels[188] = green
        pixels[189] = green
        pixels[190] = green
        pixels[191] = green
        pixels[192] = green
        pixels[193] = green
        pixels[248] = green
        pixels[253] = green
        pixels[308] = green
        pixels[313] = green


        # Letter  M

        pixels[15] = red
        pixels[16] = red
        pixels[19] = red
        pixels[20] = red
        pixels[75] = red
        pixels[77] = red
        pixels[78] = red
        pixels[80] = red
        pixels[135] = red
        pixels[137] = red
        pixels[138] = red
        pixels[140] = red
        pixels[195] = red
        pixels[197] = red
        pixels[198] = red
        pixels[200] = red
        pixels[255] = red
        pixels[260] = red
        pixels[315] = red
        pixels[320] = red


        # Letter E

        pixels[22] = green
        pixels[23] = green
        pixels[24] = green
        pixels[25] = green
        pixels[26] = green
        pixels[27] = green
        pixels[82] = green
        pixels[83] = green
        pixels[142] = green
        pixels[143] = green
        pixels[144] = green
        pixels[145] = green
        pixels[202] = green
        pixels[203] = green
        pixels[204] = green
        pixels[205] = green
        pixels[248] = green
        pixels[262] = green
        pixels[263] = green
        pixels[322] = green
        pixels[323] = green
        pixels[324] = green
        pixels[325] = green
        pixels[326] = green
        pixels[327] = green

        # Letter O


        pixels[33] = red
        pixels[34] = red
        pixels[35] = red
        pixels[36] = red
        pixels[37] = red
        pixels[38] = red
        pixels[93] = red
        pixels[98] = red
        pixels[153] = red
        pixels[158] = red
        pixels[213] = red
        pixels[218] = red
        pixels[273] = red
        pixels[278] = red
        pixels[333] = red
        pixels[334] = red
        pixels[335] = red
        pixels[336] = red
        pixels[337] = red
        pixels[338] = red


        # Letter V

        pixels[40] = green
        pixels[45] = green
        pixels[100] = green
        pixels[105] = green
        pixels[160] = green
        pixels[165] = green
        pixels[220] = green
        pixels[225] = green
        pixels[281] = green
        pixels[284] = green
        pixels[342] = green
        pixels[343] = green

        # Letter E

        pixels[47] = red
        pixels[48] = red
        pixels[49] = red
        pixels[50] = red
        pixels[51] = red
        pixels[52] = red
        pixels[107] = red
        pixels[108] = red
        pixels[167] = red
        pixels[168] = red
        pixels[169] = red
        pixels[170] = red
        pixels[227] = red
        pixels[228] = red
        pixels[229] = red
        pixels[230] = red
        pixels[287] = red
        pixels[288] = red
        pixels[347] = red
        pixels[348] = red
        pixels[349] = red
        pixels[350] = red
        pixels[351] = red
        pixels[352] = red

        # Letter R

        pixels[54] = green
        pixels[55] = green
        pixels[56] = green
        pixels[57] = green
        pixels[58] = green
        pixels[59] = green
        pixels[114] = green
        pixels[119] = green
        pixels[174] = green
        pixels[175] = green
        pixels[176] = green
        pixels[177] = green
        pixels[178] = green
        pixels[179] = green
        pixels[234] = green
        pixels[237] = green
        pixels[294] = green
        pixels[298] = green
        pixels[354] = green
        pixels[359] = green
        client.put_pixels(pixels)
        time.sleep(0.1)
        exitCounter += 0.2
    # Kill Thread / Exit Game
    sys.exit(0)

# Intruders Row 1 Animation
def Row1():
    # Access Outer Variables inside Function
    global GameRunning
    # Run until White Ball is away from Intruder balls
    while GameRunning:
        for i in range(59, 0, -1):
            # Checks if the White Ball is on the Current Position from the given range above
            if i == userLocation-1:
                pixels[i+1] = white
                # Send pixel information/properties for display
                client.put_pixels(pixels)
                # Start Game Over Sequence
                EndGame()
                # Kill this Thread
                sys.exit(0)
            # Move Ball to Next Position with Random Colours
            pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            # Reset Last Pixel
            pixels[i+1] = (0, 0, 0)
            # Send pixel information/properties for display
            client.put_pixels(pixels)
            # The time paused to give strobe effect
            time.sleep(0.05)
# Intruders Row 2 Animation            
def Row2():
    # Access Outer Variables inside Function
    global GameRunning
    # Run until White Ball is away from Intruder balls
    while GameRunning:
        for i in range(60, 119):
            # Checks if the White Ball is on the Current Position from the given range above
            if i == userLocation+1:
                pixels[i-1] = white
                # Send pixel information/properties for display
                client.put_pixels(pixels)
                # Start Game Over Sequence
                EndGame()
                # Kill this Thread
                sys.exit(0)
            # Move Ball to Next Position with Random Colours
            pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            # Reset Last Pixel
            pixels[i-1] = (0, 0, 0)
            # Send pixel information/properties for display
            client.put_pixels(pixels)
            # The time paused to give strobe effect
            time.sleep(0.05)
# Intruders Row 3 Animation            
def Row3():
    # Access Outer Variables inside Function
    global GameRunning
    # Run until White Ball is away from Intruder balls
    while GameRunning:
        for i in range(179, 120, -1):
            # Checks if the White Ball is on the Current Position from the given range above
            if i == userLocation-1:
                pixels[i+1] = white
                # Send pixel information/properties for display
                client.put_pixels(pixels)
                # Start Game Over Sequence
                EndGame()
                # Kill this Thread
                sys.exit(0)
            # Move Ball to Next Position with Random Colours     
            pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            # Reset Last Pixel      
            pixels[i+1] = (0, 0, 0)
            # Send pixel information/properties for display
            client.put_pixels(pixels)
            # The time paused to give strobe effect
            time.sleep(0.05)
# Intruders Row 4 Animation              
def Row4():
    # Access Outer Variables inside Function
    global GameRunning
    # Run until White Ball is away from Intruder balls
    while GameRunning:
        for i in range(180, 239):
            # Checks if the White Ball is on the Current Position from the given range above
            if i == userLocation+1:
                pixels[i-1] = white
                # Send pixel information/properties for display
                client.put_pixels(pixels)
                # Start Game Over Sequence
                EndGame()
                # Kill this Thread
                sys.exit(0)
            # Move Ball to Next Position with Random Colours    
            pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            # Reset Last Pixel
            pixels[i-1] = (0, 0, 0)
            # Send pixel information/properties for display
            client.put_pixels(pixels)
            # The time paused to give strobe effect
            time.sleep(0.05)
# Intruders Row 5 Animation              
def Row5():
    # Access Outer Variables inside Function
    global GameRunning
    # Run until White Ball is away from Intruder balls
    while GameRunning:
        for i in range(299, 240, -1):
            # Checks if the White Ball is on the Current Position from the given range above
            if i == userLocation-1:
                pixels[i+1] = white
                # Send pixel information/properties for display
                client.put_pixels(pixels)
                # Start Game Over Sequence
                EndGame()
                # Kill this Thread
                sys.exit(0)
            # Move Ball to Next Position with Random Colours        
            pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            # Reset Last Pixel
            pixels[i+1] = (0, 0, 0)
            # Send pixel information/properties for display
            client.put_pixels(pixels)
            # The time paused to give strobe effect
            time.sleep(0.05)
# Intruders Row 6 Animation              
def Row6():
# Access Outer Variables inside Function    
    global GameRunning
 # Run until White Ball is away from Intruder balls    
    while GameRunning:
        for i in range(300, 359):
            # Checks if the White Ball is on the Current Position from the given range above
            if i == userLocation+1:
                pixels[i-1] = white
                # Send pixel information/properties for display
                client.put_pixels(pixels)
                # Start Game Over Sequence
                EndGame()
                # Kill this Thread
                sys.exit(0)
            pixels[i] = (255, 0, 0)
            pixels[i-1] = black
            # Send pixel information/properties for display
            client.put_pixels(pixels)
            # The time paused to give strobe effect
            time.sleep(0.05)
            
# Handles the Start Sequence of the Game
def StartGame():
    global threading
    # Resets all Variables for Restart of the game
    initGame()
    # Threading for simultanious loop runs 
    threading.Thread(target=Row1).start()
    threading.Thread(target=Row2).start()
    threading.Thread(target=Row3).start()
    threading.Thread(target=Row4).start()
    threading.Thread(target=Row5).start()
    # Wait Before Running More Intruders
    time.sleep(1.2)
    # Threading for simultanious loop runs 
    threading.Thread(target=Row1).start()
    threading.Thread(target=Row2).start()
    threading.Thread(target=Row3).start()
    threading.Thread(target=Row4).start()
    threading.Thread(target=Row5).start()
    # Wait Before Running Row 6 Intruders
    time.sleep(1)
    # Threading for simultanious loop runs 
    threading.Thread(target=Row6).start()
    # Wait Before Running Row 6 Intruders
    time.sleep(1.2)
    # Threading for simultanious loop runs
    threading.Thread(target=Row6).start()
