# Author: Andrew Gair
# Date: September 2020
# Purpose: All UI related methods are stored in this class.

# My own Python module designed for simple file input/output.
import fileIO

# For using sleep commands and other time-related activities.
import time

# For using random().
import random

# tkinter is used for all UI elements.
from tkinter import *

# For opening .png images in tkinter.
from PIL import Image, ImageTk

# For playing .wav file sound effects.
from playsound import playsound

class events:

  # Class constructor. Initialize some variables.
  def __init__(self, FileName, MaxTrials, DebugFlag):
    self.FileName = FileName      # The name of the file to store output data to.
    self.StartTime = time.time()  # Used to track how long user took to press button.
    self.MaxTrials = MaxTrials    # Counts the max number of trials before experiement ends.
    self.TrialNumber = 0          # Tracks how many images user has seen so far.
    self.Category3Count = 0       # Tracks how many Category3 images user has seen so far.
    self.CurrentGroup = 0         # Tracks which category the image was taken from.
    self.PreviousImage = "0000"   # Tracks which image was shown previously so user doesn't see the same one back-to-back.
    self.ImageDisplay = None      # Different methods will change which image is displayed in this Label.
    self.Debug = None             # Different methods will change what text is displayed in this label.
    self.MainUI = None            # Different methods will destroy and recreate the MainUI element.
    self.GoodbyeSet = "false"     # Tells the program when phase 2 should end and program should terminate.
    self.TestGroup = "false"      # Determines whether or not user can see images from the test group.
    self.DebugMode = DebugFlag    # DebugMode turns on image names for easy correct/incorrect categorization.

#----
# Categorization related methods:
#----
  # When the user sorts the image into 'Category 1' during phase 1 of project
  #   The time taken to press a button is tracked, if the user takes too long to
  #   make a selection than the results will be discarded later during data analysis.
  def CategoryOne_P1(self):
    ButtonTime = time.time() - self.StartTime
    String_ButtonTime = str(ButtonTime)
    fileIO.WriteToFile(self.FileName, "1 " + String_ButtonTime[:1])
    fileIO.AddNewLine(self.FileName)
    if self.CurrentGroup == 1:
      playsound('..//Input_Files//Sound_Effects//Correct.wav')
    else:
      playsound('..//Input_Files//Sound_Effects//Incorrect.wav')
    time.sleep(0.5)
    self.NextImage_P1()
    self.StartTime = time.time()
    

  # When the user sorts the image into 'Category 2' during phase 1 of project
  def CategoryTwo_P1(self):
    ButtonTime = time.time() - self.StartTime
    String_ButtonTime = str(ButtonTime)
    fileIO.WriteToFile(self.FileName, "2 " + String_ButtonTime[:1])
    fileIO.AddNewLine(self.FileName)
    if self.CurrentGroup == 2:
      playsound('..//Input_Files//Sound_Effects//Correct.wav')
    else:
      playsound('..//Input_Files//Sound_Effects//Incorrect.wav')
    time.sleep(0.5)
    self.NextImage_P1()
    self.StartTime = time.time()
    

  # When the user sorts the image into 'Category 1' during phase 2 of project
  def CategoryOne_P2(self):
    ButtonTime = time.time() - self.StartTime
    String_ButtonTime = str(ButtonTime)
    fileIO.WriteToFile(self.FileName, "1 " + String_ButtonTime[:1])
    fileIO.AddNewLine(self.FileName)
    time.sleep(0.75)
    if self.Category3Count == 6: # 6 being the number of group_test items
      self.GoodbyeSet = "true"
      self.MainUI.destroy()
    else:
      self.NextImage_P2()
      self.StartTime = time.time()
      

  # When the user sorts the image into 'Category 2' during phase 2 of project
  def CategoryTwo_P2(self):
    ButtonTime = time.time() - self.StartTime
    String_ButtonTime = str(ButtonTime)
    fileIO.WriteToFile(self.FileName, "2 " + String_ButtonTime[:1])
    fileIO.AddNewLine(self.FileName)
    time.sleep(0.75)
    if self.Category3Count == 6: # 6 being the number of group_test items
      self.GoodbyeSet = "true"
      self.MainUI.destroy()
    else:
      self.NextImage_P2()
      self.StartTime = time.time()

  # The following methods each return a randomly chosen number from the list given.
  # This determines which image will be shown to the user.
  def PickGroupOne(self):
    AllOptions = [1113,1114,1131,1141,1311,1411,3111,4111]
    return random.choice(AllOptions)
  def PickGroupTwo(self):
    AllOptions = [2233,2234,2243,2244,2323,2324,2332,2342,2423,2424,2432,2442,3223,3224,3232,3242,3322,3422,4223,4224,4232,4242,4322,4422]
    return random.choice(AllOptions)
    
  # Returns a number from the list, but not randomly. The returned value will
  # instead be incremented through the list, so the order in which these test-group
  # images are shown is not randomized.
  def PickGroupTest(self):
    AllOptions = [1122,1212,1221,2112,2121,2211]
    return AllOptions[self.Category3Count]


#----
# Image selected related methods:
#----
  # Shows an initial image for phase 1
  def InitialImage_P1(self):
    NewGroup = random.choice([1,2])
    if NewGroup == 1:
      self.CurrentGroup = 1
      ChosenImage = str(self.PickGroupOne())
      fileIO.WriteToFile(self.FileName, ChosenImage + " ")
      return "Group_1//" + ChosenImage
    else:
      self.CurrentGroup = 2
      ChosenImage = str(self.PickGroupTwo())
      fileIO.WriteToFile(self.FileName, ChosenImage + " ")
      return "Group_2//" + ChosenImage


  # Shows an initial image for phase 2
  def InitialImage_P2(self):
    NewGroup = random.choice([1,2,3])
    if NewGroup == 1:
      self.CurrentGroup = 1
      ChosenImage = str(self.PickGroupOne())
      fileIO.WriteToFile(self.FileName, ChosenImage + " ")
      return "Group_1//" + ChosenImage
      
    elif NewGroup == 2:
      self.CurrentGroup = 2
      ChosenImage = str(self.PickGroupTwo())
      fileIO.WriteToFile(self.FileName, ChosenImage + " ")
      return "Group_2//" + ChosenImage
      
    else:
      self.CurrentGroup = 3
      ChosenImage = str(self.PickGroupTest())
      fileIO.WriteToFile(self.FileName, ChosenImage + " ")
      return "Group_Test//" + ChosenImage


  # Once user has pressed either button and categorized the image in front of them, the program
  # needs to select a new image for the user to view.
  # Which image gets shown to the user is random, but also depends upon which phase of the
  # experiment the user is in. If the user is still in 'training' then they cannot be shown
  # any images from Group_Test. Hence this function is called NextImage_P1, for 'phase 1' (training)
  def NextImage_P1(self):
    if self.TrialNumber < int(self.MaxTrials) -1:
      NewGroup = random.choice([1,2])
      if NewGroup == 1:
        self.CurrentGroup = 1
        NewImage = self.PickGroupOne()
        if NewImage == self.PreviousImage: # If image would be the same back-to-back, then look in other category.
          self.CurrentGroup = 2
          NewImage = self.PickGroupTwo()
          ImageLoad = Image.open("..//Input_Files//Group_2//" + str(NewImage) + ".png")
        else:
          ImageLoad = Image.open("..//Input_Files//Group_1//" + str(NewImage) + ".png")

      else: # elif NewGroup == 2:
        self.CurrentGroup = 2
        NewImage = self.PickGroupTwo()
        if NewImage == self.PreviousImage: # If image would be the same back-to-back, then look in other category.
          self.CurrentGroup = 1
          NewImage = self.PickGroupOne()
          ImageLoad = Image.open("..//Input_Files//Group_1//" + str(NewImage) + ".png")
        else:
          ImageLoad = Image.open("..//Input_Files//Group_2//" + str(NewImage) + ".png")
          
      self.PreviousImage = NewImage
      fileIO.WriteToFile(self.FileName, str(NewImage)+" ")
      ImageRender = ImageTk.PhotoImage(ImageLoad)
      self.ImageDisplay.configure(image = ImageRender)
      self.ImageDisplay.image = ImageRender
      if self.DebugMode == "true":
        self.Debug.configure(text = "Image name: Group_"+str(self.CurrentGroup)+"//"+str(NewImage))
      self.TrialNumber += 1
      
    else: # elif self.TrialNumber >= int(self.MaxTrials)-1:
      fileIO.WriteToFile(self.FileName, "Phase 2:")
      fileIO.AddNewLine(self.FileName)
      self.PauseScreenSet = "true"
      self.MainUI.destroy()
      self.StartPhaseTwo()


  # When the user enters phase 2, they will sometimes see a 'test-group' image.
  # Images from the test-group should not be shown back-to-back, and so there is
  # a boolean variable 'TestGroup' that toggles whether or not the user can
  # see any of these test-group images.
  def NextImage_P2(self):
    if self.TestGroup == "true":
      NewGroup = random.choice([1,2,3])
    else:
      NewGroup = random.choice([1,2])
      self.TestGroup = "true"
    
    if NewGroup == 3: # Show the user an image from the test-group
      self.TestGroup = "false" # Prevent back-to-back showings
      NewImage = self.PickGroupTest()
      ImageLoad = Image.open("..//Input_Files//Group_Test//" + str(NewImage) + ".png")
      self.PreviousImage = NewImage
      self.Category3Count += 1
      fileIO.WriteToFile(self.FileName, str(NewImage)+" ")
      ImageRender = ImageTk.PhotoImage(ImageLoad)
      self.ImageDisplay.configure(image = ImageRender)
      self.ImageDisplay.image = ImageRender
      if self.DebugMode == "true":
        self.Debug.configure(text = "Image name: Group_Test//"+str(NewImage))
      
    else: # Otherwise show an image from either category 1 or 2, doesn't matter
      self.TrialNumber = 0 # TrialNumber doesn't matter when in phase 2
      self.NextImage_P1()


#----
# UI related methods:
#----
  # Shows user a sample of what a category 1 image looks like.
  # Automatically destroys itself after set period.
  def CreateIntro_1(self):
    Intro_1 = Tk()
    Intro_1.attributes('-zoomed', True)
    Intro_1.title("Introduction")
  
    ImageLoad = Image.open("..//Input_Files//1111_example.png")
    ImageRender = ImageTk.PhotoImage(ImageLoad)
   
    ExplainLabel = Label(Intro_1, image=ImageRender)
    ExplainLabel.image = ImageRender
    ExplainLabel.grid(row=0, column=0)
  
    ImageDescription = Label(Intro_1, text="Example of Category 1 image")
    ImageDescription.grid(row=1, column=0)
    ImageDescription.config(font=("Courier", 44))
      
    Intro_1.after(1000, lambda: Intro_1.destroy()) #        <--------------------CHANGE TO 30000
    Intro_1.mainloop()


  # Shows user a sample of what a category 2 image looks like.
  # Automatically destroys itself after set period.
  def CreateIntro_2(self):
    Intro_2 = Tk()
    Intro_2.attributes('-zoomed', True)
    Intro_2.title("Introduction")
    
    ImageLoad = Image.open("..//Input_Files//2222_example.png")
    ImageRender = ImageTk.PhotoImage(ImageLoad)
   
    ExplainLabel = Label(Intro_2, image=ImageRender)
    ExplainLabel.image = ImageRender
    ExplainLabel.grid(row=0, column=0)
  
    ImageDescription = Label(Intro_2, text="Example of Category 2 image")
    ImageDescription.grid(row=1, column=0)
    ImageDescription.config(font=("Courier", 44))
      
    Intro_2.after(1000, lambda: Intro_2.destroy()) #        <--------------------CHANGE TO 30000
    Intro_2.mainloop()


  # Begins the first phase, user will hear a sound effect based on if their answer
  # was correct or incorrect.
  def StartPhaseOne(self):
    self.MainUI = Tk()
    self.MainUI.attributes('-zoomed', True)
    self.MainUI.title("Phase 1")

    ImageName = str(self.InitialImage_P1())
    ImageLoad = Image.open("..//Input_Files//" + ImageName + ".png")
    ImageRender = ImageTk.PhotoImage(ImageLoad)
    
    self.ImageDisplay = Label(self.MainUI, image=ImageRender)
    self.ImageDisplay.image = ImageRender
    self.ImageDisplay.grid(row=0, column=0, columnspan=3)
    
    if self.DebugMode == "true":
      self.Debug = Label(self.MainUI, text = "Image number: "+ImageName)
      self.Debug.grid(row=1, column=0, columnspan=3)
      self.Debug.config(font=("Courier", 22))
    
    Instructions = Label(self.MainUI, text = "Press either button '1' or '2' to place image in category 1 or category 2")
    Instructions.grid(row=2, column=0, columnspan=3)
    Instructions.config(font=("Courier", 22))
    
    SortToOne = Button(self.MainUI, text="1", command=self.CategoryOne_P1)
    SortToOne.config(font=("Courier bold", 22), width=10, bg="red")
    SortToOne.grid(row=3, column=1, sticky=W)
    
    SortToTwo = Button(self.MainUI, text="2", command=self.CategoryTwo_P1)
    SortToTwo.config(font=("Courier bold", 22), width=10, bg="RoyalBlue3")
    SortToTwo.grid(row=3, column=2, sticky=W)
    
    self.MainUI.mainloop()
    
  # Begins the second phase, where the user will have no input on their categorization choice
  # and they will also be shown images that belong to neither category.
  def StartPhaseTwo(self):
    self.MainUI = Tk()
    self.MainUI.attributes('-zoomed', True)
    self.MainUI.title("Phase 2")
    
    ImageName = str(self.InitialImage_P2())
    ImageLoad = Image.open("..//Input_Files//" + ImageName + ".png")
    ImageRender = ImageTk.PhotoImage(ImageLoad)
    
    self.ImageDisplay = Label(self.MainUI, image=ImageRender)
    self.ImageDisplay.image = ImageRender
    self.ImageDisplay.grid(row=0, column=0, columnspan=3)
    
    if self.DebugMode == "true":
      self.Debug = Label(self.MainUI, text = "Image number: "+ImageName)
      self.Debug.grid(row=1, column=0, columnspan=3)
      self.Debug.config(font=("Courier", 22))
    
    Instructions = Label(self.MainUI, text = "Press either button '1' or '2' to place image in category 1 or category 2")
    Instructions.grid(row=2, column=0, columnspan=3)
    Instructions.config(font=("Courier", 22))
    
    SortToOne = Button(self.MainUI, text="1", command=self.CategoryOne_P2)
    SortToOne.config(font=("Courier bold", 22), width=10, bg="red")
    SortToOne.grid(row=3, column=1, sticky=W)
    
    SortToTwo = Button(self.MainUI, text="2", command=self.CategoryTwo_P2)
    SortToTwo.config(font=("Courier bold", 22), width=10, bg="RoyalBlue3")
    SortToTwo.grid(row=3, column=2, sticky=W)

  
  # Informs the user that the experiement has concluded and closes the window upon pressing the button.
  def SayGoodbye(self):
    Goodbye = Tk()   
    Goodbye.title("Goodbye")
    
    GoodbyeText = Label(Goodbye, text = "Thank you for participating in this experiment!")
    GoodbyeText.grid(row=0, column=0, columnspan=3)
    GoodbyeText.config(font=("Courier", 22))
    
    GoodbyeButton = Button(Goodbye, text="End experiment", command=Goodbye.destroy)
    GoodbyeButton.config(font=("Courier bold", 22), width=15, bg="green")
    GoodbyeButton.grid(row=3, column=1, sticky=W)

    Goodbye.mainloop()

