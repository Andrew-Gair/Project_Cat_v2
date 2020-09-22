Project CAT readme:
Author: Andrew Gair

#---- Change Log:
  Sept 22 2020:
    Version two added 'Go with Debug' option to initial UI and also
    substantially cleaned-up the source code with better variable names
    and better comments on project details.
    Version two was only tested on Ubuntu OS whereas Version One
    was tested only on Windows OS.

#---- How To Run The Program:
  'python3 ./project_cat.py' is the command to execute the program
  You must navigate to the 'Source' directory first and then run the command
  in a terminal window.

#---- Known Bugs:
  If 'Phase 1 Trials' is set to a negative number, 1, or 0, the program will not
  function correctly.
  In a practical situation, the number would never be lower than 10.
  The solution is simple (but not implemented): further checking of input data.

#---- File Structure:
  The file structure is critical to proper functionality of the program, if
  a file is missing or incorrectly located the program is likely to fail.
  
  Directories:
  Docs: contains documents that give more detail on the purpose of this program.
  Input_Files: contains all input images, which are further seperated into
               their own directories based on category.
    --> Group_1: contains the source images for 'Category 1' images
    --> Group_2: contains the source images for 'Category 2' images
    --> Group_Test: contains the source images for 'Test Category' images
    --> Sound_Effects: contains the source sound files for 'Correct' and 'Incorrect'
                       categorization of images during 'Phase 1' of experiment.
    --> 1111_example.png and 2222_example.png are the source images shown during
        initial program start.
  Output_Files: contains the .txt files the program creates upon running the experiment.
  Source: the python3 source code
    --> fileIO.py: a module that contains simple methods for general purpose file input/output
    --> uiEvents.py: a specially designed class that implements the core functionality of the program.
    --> project_cat.py: the source code that calls the methods from within uiEvents.py to start 
                        the program.

#---- Naming Scheme For Images:
  Images MUST be in the form: [code].png
  	1121.png 	is a valid format
	  1121_beep.png 	is not a valid format
	All image-codes are hardcoded into uiEvents.py in the 'PickGroupOne', 'PickGroupTwo', and
	'PickGroupTest' methods.

#---- Resources Used:
  Sound effects taken from www.freesound.org

  Python modules: must be installed seperatly before program can run.
    Tkinter, for displaying UI elements
    Playsound, for playing sound effects on button press
    Pillow, for displaying images through Tkinter.
    
#---- Author's Note:
  I chose the name as this was a program meant for a research project on categorization.
    --> See the Docs directory for more information.
  Hence: 'Project Categorization', or 'Project Cat' for short.
