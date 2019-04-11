# Import system modules and custom libraries
import opc, time, sys, threading, BootInformationDisplay

# Define "Start" as a function which can be called at any time 
def Start():
    # Run B3 as a thread function
    s3 = threading.Thread(target=BootInformationDisplay.B3)
    # Starts B3 Thread
    s3.start()
    # Delay the next statment's execusion 
    time.sleep(1)
    # Run B2 as a thread function
    s2 = threading.Thread(target=BootInformationDisplay.B2)
    # Starts B2 Thread
    s2.start()
    # Delay the next statment's execusion
    time.sleep(1)
    # Run B1 as a thread function
    s1 = threading.Thread(target=BootInformationDisplay.B1)
    # Starts B1 Thread
    s1.start()
    # Delay the next statment's execusion
    time.sleep(1)
    # Run Go as a thread function
    s4 = threading.Thread(target=BootInformationDisplay.Go)
    # Starts Go Thread
    s4.start()
