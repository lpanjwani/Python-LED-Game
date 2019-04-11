# Import system modules and custom libraries
import opc, time, sys

# number of LEDs on the board
numLEDs = 360
# Server address and port
client = opc.Client('localhost:7890')

# Predefined color values
red = (255,0,0)
black = (0,0,0)
white = (255, 255, 255)
yellow = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
# Initialize all pixels as "black"
pixels = [ black ] * numLEDs
# Send pixel information/properties for display
client.put_pixels(pixels)
# Light up LEDs to show the number "3"
def B3():
    # To access outer variables in the function
    global pixels, red, black
    # To control the timing of the loop
    runCounter=0
    # Redo the process until the run counter is less then 1 using while loop
    while runCounter < 1:
        # Set specified/Selected LEDs to red
        pixels[1] = red
        pixels[2] = red
        pixels[3] = red
        pixels[4] = red
        pixels[5] = red
        pixels[6] = red
        pixels[7] = red
        pixels[8] = red
        pixels[9] = red
        pixels[10] = red
        pixels[11] = red
        pixels[12] = red
        pixels[13] = red
        pixels[14] = red
        pixels[61] = red
        pixels[62] = red
        pixels[73] = red
        pixels[74] = red
        pixels[130] = red
        pixels[131] = red
        pixels[132] = red
        pixels[133] = red
        pixels[134] = red
        pixels[190] = red
        pixels[191] = red
        pixels[192] = red
        pixels[193] = red
        pixels[194] = red
        pixels[241] = red
        pixels[242] = red
        pixels[253] = red
        pixels[254] = red
        pixels[301] = red
        pixels[302] = red
        pixels[302] = red
        pixels[303] = red
        pixels[303] = red
        pixels[304] = red
        pixels[305] = red
        pixels[306] = red
        pixels[307] = red
        pixels[308] = red
        pixels[309] = red
        pixels[310] = red
        pixels[311] = red
        pixels[312] = red
        pixels[313] = red
        pixels[314] = red
        # Sends the above values to the client
        client.put_pixels(pixels)
        # The time paused to give strobe effect
        time.sleep(0.1)
        #  Initialize all pixels as "black"
        pixels = [ black ] * numLEDs
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        # The time paused to give strobe effect
        time.sleep(0.1)
        # Increment 0.2 for loop control
        runCounter += 0.2
# Light up LEDs to show the number "2"         
def B2():
    # To access outer variables in the function
    global pixels, red, white
    # To control the timing of the loop
    runCounter = 0
    # Redo the process until the run counter is less then 1 using while loop
    while runCounter < 1:
        # Set specified/Selected LEDs to White
        pixels[24] = white
        pixels[25] = white
        pixels[26] = white
        pixels[27] = white
        pixels[28] = white
        pixels[29] = white
        pixels[30] = white
        pixels[31] = white
        pixels[32] = white
        pixels[33] = white
        pixels[34] = white
        pixels[35] = white
        pixels[36] = white
        pixels[37] = white
        pixels[96] = white
        pixels[97] = white
        pixels[144] = white
        pixels[145] = white
        pixels[146] = white
        pixels[147] = white
        pixels[148] = white
        pixels[149] = white
        pixels[150] = white
        pixels[151] = white
        pixels[152] = white
        pixels[153] = white
        pixels[154] = white
        pixels[155] = white
        pixels[156] = white
        pixels[157] = white
        pixels[204] = white
        pixels[205] = white
        pixels[264] = white
        pixels[265] = white
        pixels[324] = white
        pixels[325] = white
        pixels[326] = white
        pixels[327] = white
        pixels[328] = white
        pixels[329] = white
        pixels[330] = white
        pixels[331] = white
        pixels[332] = white
        pixels[333] = white
        pixels[334] = white
        pixels[335] = white
        pixels[336] = white
        pixels[337] = white
        # Sends the above values to the client
        client.put_pixels(pixels)
        # Wait for some time to give strobe effect
        time.sleep(0.1)
        #  Initialize all pixels as "black"
        pixels = [ black ] * numLEDs
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        # The time paused to give strobe effect
        time.sleep(0.1)
        # Increment 0.2 for loop control
        runCounter += 0.2
# Light up LEDs to show the number "1"  
def B1():
    # To access outer variables in the function
    global pixels, red, yellow
    # To control the timing of the loop
    runCounter = 0
    # Redo the process until the run counter is less then 1 using while loop
    while runCounter < 1:
        # Set specified/Selected LEDs to Yellow
        pixels[50] = yellow
        pixels[51] = yellow
        pixels[52] = yellow
        pixels[53] = yellow
        pixels[54] = yellow
        pixels[55] = yellow
        pixels[56] = yellow
        pixels[109] = yellow
        pixels[110] = yellow
        pixels[115] = yellow
        pixels[116] = yellow
        pixels[168] = yellow
        pixels[169] = yellow
        pixels[175] = yellow
        pixels[176] = yellow
        pixels[235] = yellow
        pixels[236] = yellow
        pixels[295] = yellow
        pixels[296] = yellow
        pixels[347] = yellow
        pixels[348] = yellow
        pixels[349] = yellow
        pixels[350] = yellow
        pixels[351] = yellow
        pixels[352] = yellow
        pixels[353] = yellow
        pixels[354] = yellow
        pixels[355] = yellow
        pixels[356] = yellow
        pixels[357] = yellow
        pixels[358] = yellow
        pixels[359] = yellow
        # Sends the above values to the client
        client.put_pixels(pixels)
        # Wait for some time to give strobe effect
        time.sleep(0.1)
        #  Initialize all pixels as "black"
        pixels = [ black ] * numLEDs
        # Send pixel information/properties for display
        client.put_pixels(pixels)
         # The time paused to give strobe effect
        time.sleep(0.1)
        # Increment 0.2 for loop control
        runCounter += 0.2
# Light up LEDs to show the word "GO"         
def Go():
    # To access outer variables in the function   
    global green,black,pixels
    # To control the timing of the loop
    runCounter = 0
    # Redo the process until the run counter is less then 2 using while loop
    while runCounter < 2:
        # Set specified/Selected LEDs to Green
        pixels[16] = green
        pixels[17] = green
        pixels[18] = green
        pixels[19] = green
        pixels[20] = green
        pixels[21] = green
        pixels[22] = green
        pixels[23] = green
        pixels[24] = green
        pixels[25] = green
        pixels[26] = green
        pixels[27] = green
        pixels[28] = green
        pixels[29] = green
        pixels[76] = green
        pixels[77] = green
        pixels[78] = green
        pixels[79] = green
        pixels[80] = green
        pixels[81] = green
        pixels[82] = green
        pixels[83] = green
        pixels[84] = green
        pixels[85] = green
        pixels[86] = green
        pixels[87] = green
        pixels[88] = green
        pixels[89] = green
        pixels[136] = green
        pixels[137] = green
        pixels[138] = green
        pixels[196] = green
        pixels[197] = green
        pixels[198] = green
        pixels[207] = green
        pixels[208] = green
        pixels[209] = green
        pixels[256] = green
        pixels[257] = green
        pixels[258] = green
        pixels[259] = green
        pixels[260] = green
        pixels[261] = green
        pixels[262] = green
        pixels[263] = green
        pixels[264] = green
        pixels[265] = green
        pixels[266] = green
        pixels[267] = green
        pixels[268] = green
        pixels[269] = green
        pixels[265] = green
        pixels[266] = green
        pixels[267] = green
        pixels[268] = green
        pixels[269] = green
        pixels[316] = green
        pixels[317] = green
        pixels[318] = green
        pixels[319] = green
        pixels[320] = green
        pixels[321] = green
        pixels[322] = green
        pixels[323] = green
        pixels[324] = green
        pixels[325] = green
        pixels[326] = green
        pixels[327] = green
        pixels[328] = green
        pixels[329] = green
        pixels[32] = green
        pixels[33] = green
        pixels[34] = green
        pixels[35] = green
        pixels[36] = green
        pixels[37] = green
        pixels[38] = green
        pixels[39] = green
        pixels[40] = green
        pixels[41] = green
        pixels[42] = green
        pixels[43] = green
        pixels[44] = green
        pixels[45] = green
        pixels[92] = green
        pixels[93] = green
        pixels[94] = green
        pixels[95] = green
        pixels[96] = green
        pixels[97] = green
        pixels[98] = green
        pixels[99] = green
        pixels[100] = green
        pixels[101] = green
        pixels[102] = green
        pixels[103] = green
        pixels[104] = green
        pixels[105] = green
        pixels[152] = green
        pixels[153] = green
        pixels[154] = green
        pixels[163] = green
        pixels[164] = green
        pixels[165] = green
        pixels[212] = green
        pixels[213] = green
        pixels[214] = green
        pixels[223] = green
        pixels[224] = green
        pixels[225] = green
        pixels[272] = green
        pixels[273] = green
        pixels[274] = green
        pixels[275] = green
        pixels[276] = green
        pixels[277] = green
        pixels[278] = green
        pixels[279] = green
        pixels[280] = green
        pixels[281] = green
        pixels[282] = green
        pixels[283] = green
        pixels[284] = green
        pixels[285] = green
        pixels[332] = green
        pixels[333] = green
        pixels[334] = green
        pixels[335] = green
        pixels[336] = green
        pixels[337] = green
        pixels[338] = green
        pixels[339] = green
        pixels[340] = green
        pixels[341] = green
        pixels[342] = green
        pixels[343] = green
        pixels[344] = green
        pixels[345] = green
        # Sends the above values to the client
        client.put_pixels(pixels)
        # Wait for some time to give strobe effect
        time.sleep(0.1)
        #  Initialize all pixels as "black"
        pixels = [ black ] * numLEDs
        # Send pixel information/properties for display
        client.put_pixels(pixels)
        # The time paused to give strobe effect
        time.sleep(0.5)
        # Increment 0.6 for loop control
        runCounter += 0.6
