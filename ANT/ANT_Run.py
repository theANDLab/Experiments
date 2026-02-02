#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.2),
    on February 17, 2025, at 14:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.2'
expName = 'ANT-C'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1200]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_visit%s_%s_%s' % (expInfo['participant'], expInfo['session'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\andlab.AS-LF315-1\\Documents\\Experiments\\ANT\\ANT-C.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowStencil=False,
            monitor='Eizo', color='aqua', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'aqua'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('pracResp1') is None:
        # initialise pracResp1
        pracResp1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='pracResp1',
        )
    if deviceManager.getDevice('practResp2') is None:
        # initialise practResp2
        practResp2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='practResp2',
        )
    if deviceManager.getDevice('resp') is None:
        # initialise resp
        resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp',
        )
    if deviceManager.getDevice('practResp3') is None:
        # initialise practResp3
        practResp3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='practResp3',
        )
    if deviceManager.getDevice('instResp') is None:
        # initialise instResp
        instResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instResp',
        )
    if deviceManager.getDevice('restResp') is None:
        # initialise restResp
        restResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='restResp',
        )
    if deviceManager.getDevice('endKey') is None:
        # initialise endKey
        endKey = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='endKey',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "PracInstruc" ---
    pracText1 = visual.TextStim(win=win, name='pracText1',
        text='The Fish Tank!\n\n\n\n\n\n\n\nSPACE  to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    pracResp1 = keyboard.Keyboard(deviceName='pracResp1')
    logo = visual.ImageStim(
        win=win,
        name='logo', 
        image='stim/introFish.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=[1,.8],
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    intro_bubbles = visual.ImageStim(
        win=win,
        name='intro_bubbles', 
        image='stim/big_bubbles.png', mask=None, anchor='center',
        ori=20.0, pos=(.7, .1), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "PracInstruct2" ---
    practInst2 = visual.TextStim(win=win, name='practInst2',
        text='In this game you will see rows of fish like this:\n\n\n\nPress the button ← or → that matches the direction of the MIDDLE fish!\n\nLook out for bubbles!\n\nThey tell you where the fish might pop up next!\n\nTry to answer as fast and as accurately as you can! \nPress SPACE to practice!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    practResp2 = keyboard.Keyboard(deviceName='practResp2')
    intro_img_2 = visual.ImageStim(
        win=win,
        name='intro_img_2', 
        image='stim/lincon.png', mask=None, anchor='center',
        ori=0.0, pos=(-.3, .2), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    intro_img_22 = visual.ImageStim(
        win=win,
        name='intro_img_22', 
        image='stim/rcon.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, .2), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    intro_bubs_2 = visual.ImageStim(
        win=win,
        name='intro_bubs_2', 
        image='stim/bubbles.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25,-0.03), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    
    # --- Initialize components for Routine "fixation" ---
    # Run 'Begin Experiment' code from jitterFixCross
    fixDuration  = .4
    image = visual.ImageStim(
        win=win,
        name='image', units='pix', 
        image='stim/fix.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "trial" ---
    top_cue = visual.ImageStim(
        win=win,
        name='top_cue', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=None, draggable=False, size=(19,22),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    cent_cue = visual.ImageStim(
        win=win,
        name='cent_cue', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(19,22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    bot_cue = visual.ImageStim(
        win=win,
        name='bot_cue', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=None, draggable=False, size=(19,22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    target_img = visual.ImageStim(
        win=win,
        name='target_img', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0,0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
    resp = keyboard.Keyboard(deviceName='resp')
    fixationshort = visual.ImageStim(
        win=win,
        name='fixationshort', units='pix', 
        image='stim/fix.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    # Run 'Begin Experiment' code from setTargetLoc
    targ_offset = 67
    # Run 'Begin Experiment' code from setFixStartTime
    fixStartTime = 0.0
    
    # --- Initialize components for Routine "feedback" ---
    fbk_text = visual.TextStim(win=win, name='fbk_text',
        text=' ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from fdbk_code
    msg = ""
    msg2 = ""
    score = 0 #Keep track of how many practice trials have been correct
    prac_count = 0 #Keep track of how many times pt has done the practice trials
    
    # --- Initialize components for Routine "PracInstruc3" ---
    pracInst3 = visual.TextStim(win=win, name='pracInst3',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    practResp3 = keyboard.Keyboard(deviceName='practResp3')
    
    # --- Initialize components for Routine "MainInstruc" ---
    mainInst = visual.TextStim(win=win, name='mainInst',
        text="Now let's play the real game! This time we won't tell you if you were right or wrong. Try to be as quick and accurate as you can!\n\nThere will be 3 rounds and you can choose to take a break after each one. \n\nAre you ready?",
        font='Arial',
        units='height', pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instResp = keyboard.Keyboard(deviceName='instResp')
    
    # --- Initialize components for Routine "fixation" ---
    # Run 'Begin Experiment' code from jitterFixCross
    fixDuration  = .4
    image = visual.ImageStim(
        win=win,
        name='image', units='pix', 
        image='stim/fix.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "trial" ---
    top_cue = visual.ImageStim(
        win=win,
        name='top_cue', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=None, draggable=False, size=(19,22),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    cent_cue = visual.ImageStim(
        win=win,
        name='cent_cue', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(19,22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    bot_cue = visual.ImageStim(
        win=win,
        name='bot_cue', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=None, draggable=False, size=(19,22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    target_img = visual.ImageStim(
        win=win,
        name='target_img', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0,0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
    resp = keyboard.Keyboard(deviceName='resp')
    fixationshort = visual.ImageStim(
        win=win,
        name='fixationshort', units='pix', 
        image='stim/fix.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    # Run 'Begin Experiment' code from setTargetLoc
    targ_offset = 67
    # Run 'Begin Experiment' code from setFixStartTime
    fixStartTime = 0.0
    
    # --- Initialize components for Routine "Rest" ---
    rest = visual.TextStim(win=win, name='rest',
        text='Good job on this round!\n\nTake a quick break. \n\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    restResp = keyboard.Keyboard(deviceName='restResp')
    
    # --- Initialize components for Routine "End" ---
    endText = visual.TextStim(win=win, name='endText',
        text='You fed all the fish!!\n\n\n\n\n\n\nThanks for playing!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.09, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    endKey = keyboard.Keyboard(deviceName='endKey')
    flippy_fish = visual.ImageStim(
        win=win,
        name='flippy_fish', 
        image='stim/introFish.png', mask=None, anchor='center',
        ori=1.0, pos=(0, .1), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "PracInstruc" ---
    # create an object to store info about Routine PracInstruc
    PracInstruc = data.Routine(
        name='PracInstruc',
        components=[pracText1, pracResp1, logo, intro_bubbles],
    )
    PracInstruc.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for pracResp1
    pracResp1.keys = []
    pracResp1.rt = []
    _pracResp1_allKeys = []
    # store start times for PracInstruc
    PracInstruc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PracInstruc.tStart = globalClock.getTime(format='float')
    PracInstruc.status = STARTED
    thisExp.addData('PracInstruc.started', PracInstruc.tStart)
    PracInstruc.maxDuration = None
    # keep track of which components have finished
    PracInstrucComponents = PracInstruc.components
    for thisComponent in PracInstruc.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PracInstruc" ---
    PracInstruc.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracText1* updates
        
        # if pracText1 is starting this frame...
        if pracText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracText1.frameNStart = frameN  # exact frame index
            pracText1.tStart = t  # local t and not account for scr refresh
            pracText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracText1, 'tStartRefresh')  # time at next scr refresh
            # update status
            pracText1.status = STARTED
            pracText1.setAutoDraw(True)
        
        # if pracText1 is active this frame...
        if pracText1.status == STARTED:
            # update params
            pass
        
        # *pracResp1* updates
        waitOnFlip = False
        
        # if pracResp1 is starting this frame...
        if pracResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracResp1.frameNStart = frameN  # exact frame index
            pracResp1.tStart = t  # local t and not account for scr refresh
            pracResp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracResp1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracResp1.started')
            # update status
            pracResp1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracResp1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracResp1.status == STARTED and not waitOnFlip:
            theseKeys = pracResp1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _pracResp1_allKeys.extend(theseKeys)
            if len(_pracResp1_allKeys):
                pracResp1.keys = _pracResp1_allKeys[-1].name  # just the last key pressed
                pracResp1.rt = _pracResp1_allKeys[-1].rt
                pracResp1.duration = _pracResp1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *logo* updates
        
        # if logo is starting this frame...
        if logo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            logo.frameNStart = frameN  # exact frame index
            logo.tStart = t  # local t and not account for scr refresh
            logo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(logo, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'logo.started')
            # update status
            logo.status = STARTED
            logo.setAutoDraw(True)
        
        # if logo is active this frame...
        if logo.status == STARTED:
            # update params
            pass
        
        # *intro_bubbles* updates
        
        # if intro_bubbles is starting this frame...
        if intro_bubbles.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_bubbles.frameNStart = frameN  # exact frame index
            intro_bubbles.tStart = t  # local t and not account for scr refresh
            intro_bubbles.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_bubbles, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro_bubbles.started')
            # update status
            intro_bubbles.status = STARTED
            intro_bubbles.setAutoDraw(True)
        
        # if intro_bubbles is active this frame...
        if intro_bubbles.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PracInstruc.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracInstruc.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PracInstruc" ---
    for thisComponent in PracInstruc.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PracInstruc
    PracInstruc.tStop = globalClock.getTime(format='float')
    PracInstruc.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PracInstruc.stopped', PracInstruc.tStop)
    thisExp.nextEntry()
    # the Routine "PracInstruc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    rep_pracLoop = data.TrialHandler2(
        name='rep_pracLoop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(rep_pracLoop)  # add the loop to the experiment
    thisRep_pracLoop = rep_pracLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRep_pracLoop.rgb)
    if thisRep_pracLoop != None:
        for paramName in thisRep_pracLoop:
            globals()[paramName] = thisRep_pracLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisRep_pracLoop in rep_pracLoop:
        currentLoop = rep_pracLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisRep_pracLoop.rgb)
        if thisRep_pracLoop != None:
            for paramName in thisRep_pracLoop:
                globals()[paramName] = thisRep_pracLoop[paramName]
        
        # --- Prepare to start Routine "PracInstruct2" ---
        # create an object to store info about Routine PracInstruct2
        PracInstruct2 = data.Routine(
            name='PracInstruct2',
            components=[practInst2, practResp2, intro_img_2, intro_img_22, intro_bubs_2],
        )
        PracInstruct2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for practResp2
        practResp2.keys = []
        practResp2.rt = []
        _practResp2_allKeys = []
        # store start times for PracInstruct2
        PracInstruct2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracInstruct2.tStart = globalClock.getTime(format='float')
        PracInstruct2.status = STARTED
        thisExp.addData('PracInstruct2.started', PracInstruct2.tStart)
        PracInstruct2.maxDuration = None
        # keep track of which components have finished
        PracInstruct2Components = PracInstruct2.components
        for thisComponent in PracInstruct2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PracInstruct2" ---
        # if trial has changed, end Routine now
        if isinstance(rep_pracLoop, data.TrialHandler2) and thisRep_pracLoop.thisN != rep_pracLoop.thisTrial.thisN:
            continueRoutine = False
        PracInstruct2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practInst2* updates
            
            # if practInst2 is starting this frame...
            if practInst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practInst2.frameNStart = frameN  # exact frame index
                practInst2.tStart = t  # local t and not account for scr refresh
                practInst2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practInst2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practInst2.started')
                # update status
                practInst2.status = STARTED
                practInst2.setAutoDraw(True)
            
            # if practInst2 is active this frame...
            if practInst2.status == STARTED:
                # update params
                pass
            
            # *practResp2* updates
            waitOnFlip = False
            
            # if practResp2 is starting this frame...
            if practResp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practResp2.frameNStart = frameN  # exact frame index
                practResp2.tStart = t  # local t and not account for scr refresh
                practResp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practResp2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practResp2.started')
                # update status
                practResp2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practResp2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practResp2.status == STARTED and not waitOnFlip:
                theseKeys = practResp2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _practResp2_allKeys.extend(theseKeys)
                if len(_practResp2_allKeys):
                    practResp2.keys = _practResp2_allKeys[-1].name  # just the last key pressed
                    practResp2.rt = _practResp2_allKeys[-1].rt
                    practResp2.duration = _practResp2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *intro_img_2* updates
            
            # if intro_img_2 is starting this frame...
            if intro_img_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intro_img_2.frameNStart = frameN  # exact frame index
                intro_img_2.tStart = t  # local t and not account for scr refresh
                intro_img_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intro_img_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'intro_img_2.started')
                # update status
                intro_img_2.status = STARTED
                intro_img_2.setAutoDraw(True)
            
            # if intro_img_2 is active this frame...
            if intro_img_2.status == STARTED:
                # update params
                pass
            
            # *intro_img_22* updates
            
            # if intro_img_22 is starting this frame...
            if intro_img_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intro_img_22.frameNStart = frameN  # exact frame index
                intro_img_22.tStart = t  # local t and not account for scr refresh
                intro_img_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intro_img_22, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'intro_img_22.started')
                # update status
                intro_img_22.status = STARTED
                intro_img_22.setAutoDraw(True)
            
            # if intro_img_22 is active this frame...
            if intro_img_22.status == STARTED:
                # update params
                pass
            
            # *intro_bubs_2* updates
            
            # if intro_bubs_2 is starting this frame...
            if intro_bubs_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intro_bubs_2.frameNStart = frameN  # exact frame index
                intro_bubs_2.tStart = t  # local t and not account for scr refresh
                intro_bubs_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intro_bubs_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'intro_bubs_2.started')
                # update status
                intro_bubs_2.status = STARTED
                intro_bubs_2.setAutoDraw(True)
            
            # if intro_bubs_2 is active this frame...
            if intro_bubs_2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracInstruct2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracInstruct2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracInstruct2" ---
        for thisComponent in PracInstruct2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracInstruct2
        PracInstruct2.tStop = globalClock.getTime(format='float')
        PracInstruct2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracInstruct2.stopped', PracInstruct2.tStop)
        # the Routine "PracInstruct2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        pracLoop = data.TrialHandler2(
            name='pracLoop',
            nReps=1, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(
            'conds/prac_conds.csv', 
        )
        , 
            seed=None, 
        )
        thisExp.addLoop(pracLoop)  # add the loop to the experiment
        thisPracLoop = pracLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPracLoop.rgb)
        if thisPracLoop != None:
            for paramName in thisPracLoop:
                globals()[paramName] = thisPracLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPracLoop in pracLoop:
            currentLoop = pracLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPracLoop.rgb)
            if thisPracLoop != None:
                for paramName in thisPracLoop:
                    globals()[paramName] = thisPracLoop[paramName]
            
            # --- Prepare to start Routine "fixation" ---
            # create an object to store info about Routine fixation
            fixation = data.Routine(
                name='fixation',
                components=[image],
            )
            fixation.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from jitterFixCross
            durations = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]  # Create durations 
            shuffle(durations)  # Randomize durations 
            fixDuration  = durations[0] # Take one of the randomized durations
            # store start times for fixation
            fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation.tStart = globalClock.getTime(format='float')
            fixation.status = STARTED
            thisExp.addData('fixation.started', fixation.tStart)
            fixation.maxDuration = None
            # keep track of which components have finished
            fixationComponents = fixation.components
            for thisComponent in fixation.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            # if trial has changed, end Routine now
            if isinstance(pracLoop, data.TrialHandler2) and thisPracLoop.thisN != pracLoop.thisTrial.thisN:
                continueRoutine = False
            fixation.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                
                # if image is starting this frame...
                if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.started')
                    # update status
                    image.status = STARTED
                    image.setAutoDraw(True)
                
                # if image is active this frame...
                if image.status == STARTED:
                    # update params
                    pass
                
                # if image is stopping this frame...
                if image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image.tStartRefresh + fixDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.tStopRefresh = tThisFlipGlobal  # on global time
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        # update status
                        image.status = FINISHED
                        image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    fixation.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation
            fixation.tStop = globalClock.getTime(format='float')
            fixation.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation.stopped', fixation.tStop)
            # Run 'End Routine' code from jitterFixCross
            thisExp.addData("fixDuration", fixDuration)
            # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[top_cue, cent_cue, bot_cue, target_img, resp, fixationshort],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            top_cue.setImage(upper_cue)
            cent_cue.setImage(center_cue)
            bot_cue.setImage(lower_cue)
            target_img.setImage(targetFile)
            # create starting attributes for resp
            resp.keys = []
            resp.rt = []
            _resp_allKeys = []
            # Run 'Begin Routine' code from setTargetLoc
            if targetLoc == 'upper':
                target_img.pos = (0, targ_offset)
            elif targetLoc == 'lower':
                target_img.pos = (0, 0-targ_offset)
                
            top_cue.pos = (0, targ_offset)
            bot_cue.pos = (0, 0-targ_offset)
            
                
            # Run 'Begin Routine' code from setFixStartTime
            if cue == 'center':
                fixStartTime = 0.15
            else: fixStartTime = 0.0
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            # if trial has changed, end Routine now
            if isinstance(pracLoop, data.TrialHandler2) and thisPracLoop.thisN != pracLoop.thisTrial.thisN:
                continueRoutine = False
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *top_cue* updates
                
                # if top_cue is starting this frame...
                if top_cue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    top_cue.frameNStart = frameN  # exact frame index
                    top_cue.tStart = t  # local t and not account for scr refresh
                    top_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(top_cue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'top_cue.started')
                    # update status
                    top_cue.status = STARTED
                    top_cue.setAutoDraw(True)
                
                # if top_cue is active this frame...
                if top_cue.status == STARTED:
                    # update params
                    pass
                
                # if top_cue is stopping this frame...
                if top_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > top_cue.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        top_cue.tStop = t  # not accounting for scr refresh
                        top_cue.tStopRefresh = tThisFlipGlobal  # on global time
                        top_cue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'top_cue.stopped')
                        # update status
                        top_cue.status = FINISHED
                        top_cue.setAutoDraw(False)
                
                # *cent_cue* updates
                
                # if cent_cue is starting this frame...
                if cent_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cent_cue.frameNStart = frameN  # exact frame index
                    cent_cue.tStart = t  # local t and not account for scr refresh
                    cent_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cent_cue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cent_cue.started')
                    # update status
                    cent_cue.status = STARTED
                    cent_cue.setAutoDraw(True)
                
                # if cent_cue is active this frame...
                if cent_cue.status == STARTED:
                    # update params
                    pass
                
                # if cent_cue is stopping this frame...
                if cent_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cent_cue.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        cent_cue.tStop = t  # not accounting for scr refresh
                        cent_cue.tStopRefresh = tThisFlipGlobal  # on global time
                        cent_cue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'cent_cue.stopped')
                        # update status
                        cent_cue.status = FINISHED
                        cent_cue.setAutoDraw(False)
                
                # *bot_cue* updates
                
                # if bot_cue is starting this frame...
                if bot_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    bot_cue.frameNStart = frameN  # exact frame index
                    bot_cue.tStart = t  # local t and not account for scr refresh
                    bot_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(bot_cue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bot_cue.started')
                    # update status
                    bot_cue.status = STARTED
                    bot_cue.setAutoDraw(True)
                
                # if bot_cue is active this frame...
                if bot_cue.status == STARTED:
                    # update params
                    pass
                
                # if bot_cue is stopping this frame...
                if bot_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > bot_cue.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        bot_cue.tStop = t  # not accounting for scr refresh
                        bot_cue.tStopRefresh = tThisFlipGlobal  # on global time
                        bot_cue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'bot_cue.stopped')
                        # update status
                        bot_cue.status = FINISHED
                        bot_cue.setAutoDraw(False)
                
                # *target_img* updates
                
                # if target_img is starting this frame...
                if target_img.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    target_img.frameNStart = frameN  # exact frame index
                    target_img.tStart = t  # local t and not account for scr refresh
                    target_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_img.started')
                    # update status
                    target_img.status = STARTED
                    target_img.setAutoDraw(True)
                
                # if target_img is active this frame...
                if target_img.status == STARTED:
                    # update params
                    pass
                
                # if target_img is stopping this frame...
                if target_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_img.tStartRefresh + 1.7-frameTolerance:
                        # keep track of stop time/frame for later
                        target_img.tStop = t  # not accounting for scr refresh
                        target_img.tStopRefresh = tThisFlipGlobal  # on global time
                        target_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'target_img.stopped')
                        # update status
                        target_img.status = FINISHED
                        target_img.setAutoDraw(False)
                
                # *resp* updates
                waitOnFlip = False
                
                # if resp is starting this frame...
                if resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    resp.frameNStart = frameN  # exact frame index
                    resp.tStart = t  # local t and not account for scr refresh
                    resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp.started')
                    # update status
                    resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if resp is stopping this frame...
                if resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > resp.tStartRefresh + 1.7-frameTolerance:
                        # keep track of stop time/frame for later
                        resp.tStop = t  # not accounting for scr refresh
                        resp.tStopRefresh = tThisFlipGlobal  # on global time
                        resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp.stopped')
                        # update status
                        resp.status = FINISHED
                        resp.status = FINISHED
                if resp.status == STARTED and not waitOnFlip:
                    theseKeys = resp.getKeys(keyList=['1','2'], ignoreKeys=["escape"], waitRelease=False)
                    _resp_allKeys.extend(theseKeys)
                    if len(_resp_allKeys):
                        resp.keys = _resp_allKeys[0].name  # just the first key pressed
                        resp.rt = _resp_allKeys[0].rt
                        resp.duration = _resp_allKeys[0].duration
                        # was this correct?
                        if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                            resp.corr = 1
                        else:
                            resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *fixationshort* updates
                
                # if fixationshort is starting this frame...
                if fixationshort.status == NOT_STARTED and tThisFlip >= fixStartTime-frameTolerance:
                    # keep track of start time/frame for later
                    fixationshort.frameNStart = frameN  # exact frame index
                    fixationshort.tStart = t  # local t and not account for scr refresh
                    fixationshort.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixationshort, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationshort.started')
                    # update status
                    fixationshort.status = STARTED
                    fixationshort.setAutoDraw(True)
                
                # if fixationshort is active this frame...
                if fixationshort.status == STARTED:
                    # update params
                    pass
                
                # if fixationshort is stopping this frame...
                if fixationshort.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixationshort.tStartRefresh + 2.2-frameTolerance:
                        # keep track of stop time/frame for later
                        fixationshort.tStop = t  # not accounting for scr refresh
                        fixationshort.tStopRefresh = tThisFlipGlobal  # on global time
                        fixationshort.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixationshort.stopped')
                        # update status
                        fixationshort.status = FINISHED
                        fixationshort.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # check responses
            if resp.keys in ['', [], None]:  # No response was made
                resp.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   resp.corr = 1;  # correct non-response
                else:
                   resp.corr = 0;  # failed to respond (incorrectly)
            # store data for pracLoop (TrialHandler)
            pracLoop.addData('resp.keys',resp.keys)
            pracLoop.addData('resp.corr', resp.corr)
            if resp.keys != None:  # we had a response
                pracLoop.addData('resp.rt', resp.rt)
                pracLoop.addData('resp.duration', resp.duration)
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[fbk_text],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fdbk_code
            if resp.corr == True:
                msg = 'Correct!'
                score +=1
            else:
                msg = 'Try Again!'
            fbk_text.setText(msg)
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback" ---
            # if trial has changed, end Routine now
            if isinstance(pracLoop, data.TrialHandler2) and thisPracLoop.thisN != pracLoop.thisTrial.thisN:
                continueRoutine = False
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fbk_text* updates
                
                # if fbk_text is starting this frame...
                if fbk_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fbk_text.frameNStart = frameN  # exact frame index
                    fbk_text.tStart = t  # local t and not account for scr refresh
                    fbk_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fbk_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fbk_text.started')
                    # update status
                    fbk_text.status = STARTED
                    fbk_text.setAutoDraw(True)
                
                # if fbk_text is active this frame...
                if fbk_text.status == STARTED:
                    # update params
                    pass
                
                # if fbk_text is stopping this frame...
                if fbk_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fbk_text.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fbk_text.tStop = t  # not accounting for scr refresh
                        fbk_text.tStopRefresh = tThisFlipGlobal  # on global time
                        fbk_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fbk_text.stopped')
                        # update status
                        fbk_text.status = FINISHED
                        fbk_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # Run 'End Routine' code from fdbk_code
            print("Correct trials:" , score, "/15")
            if score >= 10:
                msg2 = "Good practice!"
            elif (prac_count == 1) and (score <10):
                msg2 = "Thanks for playing!"
            else:
                msg2 = "Let's try that again!"
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'pracLoop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "PracInstruc3" ---
        # create an object to store info about Routine PracInstruc3
        PracInstruc3 = data.Routine(
            name='PracInstruc3',
            components=[pracInst3, practResp3],
        )
        PracInstruc3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for practResp3
        practResp3.keys = []
        practResp3.rt = []
        _practResp3_allKeys = []
        # Run 'Begin Routine' code from pracInst3_text
        pracInst3.setText(msg2)
        # store start times for PracInstruc3
        PracInstruc3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracInstruc3.tStart = globalClock.getTime(format='float')
        PracInstruc3.status = STARTED
        thisExp.addData('PracInstruc3.started', PracInstruc3.tStart)
        PracInstruc3.maxDuration = None
        # keep track of which components have finished
        PracInstruc3Components = PracInstruc3.components
        for thisComponent in PracInstruc3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PracInstruc3" ---
        # if trial has changed, end Routine now
        if isinstance(rep_pracLoop, data.TrialHandler2) and thisRep_pracLoop.thisN != rep_pracLoop.thisTrial.thisN:
            continueRoutine = False
        PracInstruc3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pracInst3* updates
            
            # if pracInst3 is starting this frame...
            if pracInst3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pracInst3.frameNStart = frameN  # exact frame index
                pracInst3.tStart = t  # local t and not account for scr refresh
                pracInst3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pracInst3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracInst3.started')
                # update status
                pracInst3.status = STARTED
                pracInst3.setAutoDraw(True)
            
            # if pracInst3 is active this frame...
            if pracInst3.status == STARTED:
                # update params
                pass
            
            # *practResp3* updates
            waitOnFlip = False
            
            # if practResp3 is starting this frame...
            if practResp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practResp3.frameNStart = frameN  # exact frame index
                practResp3.tStart = t  # local t and not account for scr refresh
                practResp3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practResp3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practResp3.started')
                # update status
                practResp3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practResp3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practResp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practResp3.status == STARTED and not waitOnFlip:
                theseKeys = practResp3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _practResp3_allKeys.extend(theseKeys)
                if len(_practResp3_allKeys):
                    practResp3.keys = _practResp3_allKeys[-1].name  # just the last key pressed
                    practResp3.rt = _practResp3_allKeys[-1].rt
                    practResp3.duration = _practResp3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracInstruc3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracInstruc3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracInstruc3" ---
        for thisComponent in PracInstruc3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracInstruc3
        PracInstruc3.tStop = globalClock.getTime(format='float')
        PracInstruc3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracInstruc3.stopped', PracInstruc3.tStop)
        # Run 'End Routine' code from rep_pracLoop_code
        if score >= 10:
            rep_pracLoop.finished = True
        else:
            score = 0
            rep_pracLoop.finished = False
            prac_count += 1
            print("Practice count: ", prac_count)
            if prac_count ==2:
                core.quit()
        # the Routine "PracInstruc3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'rep_pracLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "MainInstruc" ---
    # create an object to store info about Routine MainInstruc
    MainInstruc = data.Routine(
        name='MainInstruc',
        components=[mainInst, instResp],
    )
    MainInstruc.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for instResp
    instResp.keys = []
    instResp.rt = []
    _instResp_allKeys = []
    # store start times for MainInstruc
    MainInstruc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    MainInstruc.tStart = globalClock.getTime(format='float')
    MainInstruc.status = STARTED
    thisExp.addData('MainInstruc.started', MainInstruc.tStart)
    MainInstruc.maxDuration = None
    # keep track of which components have finished
    MainInstrucComponents = MainInstruc.components
    for thisComponent in MainInstruc.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "MainInstruc" ---
    MainInstruc.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mainInst* updates
        
        # if mainInst is starting this frame...
        if mainInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mainInst.frameNStart = frameN  # exact frame index
            mainInst.tStart = t  # local t and not account for scr refresh
            mainInst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mainInst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mainInst.started')
            # update status
            mainInst.status = STARTED
            mainInst.setAutoDraw(True)
        
        # if mainInst is active this frame...
        if mainInst.status == STARTED:
            # update params
            pass
        
        # *instResp* updates
        waitOnFlip = False
        
        # if instResp is starting this frame...
        if instResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instResp.frameNStart = frameN  # exact frame index
            instResp.tStart = t  # local t and not account for scr refresh
            instResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instResp.started')
            # update status
            instResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instResp.status == STARTED and not waitOnFlip:
            theseKeys = instResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instResp_allKeys.extend(theseKeys)
            if len(_instResp_allKeys):
                instResp.keys = _instResp_allKeys[-1].name  # just the last key pressed
                instResp.rt = _instResp_allKeys[-1].rt
                instResp.duration = _instResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            MainInstruc.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MainInstruc.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MainInstruc" ---
    for thisComponent in MainInstruc.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for MainInstruc
    MainInstruc.tStop = globalClock.getTime(format='float')
    MainInstruc.tStopRefresh = tThisFlipGlobal
    thisExp.addData('MainInstruc.stopped', MainInstruc.tStop)
    # check responses
    if instResp.keys in ['', [], None]:  # No response was made
        instResp.keys = None
    thisExp.addData('instResp.keys',instResp.keys)
    if instResp.keys != None:  # we had a response
        thisExp.addData('instResp.rt', instResp.rt)
        thisExp.addData('instResp.duration', instResp.duration)
    thisExp.nextEntry()
    # the Routine "MainInstruc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blockLoop = data.TrialHandler2(
        name='blockLoop',
        nReps=3, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(blockLoop)  # add the loop to the experiment
    thisBlockLoop = blockLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
    if thisBlockLoop != None:
        for paramName in thisBlockLoop:
            globals()[paramName] = thisBlockLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBlockLoop in blockLoop:
        currentLoop = blockLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
        if thisBlockLoop != None:
            for paramName in thisBlockLoop:
                globals()[paramName] = thisBlockLoop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        mainLoop = data.TrialHandler2(
            name='mainLoop',
            nReps=1, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('conds/ant_conds.csv'), 
            seed=None, 
        )
        
        thisExp.addLoop(mainLoop)  # add the loop to the experiment
        thisMainLoop = mainLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
        if thisMainLoop != None:
            for paramName in thisMainLoop:
                globals()[paramName] = thisMainLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisMainLoop in mainLoop:
            currentLoop = mainLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
            if thisMainLoop != None:
                for paramName in thisMainLoop:
                    globals()[paramName] = thisMainLoop[paramName]
            
            # --- Prepare to start Routine "fixation" ---
            # create an object to store info about Routine fixation
            fixation = data.Routine(
                name='fixation',
                components=[image],
            )
            fixation.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from jitterFixCross
            durations = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]  # Create durations 
            shuffle(durations)  # Randomize durations 
            fixDuration  = durations[0] # Take one of the randomized durations
            # store start times for fixation
            fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation.tStart = globalClock.getTime(format='float')
            fixation.status = STARTED
            thisExp.addData('fixation.started', fixation.tStart)
            fixation.maxDuration = None
            # keep track of which components have finished
            fixationComponents = fixation.components
            for thisComponent in fixation.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            # if trial has changed, end Routine now
            if isinstance(mainLoop, data.TrialHandler2) and thisMainLoop.thisN != mainLoop.thisTrial.thisN:
                continueRoutine = False
            fixation.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                
                # if image is starting this frame...
                if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.started')
                    # update status
                    image.status = STARTED
                    image.setAutoDraw(True)
                
                # if image is active this frame...
                if image.status == STARTED:
                    # update params
                    pass
                
                # if image is stopping this frame...
                if image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image.tStartRefresh + fixDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.tStopRefresh = tThisFlipGlobal  # on global time
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        # update status
                        image.status = FINISHED
                        image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    fixation.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation
            fixation.tStop = globalClock.getTime(format='float')
            fixation.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation.stopped', fixation.tStop)
            # Run 'End Routine' code from jitterFixCross
            thisExp.addData("fixDuration", fixDuration)
            # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[top_cue, cent_cue, bot_cue, target_img, resp, fixationshort],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            top_cue.setImage(upper_cue)
            cent_cue.setImage(center_cue)
            bot_cue.setImage(lower_cue)
            target_img.setImage(targetFile)
            # create starting attributes for resp
            resp.keys = []
            resp.rt = []
            _resp_allKeys = []
            # Run 'Begin Routine' code from setTargetLoc
            if targetLoc == 'upper':
                target_img.pos = (0, targ_offset)
            elif targetLoc == 'lower':
                target_img.pos = (0, 0-targ_offset)
                
            top_cue.pos = (0, targ_offset)
            bot_cue.pos = (0, 0-targ_offset)
            
                
            # Run 'Begin Routine' code from setFixStartTime
            if cue == 'center':
                fixStartTime = 0.15
            else: fixStartTime = 0.0
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            # if trial has changed, end Routine now
            if isinstance(mainLoop, data.TrialHandler2) and thisMainLoop.thisN != mainLoop.thisTrial.thisN:
                continueRoutine = False
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *top_cue* updates
                
                # if top_cue is starting this frame...
                if top_cue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    top_cue.frameNStart = frameN  # exact frame index
                    top_cue.tStart = t  # local t and not account for scr refresh
                    top_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(top_cue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'top_cue.started')
                    # update status
                    top_cue.status = STARTED
                    top_cue.setAutoDraw(True)
                
                # if top_cue is active this frame...
                if top_cue.status == STARTED:
                    # update params
                    pass
                
                # if top_cue is stopping this frame...
                if top_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > top_cue.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        top_cue.tStop = t  # not accounting for scr refresh
                        top_cue.tStopRefresh = tThisFlipGlobal  # on global time
                        top_cue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'top_cue.stopped')
                        # update status
                        top_cue.status = FINISHED
                        top_cue.setAutoDraw(False)
                
                # *cent_cue* updates
                
                # if cent_cue is starting this frame...
                if cent_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cent_cue.frameNStart = frameN  # exact frame index
                    cent_cue.tStart = t  # local t and not account for scr refresh
                    cent_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cent_cue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cent_cue.started')
                    # update status
                    cent_cue.status = STARTED
                    cent_cue.setAutoDraw(True)
                
                # if cent_cue is active this frame...
                if cent_cue.status == STARTED:
                    # update params
                    pass
                
                # if cent_cue is stopping this frame...
                if cent_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cent_cue.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        cent_cue.tStop = t  # not accounting for scr refresh
                        cent_cue.tStopRefresh = tThisFlipGlobal  # on global time
                        cent_cue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'cent_cue.stopped')
                        # update status
                        cent_cue.status = FINISHED
                        cent_cue.setAutoDraw(False)
                
                # *bot_cue* updates
                
                # if bot_cue is starting this frame...
                if bot_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    bot_cue.frameNStart = frameN  # exact frame index
                    bot_cue.tStart = t  # local t and not account for scr refresh
                    bot_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(bot_cue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bot_cue.started')
                    # update status
                    bot_cue.status = STARTED
                    bot_cue.setAutoDraw(True)
                
                # if bot_cue is active this frame...
                if bot_cue.status == STARTED:
                    # update params
                    pass
                
                # if bot_cue is stopping this frame...
                if bot_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > bot_cue.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        bot_cue.tStop = t  # not accounting for scr refresh
                        bot_cue.tStopRefresh = tThisFlipGlobal  # on global time
                        bot_cue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'bot_cue.stopped')
                        # update status
                        bot_cue.status = FINISHED
                        bot_cue.setAutoDraw(False)
                
                # *target_img* updates
                
                # if target_img is starting this frame...
                if target_img.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    target_img.frameNStart = frameN  # exact frame index
                    target_img.tStart = t  # local t and not account for scr refresh
                    target_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'target_img.started')
                    # update status
                    target_img.status = STARTED
                    target_img.setAutoDraw(True)
                
                # if target_img is active this frame...
                if target_img.status == STARTED:
                    # update params
                    pass
                
                # if target_img is stopping this frame...
                if target_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_img.tStartRefresh + 1.7-frameTolerance:
                        # keep track of stop time/frame for later
                        target_img.tStop = t  # not accounting for scr refresh
                        target_img.tStopRefresh = tThisFlipGlobal  # on global time
                        target_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'target_img.stopped')
                        # update status
                        target_img.status = FINISHED
                        target_img.setAutoDraw(False)
                
                # *resp* updates
                waitOnFlip = False
                
                # if resp is starting this frame...
                if resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    resp.frameNStart = frameN  # exact frame index
                    resp.tStart = t  # local t and not account for scr refresh
                    resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resp.started')
                    # update status
                    resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if resp is stopping this frame...
                if resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > resp.tStartRefresh + 1.7-frameTolerance:
                        # keep track of stop time/frame for later
                        resp.tStop = t  # not accounting for scr refresh
                        resp.tStopRefresh = tThisFlipGlobal  # on global time
                        resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp.stopped')
                        # update status
                        resp.status = FINISHED
                        resp.status = FINISHED
                if resp.status == STARTED and not waitOnFlip:
                    theseKeys = resp.getKeys(keyList=['1','2'], ignoreKeys=["escape"], waitRelease=False)
                    _resp_allKeys.extend(theseKeys)
                    if len(_resp_allKeys):
                        resp.keys = _resp_allKeys[0].name  # just the first key pressed
                        resp.rt = _resp_allKeys[0].rt
                        resp.duration = _resp_allKeys[0].duration
                        # was this correct?
                        if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                            resp.corr = 1
                        else:
                            resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *fixationshort* updates
                
                # if fixationshort is starting this frame...
                if fixationshort.status == NOT_STARTED and tThisFlip >= fixStartTime-frameTolerance:
                    # keep track of start time/frame for later
                    fixationshort.frameNStart = frameN  # exact frame index
                    fixationshort.tStart = t  # local t and not account for scr refresh
                    fixationshort.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixationshort, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationshort.started')
                    # update status
                    fixationshort.status = STARTED
                    fixationshort.setAutoDraw(True)
                
                # if fixationshort is active this frame...
                if fixationshort.status == STARTED:
                    # update params
                    pass
                
                # if fixationshort is stopping this frame...
                if fixationshort.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixationshort.tStartRefresh + 2.2-frameTolerance:
                        # keep track of stop time/frame for later
                        fixationshort.tStop = t  # not accounting for scr refresh
                        fixationshort.tStopRefresh = tThisFlipGlobal  # on global time
                        fixationshort.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixationshort.stopped')
                        # update status
                        fixationshort.status = FINISHED
                        fixationshort.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # check responses
            if resp.keys in ['', [], None]:  # No response was made
                resp.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   resp.corr = 1;  # correct non-response
                else:
                   resp.corr = 0;  # failed to respond (incorrectly)
            # store data for mainLoop (TrialHandler)
            mainLoop.addData('resp.keys',resp.keys)
            mainLoop.addData('resp.corr', resp.corr)
            if resp.keys != None:  # we had a response
                mainLoop.addData('resp.rt', resp.rt)
                mainLoop.addData('resp.duration', resp.duration)
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'mainLoop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "Rest" ---
        # create an object to store info about Routine Rest
        Rest = data.Routine(
            name='Rest',
            components=[rest, restResp],
        )
        Rest.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for restResp
        restResp.keys = []
        restResp.rt = []
        _restResp_allKeys = []
        # store start times for Rest
        Rest.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Rest.tStart = globalClock.getTime(format='float')
        Rest.status = STARTED
        thisExp.addData('Rest.started', Rest.tStart)
        Rest.maxDuration = None
        # keep track of which components have finished
        RestComponents = Rest.components
        for thisComponent in Rest.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Rest" ---
        # if trial has changed, end Routine now
        if isinstance(blockLoop, data.TrialHandler2) and thisBlockLoop.thisN != blockLoop.thisTrial.thisN:
            continueRoutine = False
        Rest.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rest* updates
            
            # if rest is starting this frame...
            if rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest.frameNStart = frameN  # exact frame index
                rest.tStart = t  # local t and not account for scr refresh
                rest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest.started')
                # update status
                rest.status = STARTED
                rest.setAutoDraw(True)
            
            # if rest is active this frame...
            if rest.status == STARTED:
                # update params
                pass
            
            # *restResp* updates
            waitOnFlip = False
            
            # if restResp is starting this frame...
            if restResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                restResp.frameNStart = frameN  # exact frame index
                restResp.tStart = t  # local t and not account for scr refresh
                restResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(restResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'restResp.started')
                # update status
                restResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(restResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(restResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if restResp.status == STARTED and not waitOnFlip:
                theseKeys = restResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _restResp_allKeys.extend(theseKeys)
                if len(_restResp_allKeys):
                    restResp.keys = _restResp_allKeys[-1].name  # just the last key pressed
                    restResp.rt = _restResp_allKeys[-1].rt
                    restResp.duration = _restResp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Rest.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Rest.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Rest" ---
        for thisComponent in Rest.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Rest
        Rest.tStop = globalClock.getTime(format='float')
        Rest.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Rest.stopped', Rest.tStop)
        # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 3 repeats of 'blockLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "End" ---
    # create an object to store info about Routine End
    End = data.Routine(
        name='End',
        components=[endText, endKey, flippy_fish],
    )
    End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for endKey
    endKey.keys = []
    endKey.rt = []
    _endKey_allKeys = []
    flippy_fish.setOri(0.0)
    # store start times for End
    End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End.tStart = globalClock.getTime(format='float')
    End.status = STARTED
    thisExp.addData('End.started', End.tStart)
    End.maxDuration = None
    # keep track of which components have finished
    EndComponents = End.components
    for thisComponent in End.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End" ---
    End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endText* updates
        
        # if endText is starting this frame...
        if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endText.frameNStart = frameN  # exact frame index
            endText.tStart = t  # local t and not account for scr refresh
            endText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endText.started')
            # update status
            endText.status = STARTED
            endText.setAutoDraw(True)
        
        # if endText is active this frame...
        if endText.status == STARTED:
            # update params
            pass
        
        # *endKey* updates
        waitOnFlip = False
        
        # if endKey is starting this frame...
        if endKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endKey.frameNStart = frameN  # exact frame index
            endKey.tStart = t  # local t and not account for scr refresh
            endKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endKey.started')
            # update status
            endKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endKey.status == STARTED and not waitOnFlip:
            theseKeys = endKey.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _endKey_allKeys.extend(theseKeys)
            if len(_endKey_allKeys):
                endKey.keys = _endKey_allKeys[-1].name  # just the last key pressed
                endKey.rt = _endKey_allKeys[-1].rt
                endKey.duration = _endKey_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *flippy_fish* updates
        
        # if flippy_fish is starting this frame...
        if flippy_fish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            flippy_fish.frameNStart = frameN  # exact frame index
            flippy_fish.tStart = t  # local t and not account for scr refresh
            flippy_fish.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flippy_fish, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'flippy_fish.started')
            # update status
            flippy_fish.status = STARTED
            flippy_fish.setAutoDraw(True)
        
        # if flippy_fish is active this frame...
        if flippy_fish.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from fish_flipping
        flippy_fish.ori += 1
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End
    End.tStop = globalClock.getTime(format='float')
    End.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End.stopped', End.tStop)
    thisExp.nextEntry()
    # the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
