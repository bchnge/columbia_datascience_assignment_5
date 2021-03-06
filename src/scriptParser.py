#!/usr/bin/env python
from optparse import OptionParser
from collections import Counter
import sys
import re
import pdb


import homework_05.src.common as common


def main():
    """
    reads a movie script text file and extracts data
    Examples
    ---------
    """
    usage = "usage: %prog [options] dataset"
    usage += '\n'+main.__doc__
    parser = OptionParser(usage=usage)

    parser.add_option(
        "-o", "--outfilename",
        help="Write to this file rather than stdout.  [default: %default]",
        action="store", dest='outfilename', default=None)

   # pdb.set_trace()
    (options, args) = parser.parse_args()

    ### Parse args
    # Raise an exception if the length of args is greater than 1
    assert len(args) <= 1
    # If an argument is given, then it is the 'infilename'
    # If no arguments are given, set infilename equal to None
    infilename = args[0] if args else None

      ## Get the infile/outfile
    infile, outfile = common.get_inout_files(infilename, options.outfilename)

    ## Call the function that does the real work
    organize(infile, outfile)

    ## Close the files iff not stdin, stdout
    common.close_files(infile, outfile)


def organize(infile, outfile):
    '''
    This is going to run all the parsing functions, organize the output and dump to outfile or stdout
    '''

    ###get the script
    script = infile.readlines()
    
    characters = getSpeakers(script)
    scenes = getScenesData(script)
   
    scriptData = {'Characters': characters, 'SceneData': scenes}
   
    outfile.write(str(scriptData))
   





       

###############################PARSING FUNCTIONS###################
def getSpeakers(script):
    '''
    This function will return the characters in a script. 

    Parameters
    ----------

    script: a list of lines in the script text file


    Returns
    -------

    speakers: list

    Note:
    -----

    There are a number of different ways to extract the speakers names from a script. One way is to first identify the position where these names appear, i.e. count the number of whitespace, and then extract just the name from the line. Since we are dealing with speakers and not with all characters, you can assume that each speaker is followed by a section of dialogue. You will also have to make sure that you are treating both whitespaces and tabs in the same manner; one way to do this is to convert all whitespaces to tabs with the re.sub(). 
    In order to minimize the number of false positives, we will only list speakers who appear more than once in the script. The Counter() funtion from the python collections library is a good choice for this. 
    '''
    #pdb.set_trace()
    space = 0
    Lis = []
    Charac = []
    tab_width = 8	
    for line in script:
	#line = re.sub(r"{"+'tab_width'+r"}",r"\t",line)
	line = re.sub(r"\t",' '*tab_width,line)
	space = getFirstNonSpacePos(line)
	if space > 25:	
	    newSpeaker = getSpeaker(line)
	    if len(newSpeaker)>1:
	      Lis.append(newSpeaker)
	else:
	    pass
    cnt = Counter()
    for word in Lis:
	cnt[word] += 1
    return (cnt.keys() )    

def getFirstNonSpacePos(line):
    '''
    This funciton takes a line of text and returns the number of whitespace before the first non-whitespace character. If the line contains only whitespace it returns None.

    Parameters
    __________

    line: string
    Returns
    _______
    numeric or None
    
   
    '''
    m = re.match(r"(\s+\S)",line)
    if m==None:
     index_pos = 0
    else:
     index_pos = m.end()-1
    '''
    index_pos = 0
    for char in line:
        if char != '\t' and char != '\n' and char != ' ':
            break
        if index_pos == len(line):
            index_pos = -1
            break
        index_pos = index_pos + 1  
    '''  
    
    return index_pos
    
def getSpeaker(line):
    '''
    This function extracts the speaker from the line. You will need to strip away everything but the speakers name, or title. 

    Parameters
    ----------

    line: string

    Returns
    -------
    string

    ''' 
  
    # Assuming the line contains either one or two words
    #pdb.set_trace()
    speakerName = '' 
    t = re.findall(r"(\w+)",line)
    
    if len(t)==2:   
      speakerName = re.findall(r"(\s[A-Z]+\s[A-Z]+\s)",line)
    elif len(t)==1:
      speakerName = re.findall(r"(\s[A-Z]+\s)",line)
    
    
    # This will strip white spaces
    if len(speakerName)==1:
      #speakerName = re.findall(r"([A-Z]+\s[A-Z]+|[A-Z]+)",speakerName[0])
      speakerName = speakerName[0].strip()
  
    return speakerName


def getScenesData(script):
    '''
    This function runs through the script and looks for line that have a scene marker ("INT/EXT" or such). It keeps track of the lines the scene starts and end, the type of scene it is (interior or exterior), and any additional description (such as location, directions, etc). The function returns a list containg the scene start/end lines, the type and descriptions. 

    Parameters
    ----------
    script: list of strings

    Returns
    -------
    list
    '''
    result = []
    for lineno, line in enumerate(script):
        intext = re.search("INT.|EXT.", line)
        if intext:
            strippedLine = line[intext.start():]
            newstartno = lineno
            scenetype = sceneType(strippedLine)
            scenedesc = getSceneDescription(strippedLine)
            result.append([newstartno, ' ', scenetype, scenedesc])
    
    numScenes = len(result)
    for sceneno, scene in enumerate(result):
        if sceneno<numScenes-1:
            result[sceneno][1] = result[sceneno+1][0]
        else:
            result[sceneno][1] = len(script)
    return result

def sceneType(line):
    '''
    Retrives the scene type. 

    Parameters
    ----------
    string

    Returns
    -------
    string: either "INT" or "EXT" depending on scene type

    '''

    if len(re.findall(r"INT.", line)) == 1:
        sType="INT"
    elif len(re.findall(r"EXT.", line)) == 1:
        sType="EXT"    
    return sType

def getSceneDescription(line):
    '''
    This function retrieves the description of a scene. It takes a line that starts with a scene marker, such as INT or EXT, and retirves all the descriptive text 
    which follows the marker. Note, it also strips the text of surrounding whitespaces (recommend using the .strip() method in the string library). 

    Parameters
    ----------
    string

    Returns
    -------
    string

	    '''


    desc = re.sub("(EXT.)|(INT.)", "", line).strip()
    #desc = line.split('.',1)[1].strip()
    return desc 


if __name__ == "__main__":
    main()

