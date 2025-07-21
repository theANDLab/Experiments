/************ 
 * Ant Test *
 ************/

import { PsychoJS } from './lib/core-2021.1.2.js';
import * as core from './lib/core-2021.1.2.js';
import { TrialHandler } from './lib/data-2021.1.2.js';
import { Scheduler } from './lib/util-2021.1.2.js';
import * as visual from './lib/visual-2021.1.2.js';
import * as sound from './lib/sound-2021.1.2.js';
import * as util from './lib/util-2021.1.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('aqua'),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'ANT';  // from the Builder filename that created this script
let expInfo = {'family': '', 'participant': '', 'session': ''};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(PracInstrucRoutineBegin());
flowScheduler.add(PracInstrucRoutineEachFrame());
flowScheduler.add(PracInstrucRoutineEnd());
flowScheduler.add(PracInstruct2RoutineBegin());
flowScheduler.add(PracInstruct2RoutineEachFrame());
flowScheduler.add(PracInstruct2RoutineEnd());
const pracLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pracLoopLoopBegin, pracLoopLoopScheduler);
flowScheduler.add(pracLoopLoopScheduler);
flowScheduler.add(pracLoopLoopEnd);
flowScheduler.add(MainInstrucRoutineBegin());
flowScheduler.add(MainInstrucRoutineEachFrame());
flowScheduler.add(MainInstrucRoutineEnd());
const blockLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blockLoopLoopBegin, blockLoopLoopScheduler);
flowScheduler.add(blockLoopLoopScheduler);
flowScheduler.add(blockLoopLoopEnd);
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://surreyfahs.eu.qualtrics.com/jfe/form/SV_5p9sgJm3jv3P446', 'https://surreyfahs.eu.qualtrics.com/jfe/form/SV_5p9sgJm3jv3P446');

  return Scheduler.Event.NEXT;
}


var PracInstrucClock;
var pracText1;
var pracResp1;
var logo;
var intro_bubbles;
var PracInstruct2Clock;
var practInst2;
var practResp2;
var intro_img_2;
var intro_img_22;
var intro_bubs_2;
var fixationClock;
var fixDuration;
var image;
var trialClock;
var cues;
var target_img;
var resp;
var fixationshort;
var targ_offset;
var fixStartTime;
var feedbackClock;
var fbk_text;
var MainInstrucClock;
var mainInst;
var instResp;
var RestClock;
var rest;
var restResp;
var EndClock;
var endText;
var endKey;
var flippy_fish;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "PracInstruc"
  PracInstrucClock = new util.Clock();
  pracText1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracText1',
    text: 'The Fish Tank!\n\n\n\n\n\n\n\nSPACE  to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  pracResp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  logo = new visual.ImageStim({
    win : psychoJS.window,
    name : 'logo', units : undefined, 
    image : 'stim/introFish.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 0.8],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  intro_bubbles = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_bubbles', units : undefined, 
    image : 'stim/big_bubbles.png', mask : undefined,
    ori : 20.0, pos : [0.7, 0.1], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "PracInstruct2"
  PracInstruct2Clock = new util.Clock();
  practInst2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'practInst2',
    text: 'In this game you will see rows of fish like this:\n\n\n\nPress the arrow key ← or → that matches the direction of the MIDDLE fish!\n\nLook out for bubbles!\n\nThey tell you where the fish might pop up next!\n\nTry to answer as fast and as accurately as you can! \nPress SPACE to practice!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  practResp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  intro_img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_img_2', units : undefined, 
    image : 'stim/lincon.png', mask : undefined,
    ori : 0.0, pos : [(- 0.3), 0.2], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  intro_img_22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_img_22', units : undefined, 
    image : 'stim/rcon.png', mask : undefined,
    ori : 0.0, pos : [0.3, 0.2], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  intro_bubs_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_bubs_2', units : undefined, 
    image : 'stim/bubbles.png', mask : undefined,
    ori : 0.0, pos : [0.25, (- 0.03)], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixDuration = 0.4;
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'pix', 
    image : 'stim/fix.png', mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  cues = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cues', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  target_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_img', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fixationshort = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationshort', units : 'pix', 
    image : 'stim/fix.png', mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  targ_offset = 112;
  
  fixStartTime = 0.0;
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  fbk_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'fbk_text',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  var msg = ""
  // Initialize components for Routine "MainInstruc"
  MainInstrucClock = new util.Clock();
  mainInst = new visual.TextStim({
    win: psychoJS.window,
    name: 'mainInst',
    text: "Good practice!\n\nNow on to the main game. This time we won't tell you how fast your were or the right answer. Try to be as quick and accurate as you can!\n\nThere will be 3 rounds with a rest period between each one, and at the end (you can skip this!). \n\nSPACE  to continue.",
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  instResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixDuration = 0.4;
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'pix', 
    image : 'stim/fix.png', mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  cues = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cues', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  target_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_img', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fixationshort = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationshort', units : 'pix', 
    image : 'stim/fix.png', mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  targ_offset = 112;
  
  fixStartTime = 0.0;
  
  // Initialize components for Routine "Rest"
  RestClock = new util.Clock();
  rest = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest',
    text: 'Block complete!\n\nIf you want, have a short rest.\n\n\n\nThen press SPACE for the next round!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  restResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  endText = new visual.TextStim({
    win: psychoJS.window,
    name: 'endText',
    text: 'Fish Tank Complete!!\n\n\n\n\n\n\nThank you for playing!\nPress SPACE to exit.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  endKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  flippy_fish = new visual.ImageStim({
    win : psychoJS.window,
    name : 'flippy_fish', units : undefined, 
    image : 'stim/introFish.png', mask : undefined,
    ori : 1.0, pos : [0, 0.1], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _pracResp1_allKeys;
var PracInstrucComponents;
function PracInstrucRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracInstruc'-------
    t = 0;
    PracInstrucClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    pracResp1.keys = undefined;
    pracResp1.rt = undefined;
    _pracResp1_allKeys = [];
    // keep track of which components have finished
    PracInstrucComponents = [];
    PracInstrucComponents.push(pracText1);
    PracInstrucComponents.push(pracResp1);
    PracInstrucComponents.push(logo);
    PracInstrucComponents.push(intro_bubbles);
    
    for (const thisComponent of PracInstrucComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PracInstrucRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracInstruc'-------
    // get current time
    t = PracInstrucClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pracText1* updates
    if (t >= 0.0 && pracText1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracText1.tStart = t;  // (not accounting for frame time here)
      pracText1.frameNStart = frameN;  // exact frame index
      
      pracText1.setAutoDraw(true);
    }

    
    // *pracResp1* updates
    if (t >= 0.0 && pracResp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracResp1.tStart = t;  // (not accounting for frame time here)
      pracResp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pracResp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pracResp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pracResp1.clearEvents(); });
    }

    if (pracResp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = pracResp1.getKeys({keyList: ['space'], waitRelease: false});
      _pracResp1_allKeys = _pracResp1_allKeys.concat(theseKeys);
      if (_pracResp1_allKeys.length > 0) {
        pracResp1.keys = _pracResp1_allKeys[_pracResp1_allKeys.length - 1].name;  // just the last key pressed
        pracResp1.rt = _pracResp1_allKeys[_pracResp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *logo* updates
    if (t >= 0.0 && logo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      logo.tStart = t;  // (not accounting for frame time here)
      logo.frameNStart = frameN;  // exact frame index
      
      logo.setAutoDraw(true);
    }

    
    // *intro_bubbles* updates
    if (t >= 0.0 && intro_bubbles.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_bubbles.tStart = t;  // (not accounting for frame time here)
      intro_bubbles.frameNStart = frameN;  // exact frame index
      
      intro_bubbles.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracInstrucComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracInstrucRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracInstruc'-------
    for (const thisComponent of PracInstrucComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "PracInstruc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _practResp2_allKeys;
var PracInstruct2Components;
function PracInstruct2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracInstruct2'-------
    t = 0;
    PracInstruct2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    practResp2.keys = undefined;
    practResp2.rt = undefined;
    _practResp2_allKeys = [];
    // keep track of which components have finished
    PracInstruct2Components = [];
    PracInstruct2Components.push(practInst2);
    PracInstruct2Components.push(practResp2);
    PracInstruct2Components.push(intro_img_2);
    PracInstruct2Components.push(intro_img_22);
    PracInstruct2Components.push(intro_bubs_2);
    
    for (const thisComponent of PracInstruct2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PracInstruct2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracInstruct2'-------
    // get current time
    t = PracInstruct2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practInst2* updates
    if (t >= 0.0 && practInst2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practInst2.tStart = t;  // (not accounting for frame time here)
      practInst2.frameNStart = frameN;  // exact frame index
      
      practInst2.setAutoDraw(true);
    }

    
    // *practResp2* updates
    if (t >= 0.0 && practResp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practResp2.tStart = t;  // (not accounting for frame time here)
      practResp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practResp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practResp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practResp2.clearEvents(); });
    }

    if (practResp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = practResp2.getKeys({keyList: ['space'], waitRelease: false});
      _practResp2_allKeys = _practResp2_allKeys.concat(theseKeys);
      if (_practResp2_allKeys.length > 0) {
        practResp2.keys = _practResp2_allKeys[_practResp2_allKeys.length - 1].name;  // just the last key pressed
        practResp2.rt = _practResp2_allKeys[_practResp2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *intro_img_2* updates
    if (t >= 0.0 && intro_img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_img_2.tStart = t;  // (not accounting for frame time here)
      intro_img_2.frameNStart = frameN;  // exact frame index
      
      intro_img_2.setAutoDraw(true);
    }

    
    // *intro_img_22* updates
    if (t >= 0.0 && intro_img_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_img_22.tStart = t;  // (not accounting for frame time here)
      intro_img_22.frameNStart = frameN;  // exact frame index
      
      intro_img_22.setAutoDraw(true);
    }

    
    // *intro_bubs_2* updates
    if (t >= 0.0 && intro_bubs_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_bubs_2.tStart = t;  // (not accounting for frame time here)
      intro_bubs_2.frameNStart = frameN;  // exact frame index
      
      intro_bubs_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracInstruct2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracInstruct2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracInstruct2'-------
    for (const thisComponent of PracInstruct2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "PracInstruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var pracLoop;
var currentLoop;
function pracLoopLoopBegin(pracLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  pracLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'ant_conds.csv', '0:15'),
    seed: undefined, name: 'pracLoop'
  });
  psychoJS.experiment.addLoop(pracLoop); // add the loop to the experiment
  currentLoop = pracLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPracLoop of pracLoop) {
    const snapshot = pracLoop.getSnapshot();
    pracLoopLoopScheduler.add(importConditions(snapshot));
    pracLoopLoopScheduler.add(fixationRoutineBegin(snapshot));
    pracLoopLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    pracLoopLoopScheduler.add(fixationRoutineEnd(snapshot));
    pracLoopLoopScheduler.add(trialRoutineBegin(snapshot));
    pracLoopLoopScheduler.add(trialRoutineEachFrame(snapshot));
    pracLoopLoopScheduler.add(trialRoutineEnd(snapshot));
    pracLoopLoopScheduler.add(feedbackRoutineBegin(snapshot));
    pracLoopLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    pracLoopLoopScheduler.add(feedbackRoutineEnd(snapshot));
    pracLoopLoopScheduler.add(endLoopIteration(pracLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function pracLoopLoopEnd() {
  psychoJS.experiment.removeLoop(pracLoop);

  return Scheduler.Event.NEXT;
}


var blockLoop;
function blockLoopLoopBegin(blockLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  blockLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'blockLoop'
  });
  psychoJS.experiment.addLoop(blockLoop); // add the loop to the experiment
  currentLoop = blockLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlockLoop of blockLoop) {
    const snapshot = blockLoop.getSnapshot();
    blockLoopLoopScheduler.add(importConditions(snapshot));
    const mainLoopLoopScheduler = new Scheduler(psychoJS);
    blockLoopLoopScheduler.add(mainLoopLoopBegin, mainLoopLoopScheduler);
    blockLoopLoopScheduler.add(mainLoopLoopScheduler);
    blockLoopLoopScheduler.add(mainLoopLoopEnd);
    blockLoopLoopScheduler.add(RestRoutineBegin(snapshot));
    blockLoopLoopScheduler.add(RestRoutineEachFrame(snapshot));
    blockLoopLoopScheduler.add(RestRoutineEnd(snapshot));
    blockLoopLoopScheduler.add(endLoopIteration(blockLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var mainLoop;
function mainLoopLoopBegin(mainLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  mainLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'ant_conds.csv',
    seed: undefined, name: 'mainLoop'
  });
  psychoJS.experiment.addLoop(mainLoop); // add the loop to the experiment
  currentLoop = mainLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMainLoop of mainLoop) {
    const snapshot = mainLoop.getSnapshot();
    mainLoopLoopScheduler.add(importConditions(snapshot));
    mainLoopLoopScheduler.add(fixationRoutineBegin(snapshot));
    mainLoopLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    mainLoopLoopScheduler.add(fixationRoutineEnd(snapshot));
    mainLoopLoopScheduler.add(trialRoutineBegin(snapshot));
    mainLoopLoopScheduler.add(trialRoutineEachFrame(snapshot));
    mainLoopLoopScheduler.add(trialRoutineEnd(snapshot));
    mainLoopLoopScheduler.add(endLoopIteration(mainLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function mainLoopLoopEnd() {
  psychoJS.experiment.removeLoop(mainLoop);

  return Scheduler.Event.NEXT;
}


function blockLoopLoopEnd() {
  psychoJS.experiment.removeLoop(blockLoop);

  return Scheduler.Event.NEXT;
}


var durations;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fixation'-------
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    durations = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0];
    util.shuffle(durations);
    fixDuration = durations[0];
    
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(image);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fixation'-------
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fixation'-------
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData("fixDuration", fixDuration);
    
    // the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    cues.setImage(cueFile);
    target_img.setImage(targetFile);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    if ((targetLoc === "upper")) {
        target_img.pos = [0, targ_offset];
    } else {
        if ((targetLoc === "lower")) {
            target_img.pos = [0, (0 - targ_offset)];
        }
    }
    
    if ((cue === "center")) {
        fixStartTime = 0.15;
    } else {
        fixStartTime = 0.0;
    }
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(cues);
    trialComponents.push(target_img);
    trialComponents.push(resp);
    trialComponents.push(fixationshort);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cues* updates
    if (t >= 0 && cues.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cues.tStart = t;  // (not accounting for frame time here)
      cues.frameNStart = frameN;  // exact frame index
      
      cues.setAutoDraw(true);
    }

    frameRemains = 0 + 0.15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cues.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cues.setAutoDraw(false);
    }
    
    // *target_img* updates
    if (t >= 0.5 && target_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_img.tStart = t;  // (not accounting for frame time here)
      target_img.frameNStart = frameN;  // exact frame index
      
      target_img.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target_img.setAutoDraw(false);
    }
    
    // *resp* updates
    if (t >= 0.5 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }

    frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp.status = PsychoJS.Status.FINISHED;
  }

    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[0].name;  // just the first key pressed
        resp.rt = _resp_allKeys[0].rt;
        // was this correct?
        if (resp.keys == corrAns) {
            resp.corr = 1;
        } else {
            resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixationshort* updates
    if (t >= fixStartTime && fixationshort.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationshort.tStart = t;  // (not accounting for frame time here)
      fixationshort.frameNStart = frameN;  // exact frame index
      
      fixationshort.setAutoDraw(true);
    }

    frameRemains = fixStartTime + 2.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixationshort.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationshort.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         resp.corr = 1;  // correct non-response
      } else {
         resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('resp.keys', resp.keys);
    psychoJS.experiment.addData('resp.corr', resp.corr);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        routineTimer.reset();
        }
    
    resp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var msg;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if ((resp.corr === 1)) {
        msg = "Correct!";
    } else {
        msg = "Wrong";
    }
    fbk_text.setText(msg);
    
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(fbk_text);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fbk_text* updates
    if (t >= 0.0 && fbk_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fbk_text.tStart = t;  // (not accounting for frame time here)
      fbk_text.frameNStart = frameN;  // exact frame index
      
      fbk_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fbk_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fbk_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _instResp_allKeys;
var MainInstrucComponents;
function MainInstrucRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MainInstruc'-------
    t = 0;
    MainInstrucClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instResp.keys = undefined;
    instResp.rt = undefined;
    _instResp_allKeys = [];
    // keep track of which components have finished
    MainInstrucComponents = [];
    MainInstrucComponents.push(mainInst);
    MainInstrucComponents.push(instResp);
    
    for (const thisComponent of MainInstrucComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function MainInstrucRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MainInstruc'-------
    // get current time
    t = MainInstrucClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mainInst* updates
    if (t >= 0.0 && mainInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mainInst.tStart = t;  // (not accounting for frame time here)
      mainInst.frameNStart = frameN;  // exact frame index
      
      mainInst.setAutoDraw(true);
    }

    
    // *instResp* updates
    if (t >= 0.0 && instResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instResp.tStart = t;  // (not accounting for frame time here)
      instResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instResp.clearEvents(); });
    }

    if (instResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instResp.getKeys({keyList: ['space'], waitRelease: false});
      _instResp_allKeys = _instResp_allKeys.concat(theseKeys);
      if (_instResp_allKeys.length > 0) {
        instResp.keys = _instResp_allKeys[_instResp_allKeys.length - 1].name;  // just the last key pressed
        instResp.rt = _instResp_allKeys[_instResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of MainInstrucComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MainInstrucRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MainInstruc'-------
    for (const thisComponent of MainInstrucComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instResp.keys', instResp.keys);
    if (typeof instResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instResp.rt', instResp.rt);
        routineTimer.reset();
        }
    
    instResp.stop();
    // the Routine "MainInstruc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _restResp_allKeys;
var RestComponents;
function RestRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Rest'-------
    t = 0;
    RestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    restResp.keys = undefined;
    restResp.rt = undefined;
    _restResp_allKeys = [];
    // keep track of which components have finished
    RestComponents = [];
    RestComponents.push(rest);
    RestComponents.push(restResp);
    
    for (const thisComponent of RestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RestRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Rest'-------
    // get current time
    t = RestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rest* updates
    if (t >= 0.0 && rest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest.tStart = t;  // (not accounting for frame time here)
      rest.frameNStart = frameN;  // exact frame index
      
      rest.setAutoDraw(true);
    }

    
    // *restResp* updates
    if (t >= 0.0 && restResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      restResp.tStart = t;  // (not accounting for frame time here)
      restResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { restResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { restResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { restResp.clearEvents(); });
    }

    if (restResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = restResp.getKeys({keyList: ['space'], waitRelease: false});
      _restResp_allKeys = _restResp_allKeys.concat(theseKeys);
      if (_restResp_allKeys.length > 0) {
        restResp.keys = _restResp_allKeys[_restResp_allKeys.length - 1].name;  // just the last key pressed
        restResp.rt = _restResp_allKeys[_restResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RestRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Rest'-------
    for (const thisComponent of RestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _endKey_allKeys;
var EndComponents;
function EndRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    endKey.keys = undefined;
    endKey.rt = undefined;
    _endKey_allKeys = [];
    flippy_fish.setOri(0.0);
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(endText);
    EndComponents.push(endKey);
    EndComponents.push(flippy_fish);
    
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'End'-------
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endText* updates
    if (t >= 0.0 && endText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endText.tStart = t;  // (not accounting for frame time here)
      endText.frameNStart = frameN;  // exact frame index
      
      endText.setAutoDraw(true);
    }

    
    // *endKey* updates
    if (t >= 0.0 && endKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endKey.tStart = t;  // (not accounting for frame time here)
      endKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endKey.clearEvents(); });
    }

    if (endKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = endKey.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _endKey_allKeys = _endKey_allKeys.concat(theseKeys);
      if (_endKey_allKeys.length > 0) {
        endKey.keys = _endKey_allKeys[_endKey_allKeys.length - 1].name;  // just the last key pressed
        endKey.rt = _endKey_allKeys[_endKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *flippy_fish* updates
    if (t >= 0.0 && flippy_fish.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      flippy_fish.tStart = t;  // (not accounting for frame time here)
      flippy_fish.frameNStart = frameN;  // exact frame index
      
      flippy_fish.setAutoDraw(true);
    }

    flippy_fish.ori += 1;
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'End'-------
    for (const thisComponent of EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
