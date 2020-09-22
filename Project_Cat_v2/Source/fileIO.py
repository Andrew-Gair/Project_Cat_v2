# Author: Andrew Gair
# Date: September 2020
# Purpose: Helper functions to manage input and output to/from files.

import sys
import os

# Opens 'FileName' and appends 'Value' to it
def WriteToFile(FileName, Value):
  FileHandle = open(FileName, "a")
  FileHandle.write(Value)
  FileHandle.close()
  
# Opens 'FileName' and appends a new-line to it
def AddNewLine(FileName):
  FileHandle = open(FileName, "a")
  FileHandle.write("\n")
  FileHandle.close()
