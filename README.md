homework_05
===========



This homework will write a regular expressions parser which extracts various types of information from a movie script text file. You will have explore and figure out th best way to do this - the functions in the repo provide a framework of approach. 


**Due:** Monday March 27, 6pm.

To receive full credit, you must commit and push code that passes all unit tests, and shell scripts that give the correct output.

----

Setup
-----

Clone the repo and save it in a local directory called `homework_05` by typing

    git clone https://github.com/columbia-applied-data-science/homework_05_team_XX.git \
    homework_05


Functions
---------
Note:  Don't forget to export the appropriate PYTHONPATH.  In your `~/.bashrc` (or `~/.bash_profile` on macs), put

    export PYTHONPATH=path-to-directory-above-homework_05:$PYTHONPATH

Then source it with `source ~/.bashrc` or open a new terminal.


### getSpeakers()
* Takes script and returns a list all the speakers who appear there. 
* Uses the two functions below to identify which line of text should be a speaker and extracts the relevant text.
* Given the standard spacing and layout of the text, a good approach is to count white spaces to identify which lines are potential speakers. However, you will likely end up with many false positives, or simply a very rigid system, so some additional checks will be in order. 

### getFirstNonSpacePos()
* Takes a string and returns the index of the first non-white space characters.  

### getSpeakers()
* Takes a string and extracts the speaker name. Note: the speaker name should not have any extraneous characters, such as white spaces, around it.

### getScenesData()
* Takes a script and returns a list of scene data for every scene in the script. Every element of the list, i.e. every scene description, will be a 4-element tuple consisting of:
1) scene start line
2) scene end line
3) scene type: 'EXT' or 'INT'
4) any other descriptive text in the scene delimiter line, such as location, stage directions, etc

IN THE ABOVE ORDER!

* Note: for our purposes every scene will begin with either an 'Exterior' or 'Interior' marker, usually denoted by 'EXT.' or 'INT.

### sceneType()
* takes a string, delimiting the start of a scene, and returns the scene type ('EXT' or 'INT')

### getSceneDescription()
* takes a string, delimiting the start of a scene, and returns additional descriptive information (location, directions, etc)

----

Unit Tests
----------

To run tests, cd to *tests/* and do

    python -m unittest -v scriptUnitTest

Once you are done, you will get notification that all tests passed.
