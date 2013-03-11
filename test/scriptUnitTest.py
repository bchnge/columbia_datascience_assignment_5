import glob
import unittest
import pdb


import homework_05_soln.src.common as common
from homework_05_soln.src.scriptParser import *



class TestScript(unittest.TestCase):

    def setUp(self):
        #pdb.set_trace()
        self.f = open(path)
        self.script = self.f.readlines()
        self.speakers = getSpeakers(self.script)
        self.scenes = getScenesData(self.script)
         
    
    def test_speakers_type(self):
        self.assertIs(type(self.speakers), list)
    
    def test_speakers_len(self):
        self.assertGreater(len(set(self.speakers)), 15)



    def test_scenes_type(self):
        self.assertIs(type(self.scenes), list)

    def test_scenes_len(self):
        self.assertGreater(len(self.scenes), 15)

    def test_scenes_tuple(self):
        [self.assertIs(len(scene), 4) for scene in self.scenes]

    def test_scenes_startEnd(self):
        [self.assertGreater(scene[1], scene[0]) for scene in self.scenes]

    def test_scene_type(self):
        [self.assertIn(scene[2], ['EXT','INT']) for scene in self.scenes]






class TestScriptBasic(unittest.TestCase):

    def setUp(self):
        self.sceneHead  = '       EXT. SUBMARINE, ESCAPE HATCH - CONTINUOUS'
        self.f = open('../data/Script.test')
        self.script = self.f.readlines()
        self.speakers = getSpeakers(self.script)
        self.scenes = getScenesData(self.script)

    

    def test_sceneDescription(self):
        sceneDesc = getSceneDescription(self.sceneHead)
        self.assertEquals(sceneDesc, 'SUBMARINE, ESCAPE HATCH - CONTINUOUS')

    def test_sceneType(self):
        #pdb.set_trace()
        sceneT = sceneType(self.sceneHead)
        self.assertEquals(sceneT, 'EXT')

    def test_firstNoneSpacePos(self):
        fnsp = getFirstNonSpacePos(self.sceneHead)
        self.assertIs(fnsp, 7)

    def test_speakers(self):
        self.assertEquals(self.speakers, ['RENARD', 'CIGAR GIRL'])

    def test_scenes(self):
        self.assertEquals(self.scenes, [(0, 10, 'INT', 'BANK - GENEVA - DAY'), (10, 15, 'INT', 'STAIRWELL/ELEVATOR SHAFT - DAY'), (15, 22, 'EXT', 'STREET - GENEVA'), (22, 63, 'INT', 'HOTEL - GENEVA - DAY'), (63, 68, 'EXT', 'RIVER THAMES - LONDON - DAY'), (68, 74, 'EXT', 'RIVER THAMES - LONDON - DAY')])

    def test_scenes(self):
        self.assertEquals(len(self.scenes), 6) 

        
suite = unittest.TestLoader().loadTestsFromTestCase(TestScriptBasic)
unittest.TextTestRunner(verbosity=2).run(suite)



###Run it
print 'TESTING TXT SCRIPTS'
paths = glob.glob('../data/' + '*.txt')
print paths


for path in paths:
    print path
    suite = unittest.TestLoader().loadTestsFromTestCase(TestScript)
    unittest.TextTestRunner(verbosity=2).run(suite)


