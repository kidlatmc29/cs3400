"""
GEDtest.py

Test program for the family tree assignment derived from descendants.py
This is not intended to be an "importable" module
"""
from familyTree import *

def runKennedyTests():
    
    print("Running tests on familyTree.py using the Kennedy.ged file\n")
          
    # Optionally print out all information stored about individuals
    doPrint = input("Print persons info?")
    if doPrint in 'yY':
        printAllPersonInfo()

    #  Optionally print out all information stored about families
    print()
    doPrint = input("Print families info?")
    if doPrint in 'yY':
        printAllFamilyInfo()

    print()
    doPrint = input("Print descendants?")
    if doPrint in 'yY':
        print()
        person = "I46"  # Patrick Kennedy
        getPerson(person).printDescendants()
        print()

    print()
    doPrint = input("Test isDescendant?")
    if doPrint in 'yY':
        print()
        print('**** Tests of isDescendant')
        print('Expected answers are "is" "is" "is not" "is not"')
        #
        # NOTE: These tests use a name() function in person that
        #       prints just the name, without event information.
        #
        if getPerson("I46").isDescendant('I55'): notString = ' '
        else: notString = ' not '
        print(getPerson("I55").name() + ' is' + notString +
              'a descendant of ' + getPerson("I46").name())
        if getPerson("I47").isDescendant('I54'): notString = ' '
        else: notString = ' not '
        print(getPerson("I54").name() + ' is' + notString +
              'a descendant of ' + getPerson("I47").name())
        if getPerson("I46").isDescendant('I53'): notString = ' '
        else: notString = ' not '
        print(getPerson("I53").name() + ' is' + notString +
              'a descendant of ' + getPerson("I46").name())
        if getPerson("I61").isDescendant('I54'): notString = ' '
        else: notString = ' not '
        print(getPerson("I54").name() + ' is' + notString +
              'a descendant of ' + getPerson("I61").name())
        
    print()
    doPrint = input("Test printAncestors?")
    if doPrint in 'yY':
        print('**** Call to printAncestors for I55 (John Fitzgerald KENNEDY Jr.)')
        print()
        getPerson("I55").printAncestors('')

    print()
    doPrint = input("Test printCousins?")
    if doPrint in 'yY':
        print()
        getPerson("I54").printCousins()  # Caroline KENNEDY
        print()
        getPerson("I82").printCousins()  # Edwin Moore KENNEDY Jr.
        print()
        getPerson("I1").printCousins()  # Joseph Patrick Kennedy
        print()
        getPerson("I49").printCousins(1)   # Janet LEE
        print()
        getPerson("I81").printCousins(2)   # John Bouvier Kennedy SCHLOSSBERG

def runGeneralTests():
    print("Running tests on familyTree.py using",filename)
    print()
          
    # Optionally print out all information stored about individuals
    doPrint = input("Print persons info?")
    if doPrint in 'yY':
        printAllPersonInfo()

    #  Optionally print out all information stored about families
    print()
    doPrint = input("Print families info?")
    if doPrint in 'yY':
        printAllFamilyInfo()

    print()
    doPrint = input("Print descendants?")
    if doPrint in 'yY':
        print()
        person = input("Enter person ID for descendants chart:")
        getPerson(person).printDescendants()
        print()

#-----------------------------------------------------------------------
        
## This module will only be used to test familyTree.py, 
## so it will always be the main module in an execution.
## There is no need to test whether __name__ == '__main__' 

## Define filename for call to processGEDCOM( )
filename = input("Type the name of the GEDCOM file or hit Enter to accept default:")
if filename == '':
    filename = "Kennedy.ged"  # Set a default name if none provided

processGEDCOM(filename)

if filename == "Kennedy.ged":
    runKennedyTests()
else:
    runGeneralTests()
