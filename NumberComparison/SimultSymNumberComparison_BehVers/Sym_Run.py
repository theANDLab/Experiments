#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 05, 2020, at 17:44
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
#psychopy.useVersion('3.2.3')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'NumberGame_v09302020'  # from the Builder filename that created this script
expInfo = {'Participant': '', 'Session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['Participant'], expInfo['Session'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\local-admin\\Desktop\\Dense sampling\\SimultSymNumberComparison_BehVers\\NumberGame_v09302020.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='Eizo', color=[-0.608,-0.608,-0.608], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruct"
InstructClock = core.Clock()
gameName = visual.TextStim(win=win, name='gameName',
    text='The Number Game',
    font='Arial',
    pos=(0, 0.42), height=0.05, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
gameInstruct = visual.TextStim(win=win, name='gameInstruct',
    text='This game is about choosing the number that means more. \nPress the left button for the left side or the right button for the right side.\n\n',
    font='Arial',
    pos=(0, .3), height=0.03, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
gameExample = visual.ImageStim(
    win=win,
    name='gameExample', units='height', 
    image='NumberGame_images/instruction_example.png', mask=None,
    ori=0, pos=(0, 0), size=(0.565, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
hand_left = visual.ImageStim(
    win=win,
    name='hand_left', units='height', 
    image='NumberGame_images/hand_left.png', mask=None,
    ori=0, pos=(-.4, -.2), size=(.188, .3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
button_yellow = visual.ImageStim(
    win=win,
    name='button_yellow', units='height', 
    image='NumberGame_images/black_button.png', mask=None,
    ori=0, pos=(-.25, -.15), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
hand_right = visual.ImageStim(
    win=win,
    name='hand_right', units='height', 
    image='NumberGame_images/hand_right.png', mask=None,
    ori=0, pos=(.4, -.2), size=(.188, .3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-5.0)
button_blue = visual.ImageStim(
    win=win,
    name='button_blue', units='height', 
    image='NumberGame_images/black_button.png', mask=None,
    ori=0, pos=(.25, -.15), size=(.1, .1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
check_mark = visual.ImageStim(
    win=win,
    name='check_mark', units='height', 
    image='NumberGame_images/check_mark.png', mask=None,
    ori=0, pos=(-.25, -.085), size=(.05, .05),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
instructProceed = visual.TextStim(win=win, name='instructProceed',
    text='First we are going to do some practice.\nReady? (SPACE to continue)',
    font='Arial',
    pos=(0, -.37), height=0.03, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instructReady = keyboard.Keyboard()

# Initialize components for Routine "PrePrac1"
PrePrac1Clock = core.Clock()
prepracFix1 = visual.Line(
    win=win, name='prepracFix1',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
prepracLeft1 = visual.ImageStim(
    win=win,
    name='prepracLeft1', units='height', 
    image='NumberGame_images/1_Arial.bmp', mask=None,
    ori=0, pos=(-.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prepracRight1 = visual.ImageStim(
    win=win,
    name='prepracRight1', units='height', 
    image='NumberGame_images/5_Arial.bmp', mask=None,
    ori=0, pos=(.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
prepracInstruct1 = visual.TextStim(win=win, name='prepracInstruct1',
    text='Which one means more? \nWhich button would you press?',
    font='Arial',
    pos=(0, -.4), height=0.03, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
prepracResp1 = keyboard.Keyboard()

# Initialize components for Routine "PrePrac2"
PrePrac2Clock = core.Clock()
prepracFix2 = visual.Line(
    win=win, name='prepracFix2',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
prepracLeft2 = visual.ImageStim(
    win=win,
    name='prepracLeft2', units='height', 
    image='NumberGame_images/6_Arial.bmp', mask=None,
    ori=0, pos=(-.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prepracRight2 = visual.ImageStim(
    win=win,
    name='prepracRight2', units='height', 
    image='NumberGame_images/4_Arial.bmp', mask=None,
    ori=0, pos=(.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
prepracInstruct2 = visual.TextStim(win=win, name='prepracInstruct2',
    text='Which one means more? \nWhich button would you press? ',
    font='Arial',
    pos=(0, -.4), height=0.03, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
prepracResp2 = keyboard.Keyboard()

# Initialize components for Routine "PrePracEnd"
PrePracEndClock = core.Clock()
prepracEnd = visual.TextStim(win=win, name='prepracEnd',
    text='You got it! \nNow we will do some more practice. \nPress a button as soon as you know the answer.\n\nReady?\n(SPACE to continue)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prepracEndResp = keyboard.Keyboard()

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
blankReady = visual.TextStim(win=win, name='blankReady',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Fix"
FixClock = core.Clock()
fix1 = visual.Line(
    win=win, name='fix1',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Prac"
PracClock = core.Clock()
pracITI = visual.Line(
    win=win, name='pracITI',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
pracLeft = visual.ImageStim(
    win=win,
    name='pracLeft', units='height', 
    image='sin', mask=None,
    ori=0, pos=(-.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
pracRight = visual.ImageStim(
    win=win,
    name='pracRight', units='height', 
    image='sin', mask=None,
    ori=0, pos=(.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
pracResp = keyboard.Keyboard()
pracStatic = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='pracStatic')

# Initialize components for Routine "PracFeedback"
PracFeedbackClock = core.Clock()
# feedback variables just need some values at start
feedbackImg=''
feedbackMsg=''
pracCorr=[] # holding array for accuracy (1 or 0)
#minNrPractice = 10  # min number of trials to practice
#minAccuracy = 0.5 # criterion: 5/10
feedbackImage = visual.ImageStim(
    win=win,
    name='feedbackImage', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(.2, .2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
feedbackText = visual.TextStim(win=win, name='feedbackText',
    text='default text',
    font='Arial',
    pos=(0, 0.15), height=0.04, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "PracEnd"
PracEndClock = core.Clock()
pracITIEnd = visual.Line(
    win=win, name='pracITIEnd',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
pracEnd = visual.TextStim(win=win, name='pracEnd',
    text="Great job!\nNow we are going to do some more, but this time you won't get feedback.\nPress a button as soon as you know the answer.\n\nReady?\n(Press SPACE to continue)",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
pracEndClear = keyboard.Keyboard()

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
blankReady = visual.TextStim(win=win, name='blankReady',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Fix"
FixClock = core.Clock()
fix1 = visual.Line(
    win=win, name='fix1',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Test"
TestClock = core.Clock()
testITI = visual.Line(
    win=win, name='testITI',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
testLeft = visual.ImageStim(
    win=win,
    name='testLeft', units='height', 
    image='sin', mask=None,
    ori=0, pos=(-.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
testRight = visual.ImageStim(
    win=win,
    name='testRight', units='height', 
    image='sin', mask=None,
    ori=0, pos=(.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
testResp = keyboard.Keyboard()
testStatic = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='testStatic')

# Initialize components for Routine "trlTrack"
trlTrackClock = core.Clock()
# variable just needs some value at start
corr =[]

# Initialize components for Routine "TaskFeedback"
TaskFeedbackClock = core.Clock()
# variable just needs some value at start
TaskFeedback=''
ACC=''
blockBreak = visual.TextStim(win=win, name='blockBreak',
    text="You are doing awesome!\nLet's take a short break...\n\n(Press SPACE to continue)",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
TaskFeedbackText = visual.TextStim(win=win, name='TaskFeedbackText',
    text='default text',
    font='Arial',
    pos=(.45, -.4), height=0.02, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
breakEnd = keyboard.Keyboard()

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
blankReady = visual.TextStim(win=win, name='blankReady',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Fix"
FixClock = core.Clock()
fix1 = visual.Line(
    win=win, name='fix1',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Test"
TestClock = core.Clock()
testITI = visual.Line(
    win=win, name='testITI',units='height', 
    start=(-(.7,.7)[0]/2.0, 0), end=(+(.7,.7)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=4, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], colorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
testLeft = visual.ImageStim(
    win=win,
    name='testLeft', units='height', 
    image='sin', mask=None,
    ori=0, pos=(-.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
testRight = visual.ImageStim(
    win=win,
    name='testRight', units='height', 
    image='sin', mask=None,
    ori=0, pos=(.28, 0), size=(.35, .35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
testResp = keyboard.Keyboard()
testStatic = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='testStatic')

# Initialize components for Routine "trlTrack"
trlTrackClock = core.Clock()
# variable just needs some value at start
corr =[]

# Initialize components for Routine "End"
EndClock = core.Clock()
TaskFeedbackText2 = visual.TextStim(win=win, name='TaskFeedbackText2',
    text='default text',
    font='Arial',
    pos=(.45, -.4), height=0.02, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
endInstr = visual.TextStim(win=win, name='endInstr',
    text='Great job!\n\n  DONE!',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[0.804,0.804,0.804], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruct"-------
# update component parameters for each repeat
instructReady.keys = []
instructReady.rt = []
# keep track of which components have finished
InstructComponents = [gameName, gameInstruct, gameExample, hand_left, button_yellow, hand_right, button_blue, check_mark, instructProceed, instructReady]
for thisComponent in InstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instruct"-------
while continueRoutine:
    # get current time
    t = InstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gameName* updates
    if gameName.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gameName.frameNStart = frameN  # exact frame index
        gameName.tStart = t  # local t and not account for scr refresh
        gameName.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gameName, 'tStartRefresh')  # time at next scr refresh
        gameName.setAutoDraw(True)
    
    # *gameInstruct* updates
    if gameInstruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gameInstruct.frameNStart = frameN  # exact frame index
        gameInstruct.tStart = t  # local t and not account for scr refresh
        gameInstruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gameInstruct, 'tStartRefresh')  # time at next scr refresh
        gameInstruct.setAutoDraw(True)
    
    # *gameExample* updates
    if gameExample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gameExample.frameNStart = frameN  # exact frame index
        gameExample.tStart = t  # local t and not account for scr refresh
        gameExample.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gameExample, 'tStartRefresh')  # time at next scr refresh
        gameExample.setAutoDraw(True)
    
    # *hand_left* updates
    if hand_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hand_left.frameNStart = frameN  # exact frame index
        hand_left.tStart = t  # local t and not account for scr refresh
        hand_left.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hand_left, 'tStartRefresh')  # time at next scr refresh
        hand_left.setAutoDraw(True)
    
    # *button_yellow* updates
    if button_yellow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_yellow.frameNStart = frameN  # exact frame index
        button_yellow.tStart = t  # local t and not account for scr refresh
        button_yellow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_yellow, 'tStartRefresh')  # time at next scr refresh
        button_yellow.setAutoDraw(True)
    
    # *hand_right* updates
    if hand_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hand_right.frameNStart = frameN  # exact frame index
        hand_right.tStart = t  # local t and not account for scr refresh
        hand_right.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hand_right, 'tStartRefresh')  # time at next scr refresh
        hand_right.setAutoDraw(True)
    
    # *button_blue* updates
    if button_blue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_blue.frameNStart = frameN  # exact frame index
        button_blue.tStart = t  # local t and not account for scr refresh
        button_blue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_blue, 'tStartRefresh')  # time at next scr refresh
        button_blue.setAutoDraw(True)
    
    # *check_mark* updates
    if check_mark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        check_mark.frameNStart = frameN  # exact frame index
        check_mark.tStart = t  # local t and not account for scr refresh
        check_mark.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(check_mark, 'tStartRefresh')  # time at next scr refresh
        check_mark.setAutoDraw(True)
    
    # *instructProceed* updates
    if instructProceed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructProceed.frameNStart = frameN  # exact frame index
        instructProceed.tStart = t  # local t and not account for scr refresh
        instructProceed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructProceed, 'tStartRefresh')  # time at next scr refresh
        instructProceed.setAutoDraw(True)
    
    # *instructReady* updates
    waitOnFlip = False
    if instructReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructReady.frameNStart = frameN  # exact frame index
        instructReady.tStart = t  # local t and not account for scr refresh
        instructReady.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructReady, 'tStartRefresh')  # time at next scr refresh
        instructReady.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instructReady.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructReady.status == STARTED and not waitOnFlip:
        theseKeys = instructReady.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruct"-------
for thisComponent in InstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gameName.started', gameName.tStartRefresh)
thisExp.addData('gameName.stopped', gameName.tStopRefresh)
thisExp.addData('gameInstruct.started', gameInstruct.tStartRefresh)
thisExp.addData('gameInstruct.stopped', gameInstruct.tStopRefresh)
thisExp.addData('gameExample.started', gameExample.tStartRefresh)
thisExp.addData('gameExample.stopped', gameExample.tStopRefresh)
thisExp.addData('hand_left.started', hand_left.tStartRefresh)
thisExp.addData('hand_left.stopped', hand_left.tStopRefresh)
thisExp.addData('button_yellow.started', button_yellow.tStartRefresh)
thisExp.addData('button_yellow.stopped', button_yellow.tStopRefresh)
thisExp.addData('hand_right.started', hand_right.tStartRefresh)
thisExp.addData('hand_right.stopped', hand_right.tStopRefresh)
thisExp.addData('button_blue.started', button_blue.tStartRefresh)
thisExp.addData('button_blue.stopped', button_blue.tStopRefresh)
thisExp.addData('check_mark.started', check_mark.tStartRefresh)
thisExp.addData('check_mark.stopped', check_mark.tStopRefresh)
thisExp.addData('instructProceed.started', instructProceed.tStartRefresh)
thisExp.addData('instructProceed.stopped', instructProceed.tStopRefresh)
# the Routine "Instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PrePrac1"-------
# update component parameters for each repeat
prepracResp1.keys = []
prepracResp1.rt = []
# keep track of which components have finished
PrePrac1Components = [prepracFix1, prepracLeft1, prepracRight1, prepracInstruct1, prepracResp1]
for thisComponent in PrePrac1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PrePrac1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "PrePrac1"-------
while continueRoutine:
    # get current time
    t = PrePrac1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PrePrac1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prepracFix1* updates
    if prepracFix1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracFix1.frameNStart = frameN  # exact frame index
        prepracFix1.tStart = t  # local t and not account for scr refresh
        prepracFix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracFix1, 'tStartRefresh')  # time at next scr refresh
        prepracFix1.setAutoDraw(True)
    
    # *prepracLeft1* updates
    if prepracLeft1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracLeft1.frameNStart = frameN  # exact frame index
        prepracLeft1.tStart = t  # local t and not account for scr refresh
        prepracLeft1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracLeft1, 'tStartRefresh')  # time at next scr refresh
        prepracLeft1.setAutoDraw(True)
    
    # *prepracRight1* updates
    if prepracRight1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracRight1.frameNStart = frameN  # exact frame index
        prepracRight1.tStart = t  # local t and not account for scr refresh
        prepracRight1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracRight1, 'tStartRefresh')  # time at next scr refresh
        prepracRight1.setAutoDraw(True)
    
    # *prepracInstruct1* updates
    if prepracInstruct1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prepracInstruct1.frameNStart = frameN  # exact frame index
        prepracInstruct1.tStart = t  # local t and not account for scr refresh
        prepracInstruct1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracInstruct1, 'tStartRefresh')  # time at next scr refresh
        prepracInstruct1.setAutoDraw(True)
    
    # *prepracResp1* updates
    waitOnFlip = False
    if prepracResp1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracResp1.frameNStart = frameN  # exact frame index
        prepracResp1.tStart = t  # local t and not account for scr refresh
        prepracResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracResp1, 'tStartRefresh')  # time at next scr refresh
        prepracResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(prepracResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(prepracResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if prepracResp1.status == STARTED and not waitOnFlip:
        theseKeys = prepracResp1.getKeys(keyList=['2'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            prepracResp1.keys.append(theseKeys.name)  # storing all keys
            prepracResp1.rt.append(theseKeys.rt)
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PrePrac1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PrePrac1"-------
for thisComponent in PrePrac1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prepracFix1.started', prepracFix1.tStartRefresh)
thisExp.addData('prepracFix1.stopped', prepracFix1.tStopRefresh)
thisExp.addData('prepracLeft1.started', prepracLeft1.tStartRefresh)
thisExp.addData('prepracLeft1.stopped', prepracLeft1.tStopRefresh)
thisExp.addData('prepracRight1.started', prepracRight1.tStartRefresh)
thisExp.addData('prepracRight1.stopped', prepracRight1.tStopRefresh)
thisExp.addData('prepracInstruct1.started', prepracInstruct1.tStartRefresh)
thisExp.addData('prepracInstruct1.stopped', prepracInstruct1.tStopRefresh)
# check responses
if prepracResp1.keys in ['', [], None]:  # No response was made
    prepracResp1.keys = None
thisExp.addData('prepracResp1.keys',prepracResp1.keys)
if prepracResp1.keys != None:  # we had a response
    thisExp.addData('prepracResp1.rt', prepracResp1.rt)
thisExp.addData('prepracResp1.started', prepracResp1.tStartRefresh)
thisExp.addData('prepracResp1.stopped', prepracResp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "PrePrac1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PrePrac2"-------
# update component parameters for each repeat
prepracResp2.keys = []
prepracResp2.rt = []
# keep track of which components have finished
PrePrac2Components = [prepracFix2, prepracLeft2, prepracRight2, prepracInstruct2, prepracResp2]
for thisComponent in PrePrac2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PrePrac2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "PrePrac2"-------
while continueRoutine:
    # get current time
    t = PrePrac2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PrePrac2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prepracFix2* updates
    if prepracFix2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracFix2.frameNStart = frameN  # exact frame index
        prepracFix2.tStart = t  # local t and not account for scr refresh
        prepracFix2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracFix2, 'tStartRefresh')  # time at next scr refresh
        prepracFix2.setAutoDraw(True)
    
    # *prepracLeft2* updates
    if prepracLeft2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracLeft2.frameNStart = frameN  # exact frame index
        prepracLeft2.tStart = t  # local t and not account for scr refresh
        prepracLeft2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracLeft2, 'tStartRefresh')  # time at next scr refresh
        prepracLeft2.setAutoDraw(True)
    
    # *prepracRight2* updates
    if prepracRight2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracRight2.frameNStart = frameN  # exact frame index
        prepracRight2.tStart = t  # local t and not account for scr refresh
        prepracRight2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracRight2, 'tStartRefresh')  # time at next scr refresh
        prepracRight2.setAutoDraw(True)
    
    # *prepracInstruct2* updates
    if prepracInstruct2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prepracInstruct2.frameNStart = frameN  # exact frame index
        prepracInstruct2.tStart = t  # local t and not account for scr refresh
        prepracInstruct2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracInstruct2, 'tStartRefresh')  # time at next scr refresh
        prepracInstruct2.setAutoDraw(True)
    
    # *prepracResp2* updates
    waitOnFlip = False
    if prepracResp2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracResp2.frameNStart = frameN  # exact frame index
        prepracResp2.tStart = t  # local t and not account for scr refresh
        prepracResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracResp2, 'tStartRefresh')  # time at next scr refresh
        prepracResp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(prepracResp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(prepracResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if prepracResp2.status == STARTED and not waitOnFlip:
        theseKeys = prepracResp2.getKeys(keyList=['1'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            prepracResp2.keys.append(theseKeys.name)  # storing all keys
            prepracResp2.rt.append(theseKeys.rt)
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PrePrac2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PrePrac2"-------
for thisComponent in PrePrac2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prepracFix2.started', prepracFix2.tStartRefresh)
thisExp.addData('prepracFix2.stopped', prepracFix2.tStopRefresh)
thisExp.addData('prepracLeft2.started', prepracLeft2.tStartRefresh)
thisExp.addData('prepracLeft2.stopped', prepracLeft2.tStopRefresh)
thisExp.addData('prepracRight2.started', prepracRight2.tStartRefresh)
thisExp.addData('prepracRight2.stopped', prepracRight2.tStopRefresh)
thisExp.addData('prepracInstruct2.started', prepracInstruct2.tStartRefresh)
thisExp.addData('prepracInstruct2.stopped', prepracInstruct2.tStopRefresh)
# check responses
if prepracResp2.keys in ['', [], None]:  # No response was made
    prepracResp2.keys = None
thisExp.addData('prepracResp2.keys',prepracResp2.keys)
if prepracResp2.keys != None:  # we had a response
    thisExp.addData('prepracResp2.rt', prepracResp2.rt)
thisExp.addData('prepracResp2.started', prepracResp2.tStartRefresh)
thisExp.addData('prepracResp2.stopped', prepracResp2.tStopRefresh)
thisExp.nextEntry()
# the Routine "PrePrac2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PrePracEnd"-------
# update component parameters for each repeat
prepracEndResp.keys = []
prepracEndResp.rt = []
# keep track of which components have finished
PrePracEndComponents = [prepracEnd, prepracEndResp]
for thisComponent in PrePracEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PrePracEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "PrePracEnd"-------
while continueRoutine:
    # get current time
    t = PrePracEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PrePracEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prepracEnd* updates
    if prepracEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prepracEnd.frameNStart = frameN  # exact frame index
        prepracEnd.tStart = t  # local t and not account for scr refresh
        prepracEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracEnd, 'tStartRefresh')  # time at next scr refresh
        prepracEnd.setAutoDraw(True)
    
    # *prepracEndResp* updates
    waitOnFlip = False
    if prepracEndResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepracEndResp.frameNStart = frameN  # exact frame index
        prepracEndResp.tStart = t  # local t and not account for scr refresh
        prepracEndResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepracEndResp, 'tStartRefresh')  # time at next scr refresh
        prepracEndResp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(prepracEndResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if prepracEndResp.status == STARTED and not waitOnFlip:
        theseKeys = prepracEndResp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PrePracEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PrePracEnd"-------
for thisComponent in PrePracEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prepracEnd.started', prepracEnd.tStartRefresh)
thisExp.addData('prepracEnd.stopped', prepracEnd.tStopRefresh)
# the Routine "PrePracEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank"-------
routineTimer.addTime(4.000000)
# update component parameters for each repeat
# reset the performance variables
corr =[]
TaskFeedback=''
ACC=''
# keep track of which components have finished
BlankComponents = [blankReady]
for thisComponent in BlankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BlankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BlankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blankReady* updates
    if blankReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blankReady.frameNStart = frameN  # exact frame index
        blankReady.tStart = t  # local t and not account for scr refresh
        blankReady.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blankReady, 'tStartRefresh')  # time at next scr refresh
        blankReady.setAutoDraw(True)
    if blankReady.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blankReady.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            blankReady.tStop = t  # not accounting for scr refresh
            blankReady.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blankReady, 'tStopRefresh')  # time at next scr refresh
            blankReady.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank"-------
for thisComponent in BlankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blankReady.started', blankReady.tStartRefresh)
thisExp.addData('blankReady.stopped', blankReady.tStopRefresh)

# ------Prepare to start Routine "Fix"-------
routineTimer.addTime(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
FixComponents = [fix1]
for thisComponent in FixComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Fix"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FixClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix1* updates
    if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix1.frameNStart = frameN  # exact frame index
        fix1.tStart = t  # local t and not account for scr refresh
        fix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
        fix1.setAutoDraw(True)
    if fix1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix1.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            fix1.tStop = t  # not accounting for scr refresh
            fix1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
            fix1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fix"-------
for thisComponent in FixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix1.started', fix1.tStartRefresh)
thisExp.addData('fix1.stopped', fix1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_Prac = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conds/NumberGame_Prac.xlsx', selection='0:10'),
    seed=None, name='trials_Prac')
thisExp.addLoop(trials_Prac)  # add the loop to the experiment
thisTrials_Prac = trials_Prac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_Prac.rgb)
if thisTrials_Prac != None:
    for paramName in thisTrials_Prac:
        exec('{} = thisTrials_Prac[paramName]'.format(paramName))

for thisTrials_Prac in trials_Prac:
    currentLoop = trials_Prac
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Prac.rgb)
    if thisTrials_Prac != None:
        for paramName in thisTrials_Prac:
            exec('{} = thisTrials_Prac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Prac"-------
    # update component parameters for each repeat
    pracResp.keys = []
    pracResp.rt = []
    # keep track of which components have finished
    PracComponents = [pracITI, pracLeft, pracRight, pracResp, pracStatic]
    for thisComponent in PracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Prac"-------
    while continueRoutine:
        # get current time
        t = PracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracITI* updates
        if pracITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracITI.frameNStart = frameN  # exact frame index
            pracITI.tStart = t  # local t and not account for scr refresh
            pracITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracITI, 'tStartRefresh')  # time at next scr refresh
            pracITI.setAutoDraw(True)
        if pracITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracITI.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                pracITI.tStop = t  # not accounting for scr refresh
                pracITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pracITI, 'tStopRefresh')  # time at next scr refresh
                pracITI.setAutoDraw(False)
        
        # *pracLeft* updates
        if pracLeft.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            pracLeft.frameNStart = frameN  # exact frame index
            pracLeft.tStart = t  # local t and not account for scr refresh
            pracLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracLeft, 'tStartRefresh')  # time at next scr refresh
            pracLeft.setAutoDraw(True)
        if pracLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracLeft.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                pracLeft.tStop = t  # not accounting for scr refresh
                pracLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pracLeft, 'tStopRefresh')  # time at next scr refresh
                pracLeft.setAutoDraw(False)
        
        # *pracRight* updates
        if pracRight.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            pracRight.frameNStart = frameN  # exact frame index
            pracRight.tStart = t  # local t and not account for scr refresh
            pracRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracRight, 'tStartRefresh')  # time at next scr refresh
            pracRight.setAutoDraw(True)
        if pracRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracRight.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                pracRight.tStop = t  # not accounting for scr refresh
                pracRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pracRight, 'tStopRefresh')  # time at next scr refresh
                pracRight.setAutoDraw(False)
        
        # *pracResp* updates
        waitOnFlip = False
        if pracResp.status == NOT_STARTED and pracLeft.status==STARTED:
            # keep track of start time/frame for later
            pracResp.frameNStart = frameN  # exact frame index
            pracResp.tStart = t  # local t and not account for scr refresh
            pracResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracResp, 'tStartRefresh')  # time at next scr refresh
            pracResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracResp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                pracResp.tStop = t  # not accounting for scr refresh
                pracResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pracResp, 'tStopRefresh')  # time at next scr refresh
                pracResp.status = FINISHED
        if pracResp.status == STARTED and not waitOnFlip:
            theseKeys = pracResp.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if pracResp.keys == []:  # then this was the first keypress
                    pracResp.keys = theseKeys.name  # just the first key pressed
                    pracResp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (pracResp.keys == str(CorrectAnswer)) or (pracResp.keys == CorrectAnswer):
                        pracResp.corr = 1
                    else:
                        pracResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        # *pracStatic* period
        if pracStatic.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracStatic.frameNStart = frameN  # exact frame index
            pracStatic.tStart = t  # local t and not account for scr refresh
            pracStatic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracStatic, 'tStartRefresh')  # time at next scr refresh
            pracStatic.start(.25)
        elif pracStatic.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *pracStatic*
            pracLeft.setImage(ImageLeft)
            pracRight.setImage(ImageRight)
            # component updates done
            pracStatic.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac"-------
    for thisComponent in PracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Prac.addData('pracITI.started', pracITI.tStartRefresh)
    trials_Prac.addData('pracITI.stopped', pracITI.tStopRefresh)
    trials_Prac.addData('pracLeft.started', pracLeft.tStartRefresh)
    trials_Prac.addData('pracLeft.stopped', pracLeft.tStopRefresh)
    trials_Prac.addData('pracRight.started', pracRight.tStartRefresh)
    trials_Prac.addData('pracRight.stopped', pracRight.tStopRefresh)
    # check responses
    if pracResp.keys in ['', [], None]:  # No response was made
        pracResp.keys = None
        # was no response the correct answer?!
        if str(CorrectAnswer).lower() == 'none':
           pracResp.corr = 1;  # correct non-response
        else:
           pracResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_Prac (TrialHandler)
    trials_Prac.addData('pracResp.keys',pracResp.keys)
    trials_Prac.addData('pracResp.corr', pracResp.corr)
    if pracResp.keys != None:  # we had a response
        trials_Prac.addData('pracResp.rt', pracResp.rt)
    trials_Prac.addData('pracResp.started', pracResp.tStartRefresh)
    trials_Prac.addData('pracResp.stopped', pracResp.tStopRefresh)
    trials_Prac.addData('pracStatic.started', pracStatic.tStart)
    trials_Prac.addData('pracStatic.stopped', pracStatic.tStop)
    # the Routine "Prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PracFeedback"-------
    routineTimer.addTime(1.500000)
    # update component parameters for each repeat
    if pracResp.keys: # if the list isn't empty (i.e., a button was pressed) 
        if pracResp.corr:
            feedbackMsg = "Correct!"
            feedbackImg = "NumberGame_images/check_mark.png"
        elif pracResp.corr == 0:
            feedbackMsg = "Wrong..."
            feedbackImg = "NumberGame_images/x_mark.png"
    else:
        feedbackMsg = "Remember to press a button..."
        feedbackImg = "NumberGame_images/x_mark.png"
        
    # track all prac trials
    pracCorr.append(pracResp.corr)
    feedbackImage.setImage(feedbackImg)
    feedbackText.setText(feedbackMsg)
    # keep track of which components have finished
    PracFeedbackComponents = [feedbackImage, feedbackText]
    for thisComponent in PracFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "PracFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackImage* updates
        if feedbackImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackImage.frameNStart = frameN  # exact frame index
            feedbackImage.tStart = t  # local t and not account for scr refresh
            feedbackImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackImage, 'tStartRefresh')  # time at next scr refresh
            feedbackImage.setAutoDraw(True)
        if feedbackImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackImage.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedbackImage.tStop = t  # not accounting for scr refresh
                feedbackImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackImage, 'tStopRefresh')  # time at next scr refresh
                feedbackImage.setAutoDraw(False)
        
        # *feedbackText* updates
        if feedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackText.frameNStart = frameN  # exact frame index
            feedbackText.tStart = t  # local t and not account for scr refresh
            feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
            feedbackText.setAutoDraw(True)
        if feedbackText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackText.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedbackText.tStop = t  # not accounting for scr refresh
                feedbackText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackText, 'tStopRefresh')  # time at next scr refresh
                feedbackText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracFeedback"-------
    for thisComponent in PracFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #if len(pracCorr) >= minNrPractice:
    #    nCorr=sum(pracCorr[:])
    #    nResps=len(pracCorr[:])
    #    accuracy = nCorr/nResps
        
    #    if accuracy > minAccuracy:
    #        trials_Prac.finished = True
    #        
    trials_Prac.addData('feedbackImage.started', feedbackImage.tStartRefresh)
    trials_Prac.addData('feedbackImage.stopped', feedbackImage.tStopRefresh)
    trials_Prac.addData('feedbackText.started', feedbackText.tStartRefresh)
    trials_Prac.addData('feedbackText.stopped', feedbackText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_Prac'

# get names of stimulus parameters
if trials_Prac.trialList in ([], [None], None):
    params = []
else:
    params = trials_Prac.trialList[0].keys()
# save data for this loop
trials_Prac.saveAsExcel(filename + '.xlsx', sheetName='trials_Prac',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_Prac.saveAsText(filename + 'trials_Prac.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "PracEnd"-------
# update component parameters for each repeat
pracEndClear.keys = []
pracEndClear.rt = []
# keep track of which components have finished
PracEndComponents = [pracITIEnd, pracEnd, pracEndClear]
for thisComponent in PracEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "PracEnd"-------
while continueRoutine:
    # get current time
    t = PracEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pracITIEnd* updates
    if pracITIEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracITIEnd.frameNStart = frameN  # exact frame index
        pracITIEnd.tStart = t  # local t and not account for scr refresh
        pracITIEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracITIEnd, 'tStartRefresh')  # time at next scr refresh
        pracITIEnd.setAutoDraw(True)
    if pracITIEnd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pracITIEnd.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            pracITIEnd.tStop = t  # not accounting for scr refresh
            pracITIEnd.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pracITIEnd, 'tStopRefresh')  # time at next scr refresh
            pracITIEnd.setAutoDraw(False)
    
    # *pracEnd* updates
    if pracEnd.status == NOT_STARTED and pracITIEnd.status==FINISHED:
        # keep track of start time/frame for later
        pracEnd.frameNStart = frameN  # exact frame index
        pracEnd.tStart = t  # local t and not account for scr refresh
        pracEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracEnd, 'tStartRefresh')  # time at next scr refresh
        pracEnd.setAutoDraw(True)
    
    # *pracEndClear* updates
    waitOnFlip = False
    if pracEndClear.status == NOT_STARTED and pracITIEnd.status==FINISHED:
        # keep track of start time/frame for later
        pracEndClear.frameNStart = frameN  # exact frame index
        pracEndClear.tStart = t  # local t and not account for scr refresh
        pracEndClear.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracEndClear, 'tStartRefresh')  # time at next scr refresh
        pracEndClear.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(pracEndClear.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if pracEndClear.status == STARTED and not waitOnFlip:
        theseKeys = pracEndClear.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracEnd"-------
for thisComponent in PracEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('pracITIEnd.started', pracITIEnd.tStartRefresh)
thisExp.addData('pracITIEnd.stopped', pracITIEnd.tStopRefresh)
thisExp.addData('pracEnd.started', pracEnd.tStartRefresh)
thisExp.addData('pracEnd.stopped', pracEnd.tStopRefresh)
# the Routine "PracEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank"-------
routineTimer.addTime(4.000000)
# update component parameters for each repeat
# reset the performance variables
corr =[]
TaskFeedback=''
ACC=''
# keep track of which components have finished
BlankComponents = [blankReady]
for thisComponent in BlankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BlankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BlankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blankReady* updates
    if blankReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blankReady.frameNStart = frameN  # exact frame index
        blankReady.tStart = t  # local t and not account for scr refresh
        blankReady.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blankReady, 'tStartRefresh')  # time at next scr refresh
        blankReady.setAutoDraw(True)
    if blankReady.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blankReady.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            blankReady.tStop = t  # not accounting for scr refresh
            blankReady.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blankReady, 'tStopRefresh')  # time at next scr refresh
            blankReady.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank"-------
for thisComponent in BlankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blankReady.started', blankReady.tStartRefresh)
thisExp.addData('blankReady.stopped', blankReady.tStopRefresh)

# ------Prepare to start Routine "Fix"-------
routineTimer.addTime(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
FixComponents = [fix1]
for thisComponent in FixComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Fix"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FixClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix1* updates
    if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix1.frameNStart = frameN  # exact frame index
        fix1.tStart = t  # local t and not account for scr refresh
        fix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
        fix1.setAutoDraw(True)
    if fix1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix1.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            fix1.tStop = t  # not accounting for scr refresh
            fix1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
            fix1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fix"-------
for thisComponent in FixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix1.started', fix1.tStartRefresh)
thisExp.addData('fix1.stopped', fix1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_Test1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conds/NumberGame_Block1.xlsx'),
    seed=None, name='trials_Test1')
thisExp.addLoop(trials_Test1)  # add the loop to the experiment
thisTrials_Test1 = trials_Test1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_Test1.rgb)
if thisTrials_Test1 != None:
    for paramName in thisTrials_Test1:
        exec('{} = thisTrials_Test1[paramName]'.format(paramName))

for thisTrials_Test1 in trials_Test1:
    currentLoop = trials_Test1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Test1.rgb)
    if thisTrials_Test1 != None:
        for paramName in thisTrials_Test1:
            exec('{} = thisTrials_Test1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Test"-------
    # update component parameters for each repeat
    testResp.keys = []
    testResp.rt = []
    # keep track of which components have finished
    TestComponents = [testITI, testLeft, testRight, testResp, testStatic]
    for thisComponent in TestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Test"-------
    while continueRoutine:
        # get current time
        t = TestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testITI* updates
        if testITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testITI.frameNStart = frameN  # exact frame index
            testITI.tStart = t  # local t and not account for scr refresh
            testITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testITI, 'tStartRefresh')  # time at next scr refresh
            testITI.setAutoDraw(True)
        if testITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testITI.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                testITI.tStop = t  # not accounting for scr refresh
                testITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testITI, 'tStopRefresh')  # time at next scr refresh
                testITI.setAutoDraw(False)
        
        # *testLeft* updates
        if testLeft.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            testLeft.frameNStart = frameN  # exact frame index
            testLeft.tStart = t  # local t and not account for scr refresh
            testLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testLeft, 'tStartRefresh')  # time at next scr refresh
            testLeft.setAutoDraw(True)
        if testLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testLeft.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                testLeft.tStop = t  # not accounting for scr refresh
                testLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testLeft, 'tStopRefresh')  # time at next scr refresh
                testLeft.setAutoDraw(False)
        
        # *testRight* updates
        if testRight.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            testRight.frameNStart = frameN  # exact frame index
            testRight.tStart = t  # local t and not account for scr refresh
            testRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testRight, 'tStartRefresh')  # time at next scr refresh
            testRight.setAutoDraw(True)
        if testRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testRight.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                testRight.tStop = t  # not accounting for scr refresh
                testRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testRight, 'tStopRefresh')  # time at next scr refresh
                testRight.setAutoDraw(False)
        
        # *testResp* updates
        waitOnFlip = False
        if testResp.status == NOT_STARTED and testLeft.status==STARTED:
            # keep track of start time/frame for later
            testResp.frameNStart = frameN  # exact frame index
            testResp.tStart = t  # local t and not account for scr refresh
            testResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testResp, 'tStartRefresh')  # time at next scr refresh
            testResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(testResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(testResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if testResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testResp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                testResp.tStop = t  # not accounting for scr refresh
                testResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testResp, 'tStopRefresh')  # time at next scr refresh
                testResp.status = FINISHED
        if testResp.status == STARTED and not waitOnFlip:
            theseKeys = testResp.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if testResp.keys == []:  # then this was the first keypress
                    testResp.keys = theseKeys.name  # just the first key pressed
                    testResp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (testResp.keys == str(CorrectAnswer)) or (testResp.keys == CorrectAnswer):
                        testResp.corr = 1
                    else:
                        testResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        # *testStatic* period
        if testStatic.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testStatic.frameNStart = frameN  # exact frame index
            testStatic.tStart = t  # local t and not account for scr refresh
            testStatic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testStatic, 'tStartRefresh')  # time at next scr refresh
            testStatic.start(.25)
        elif testStatic.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *testStatic*
            testLeft.setImage(ImageLeft)
            testRight.setImage(ImageRight)
            # component updates done
            testStatic.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test"-------
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Test1.addData('testITI.started', testITI.tStartRefresh)
    trials_Test1.addData('testITI.stopped', testITI.tStopRefresh)
    trials_Test1.addData('testLeft.started', testLeft.tStartRefresh)
    trials_Test1.addData('testLeft.stopped', testLeft.tStopRefresh)
    trials_Test1.addData('testRight.started', testRight.tStartRefresh)
    trials_Test1.addData('testRight.stopped', testRight.tStopRefresh)
    # check responses
    if testResp.keys in ['', [], None]:  # No response was made
        testResp.keys = None
        # was no response the correct answer?!
        if str(CorrectAnswer).lower() == 'none':
           testResp.corr = 1;  # correct non-response
        else:
           testResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_Test1 (TrialHandler)
    trials_Test1.addData('testResp.keys',testResp.keys)
    trials_Test1.addData('testResp.corr', testResp.corr)
    if testResp.keys != None:  # we had a response
        trials_Test1.addData('testResp.rt', testResp.rt)
    trials_Test1.addData('testResp.started', testResp.tStartRefresh)
    trials_Test1.addData('testResp.stopped', testResp.tStopRefresh)
    trials_Test1.addData('testStatic.started', testStatic.tStart)
    trials_Test1.addData('testStatic.stopped', testStatic.tStop)
    # the Routine "Test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trlTrack"-------
    # update component parameters for each repeat
    # add to object "corr"
    corr.append(testResp.corr)
    # keep track of which components have finished
    trlTrackComponents = []
    for thisComponent in trlTrackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trlTrackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trlTrack"-------
    while continueRoutine:
        # get current time
        t = trlTrackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trlTrackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trlTrackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trlTrack"-------
    for thisComponent in trlTrackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trlTrack" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_Test1'

# get names of stimulus parameters
if trials_Test1.trialList in ([], [None], None):
    params = []
else:
    params = trials_Test1.trialList[0].keys()
# save data for this loop
trials_Test1.saveAsExcel(filename + '.xlsx', sheetName='trials_Test1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_Test1.saveAsText(filename + 'trials_Test1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "TaskFeedback"-------
# update component parameters for each repeat
# tabulate accuracy of all test trials
nCorr=sum(corr[:])
nResps=len(corr[:])
TaskFeedback=""
ACC=nCorr/nResps
TaskFeedbackText.setText(TaskFeedback)
breakEnd.keys = []
breakEnd.rt = []
# keep track of which components have finished
TaskFeedbackComponents = [blockBreak, TaskFeedbackText, breakEnd]
for thisComponent in TaskFeedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TaskFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "TaskFeedback"-------
while continueRoutine:
    # get current time
    t = TaskFeedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TaskFeedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blockBreak* updates
    if blockBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blockBreak.frameNStart = frameN  # exact frame index
        blockBreak.tStart = t  # local t and not account for scr refresh
        blockBreak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blockBreak, 'tStartRefresh')  # time at next scr refresh
        blockBreak.setAutoDraw(True)
    
    # *TaskFeedbackText* updates
    if TaskFeedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TaskFeedbackText.frameNStart = frameN  # exact frame index
        TaskFeedbackText.tStart = t  # local t and not account for scr refresh
        TaskFeedbackText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TaskFeedbackText, 'tStartRefresh')  # time at next scr refresh
        TaskFeedbackText.setAutoDraw(True)
    
    # *breakEnd* updates
    waitOnFlip = False
    if breakEnd.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        breakEnd.frameNStart = frameN  # exact frame index
        breakEnd.tStart = t  # local t and not account for scr refresh
        breakEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(breakEnd, 'tStartRefresh')  # time at next scr refresh
        breakEnd.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(breakEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if breakEnd.status == STARTED and not waitOnFlip:
        theseKeys = breakEnd.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TaskFeedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TaskFeedback"-------
for thisComponent in TaskFeedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blockBreak.started', blockBreak.tStartRefresh)
thisExp.addData('blockBreak.stopped', blockBreak.tStopRefresh)
thisExp.addData('TaskFeedbackText.started', TaskFeedbackText.tStartRefresh)
thisExp.addData('TaskFeedbackText.stopped', TaskFeedbackText.tStopRefresh)
# the Routine "TaskFeedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank"-------
routineTimer.addTime(4.000000)
# update component parameters for each repeat
# reset the performance variables
corr =[]
TaskFeedback=''
ACC=''
# keep track of which components have finished
BlankComponents = [blankReady]
for thisComponent in BlankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BlankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BlankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blankReady* updates
    if blankReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blankReady.frameNStart = frameN  # exact frame index
        blankReady.tStart = t  # local t and not account for scr refresh
        blankReady.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blankReady, 'tStartRefresh')  # time at next scr refresh
        blankReady.setAutoDraw(True)
    if blankReady.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blankReady.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            blankReady.tStop = t  # not accounting for scr refresh
            blankReady.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blankReady, 'tStopRefresh')  # time at next scr refresh
            blankReady.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank"-------
for thisComponent in BlankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blankReady.started', blankReady.tStartRefresh)
thisExp.addData('blankReady.stopped', blankReady.tStopRefresh)

# ------Prepare to start Routine "Fix"-------
routineTimer.addTime(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
FixComponents = [fix1]
for thisComponent in FixComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Fix"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FixClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix1* updates
    if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix1.frameNStart = frameN  # exact frame index
        fix1.tStart = t  # local t and not account for scr refresh
        fix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
        fix1.setAutoDraw(True)
    if fix1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix1.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            fix1.tStop = t  # not accounting for scr refresh
            fix1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
            fix1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fix"-------
for thisComponent in FixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix1.started', fix1.tStartRefresh)
thisExp.addData('fix1.stopped', fix1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_Test2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conds/NumberGame_Block2.xlsx'),
    seed=None, name='trials_Test2')
thisExp.addLoop(trials_Test2)  # add the loop to the experiment
thisTrials_Test2 = trials_Test2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_Test2.rgb)
if thisTrials_Test2 != None:
    for paramName in thisTrials_Test2:
        exec('{} = thisTrials_Test2[paramName]'.format(paramName))

for thisTrials_Test2 in trials_Test2:
    currentLoop = trials_Test2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Test2.rgb)
    if thisTrials_Test2 != None:
        for paramName in thisTrials_Test2:
            exec('{} = thisTrials_Test2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Test"-------
    # update component parameters for each repeat
    testResp.keys = []
    testResp.rt = []
    # keep track of which components have finished
    TestComponents = [testITI, testLeft, testRight, testResp, testStatic]
    for thisComponent in TestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Test"-------
    while continueRoutine:
        # get current time
        t = TestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testITI* updates
        if testITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testITI.frameNStart = frameN  # exact frame index
            testITI.tStart = t  # local t and not account for scr refresh
            testITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testITI, 'tStartRefresh')  # time at next scr refresh
            testITI.setAutoDraw(True)
        if testITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testITI.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                testITI.tStop = t  # not accounting for scr refresh
                testITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testITI, 'tStopRefresh')  # time at next scr refresh
                testITI.setAutoDraw(False)
        
        # *testLeft* updates
        if testLeft.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            testLeft.frameNStart = frameN  # exact frame index
            testLeft.tStart = t  # local t and not account for scr refresh
            testLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testLeft, 'tStartRefresh')  # time at next scr refresh
            testLeft.setAutoDraw(True)
        if testLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testLeft.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                testLeft.tStop = t  # not accounting for scr refresh
                testLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testLeft, 'tStopRefresh')  # time at next scr refresh
                testLeft.setAutoDraw(False)
        
        # *testRight* updates
        if testRight.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            testRight.frameNStart = frameN  # exact frame index
            testRight.tStart = t  # local t and not account for scr refresh
            testRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testRight, 'tStartRefresh')  # time at next scr refresh
            testRight.setAutoDraw(True)
        if testRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testRight.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                testRight.tStop = t  # not accounting for scr refresh
                testRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testRight, 'tStopRefresh')  # time at next scr refresh
                testRight.setAutoDraw(False)
        
        # *testResp* updates
        waitOnFlip = False
        if testResp.status == NOT_STARTED and testLeft.status==STARTED:
            # keep track of start time/frame for later
            testResp.frameNStart = frameN  # exact frame index
            testResp.tStart = t  # local t and not account for scr refresh
            testResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testResp, 'tStartRefresh')  # time at next scr refresh
            testResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(testResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(testResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if testResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testResp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                testResp.tStop = t  # not accounting for scr refresh
                testResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testResp, 'tStopRefresh')  # time at next scr refresh
                testResp.status = FINISHED
        if testResp.status == STARTED and not waitOnFlip:
            theseKeys = testResp.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if testResp.keys == []:  # then this was the first keypress
                    testResp.keys = theseKeys.name  # just the first key pressed
                    testResp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (testResp.keys == str(CorrectAnswer)) or (testResp.keys == CorrectAnswer):
                        testResp.corr = 1
                    else:
                        testResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        # *testStatic* period
        if testStatic.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testStatic.frameNStart = frameN  # exact frame index
            testStatic.tStart = t  # local t and not account for scr refresh
            testStatic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testStatic, 'tStartRefresh')  # time at next scr refresh
            testStatic.start(.25)
        elif testStatic.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *testStatic*
            testLeft.setImage(ImageLeft)
            testRight.setImage(ImageRight)
            # component updates done
            testStatic.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test"-------
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_Test2.addData('testITI.started', testITI.tStartRefresh)
    trials_Test2.addData('testITI.stopped', testITI.tStopRefresh)
    trials_Test2.addData('testLeft.started', testLeft.tStartRefresh)
    trials_Test2.addData('testLeft.stopped', testLeft.tStopRefresh)
    trials_Test2.addData('testRight.started', testRight.tStartRefresh)
    trials_Test2.addData('testRight.stopped', testRight.tStopRefresh)
    # check responses
    if testResp.keys in ['', [], None]:  # No response was made
        testResp.keys = None
        # was no response the correct answer?!
        if str(CorrectAnswer).lower() == 'none':
           testResp.corr = 1;  # correct non-response
        else:
           testResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_Test2 (TrialHandler)
    trials_Test2.addData('testResp.keys',testResp.keys)
    trials_Test2.addData('testResp.corr', testResp.corr)
    if testResp.keys != None:  # we had a response
        trials_Test2.addData('testResp.rt', testResp.rt)
    trials_Test2.addData('testResp.started', testResp.tStartRefresh)
    trials_Test2.addData('testResp.stopped', testResp.tStopRefresh)
    trials_Test2.addData('testStatic.started', testStatic.tStart)
    trials_Test2.addData('testStatic.stopped', testStatic.tStop)
    # the Routine "Test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trlTrack"-------
    # update component parameters for each repeat
    # add to object "corr"
    corr.append(testResp.corr)
    # keep track of which components have finished
    trlTrackComponents = []
    for thisComponent in trlTrackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trlTrackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trlTrack"-------
    while continueRoutine:
        # get current time
        t = trlTrackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trlTrackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trlTrackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trlTrack"-------
    for thisComponent in trlTrackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trlTrack" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_Test2'

# get names of stimulus parameters
if trials_Test2.trialList in ([], [None], None):
    params = []
else:
    params = trials_Test2.trialList[0].keys()
# save data for this loop
trials_Test2.saveAsExcel(filename + '.xlsx', sheetName='trials_Test2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_Test2.saveAsText(filename + 'trials_Test2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
routineTimer.addTime(5.000000)
# update component parameters for each repeat
# tabulate accuracy of all test trials
nCorr=sum(corr[:])
nResps=len(corr[:])
TaskFeedback=""  #"{} / {}".format(nCorr, nResps)
ACC=nCorr/nResps
TaskFeedbackText2.setText(TaskFeedback)
# keep track of which components have finished
EndComponents = [TaskFeedbackText2, endInstr]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TaskFeedbackText2* updates
    if TaskFeedbackText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TaskFeedbackText2.frameNStart = frameN  # exact frame index
        TaskFeedbackText2.tStart = t  # local t and not account for scr refresh
        TaskFeedbackText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TaskFeedbackText2, 'tStartRefresh')  # time at next scr refresh
        TaskFeedbackText2.setAutoDraw(True)
    if TaskFeedbackText2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > TaskFeedbackText2.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            TaskFeedbackText2.tStop = t  # not accounting for scr refresh
            TaskFeedbackText2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(TaskFeedbackText2, 'tStopRefresh')  # time at next scr refresh
            TaskFeedbackText2.setAutoDraw(False)
    
    # *endInstr* updates
    if endInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endInstr.frameNStart = frameN  # exact frame index
        endInstr.tStart = t  # local t and not account for scr refresh
        endInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endInstr, 'tStartRefresh')  # time at next scr refresh
        endInstr.setAutoDraw(True)
    if endInstr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endInstr.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            endInstr.tStop = t  # not accounting for scr refresh
            endInstr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endInstr, 'tStopRefresh')  # time at next scr refresh
            endInstr.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TaskFeedbackText2.started', TaskFeedbackText2.tStartRefresh)
thisExp.addData('TaskFeedbackText2.stopped', TaskFeedbackText2.tStopRefresh)
thisExp.addData('endInstr.started', endInstr.tStartRefresh)
thisExp.addData('endInstr.stopped', endInstr.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
