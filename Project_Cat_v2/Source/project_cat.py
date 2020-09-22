# Author: Andrew Gair
# Date: September 2020
# Purpose: Main code. Creates GUI for collecting user input,
#          also creates output file based on Subject-Number
#          and places user responses into said output file.

# My own Python module designed for simple file input/output.
import fileIO

# My own Python class containing methods that are activated on button press.
import uiEvents

# tkinter is used for all UI elements.
from tkinter import *


#-- Global Variables --#
FileName = ""             # The name of the output file (will be named after subject-number).
MaxTrials = 0             # The total number of trials user will complete.
StartupComplete = "false" # Used to verify if setup data was entered properly.
DebugFlag = "false"       # Used to determine if image-names should appear during program execution.


# Function that gathers data from the Startup-UI created later
# All data gathered is placed into output file using 'fileIO' module
def Startup(DebugSet):
  global FileName, MaxTrials, StartupComplete, DebugFlag
  SubjectNumber = ParticipantNumber.get()
  SubjectGender = Gender.get()
  MaxTrials = TrialNumber.get()
  
  if len(SubjectNumber) > 2: # Simple error checking based on input length.
  
    if len(SubjectGender) > 0:
    
      if len(MaxTrials) > 0:
        FileName = "..//Output_Files//" + SubjectNumber + ".txt"
        FileHandle = open(FileName, "w+") # Open file for [W]rite. If no file available, [+]create one
        FileHandle.write("Subject Number: " + SubjectNumber + "\n" + "Subject Gender: " + SubjectGender + "\n" + "Max Trials: " + MaxTrials + "\n" + "\n\nFormat is: [Image code], [Subject selected category], [Subject response time (seconds)]\n\n" + "Phase 1:\n")
        FileHandle.close()
        StartupComplete = "true"
        StartupGUI.destroy()
        DebugFlag = DebugSet
      else:
        print("Max Trials input was invalid, program exiting\n")
        StartupGUI.destroy()
        sys.exit()
        
    else:
      print("Subject Gender input was invalid, program exiting\n")
      StartupGUI.destroy()
      sys.exit()
      
  else:
    print("Subject Number input was invalid, program exiting\n")
    StartupGUI.destroy()
    sys.exit()

#----
# Program Start

#---- Create Startup-UI to gather simple user information
StartupGUI = Tk()
StartupGUI.title('Startup-Menu')

# UI for gathering a participant number.
ParticipantTitle = Label(StartupGUI, text="Participant Number:")
ParticipantTitle.grid(row=1, column=0, sticky=E)
ParticipantNumber = Entry(StartupGUI)
ParticipantNumber.grid(row=1, column=1)
ParticipantNumber.focus_set()

# UI for gathering participant's gender.
GenderTitle = Label(StartupGUI, text="Gender:")
GenderTitle.grid(row=2, column=0, sticky=E)
Gender = Entry(StartupGUI)
Gender.grid(row=2, column=1)

# UI for customizing how many trials participant will face.
TrialTitle = Label(StartupGUI, text="Phase 1 Trials:")
TrialTitle.grid(row=3, column=0, sticky=E)
TrialNumber = Entry(StartupGUI)
TrialNumber.grid(row=3, column=1)

# On pressing 'Go' launch the function 'Startup' and proceed with program.
GoButton = Button(StartupGUI, text="Go", command=lambda: Startup("false"))
GoButton.grid(row=4, column=0, sticky=W+E)

# Does same thing as 'Go' button, but launches with image-names visisble.
DebugButton = Button(StartupGUI, text="Go with Debug", command=lambda: Startup("true"))
DebugButton.grid(row=4, column=1, sticky=W+E)

StartupGUI.mainloop()

#---- End Startup-UI section

# Initialize the class 'myEvents' using the imported class 'uiEvents'.
myEvents = uiEvents.events(FileName, MaxTrials, DebugFlag)

# If Startup interface failed (perhaps due to bad user input) exit program
if StartupComplete != "true":
  sys.exit()
else:
  #----
  # Start introduction section
  myEvents.CreateIntro_1()
  myEvents.CreateIntro_2()
  # End introduction section
  #----

  #----
  # Start main section
  myEvents.StartPhaseOne()
  
  if myEvents.GoodbyeSet == "true":
    myEvents.SayGoodbye() # Only runs once StartPhaseOne() has concluded
  # End main section
  #----

# Program End
#----
