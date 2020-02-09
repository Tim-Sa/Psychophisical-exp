#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Декабрь 16, 2019, at 18:07
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

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

#!#######################################################--INCLUDE THIS LIBRARY FOR RANDOM CHOOSE FUNCTIONS OF CALC POLYGON SIZES FROM LIST--##############################
import random

#!#######################################################--INCLUDE THIS LIBRARY FOR WRITING RESULTS TO EXCEL FILE--########################################################
from pandas import DataFrame


#!##################################################--SETTINGS OF EXPERIMENT--##############################################################
repeats = 25

frames_low = 18
frames_hight = 8
line_low = 4
line_hight = 9
max_diametr = 254
min_diametr = 113

path = max_diametr - min_diametr

last_frameN_low = frames_low+1
last_frameN_hight = frames_hight+1
#!###########################################################--DEFINITION OF POLYGON CHANGE SIZE FUNCTIONS --##############################################################

def hex_in_hight_speed(frameN):
    
    global in_hight_counter #count of using this func
    in_hight_counter += 1
    
    if in_hight_counter == repeats * last_frameN-1: #if using-num is equal to repeats - don't use this function anymore (delete from list of using funcs)
        functions_of_hex.remove(hex_in_hight_speed) 
   
    result = max_diametr-frameN*path/frames_hight #formula of poligon size for decreasing at high speed
    return result

def hex_out_hight_speed(frameN):

    global out_hight_counter 
    out_hight_counter += 1
    
    if out_hight_counter == repeats * last_frameN-1:
        functions_of_hex.remove(hex_out_hight_speed) 
        
    result = min_diametr+frameN*path/frames_hight #formula of poligon size for increasing at high speed
    return result

def hex_in_low_speed(frameN):

    global in_low_counter 
    in_low_counter += 1

    if in_low_counter == repeats * last_frameN-1:
        functions_of_hex.remove(hex_in_low_speed)

    result = max_diametr-frameN*path/frames_low#formula of poligon size for decreasing at low speed
    return result

def hex_out_low_speed(frameN):

    global out_low_counter 
    out_low_counter += 1

    if out_low_counter == repeats * last_frameN-1:
        functions_of_hex.remove(hex_out_low_speed)

    result = min_diametr+frameN*path/frames_low#formula of poligon size for increasing at low speed
    return result
    
#counters of func-using
in_hight_counter = 0
out_hight_counter = 0 
in_low_counter = 0
out_low_counter = 0


#!#######################################################--LIST OF CHANGE POLYGON SIZE FUNCTIONS--#########################################################
start_functions_of_hex =[hex_in_hight_speed, hex_out_hight_speed, hex_in_low_speed, hex_out_low_speed]

functions_of_hex = start_functions_of_hex[::]#after all trial repeats of function using we will delete this function from list, but with starting new observe - 
                                              #we need all functions in list again. 
                                              #--
                                              #So we have 2 lists - 1)start_list - that not changing 2) his copy for changing
#!#########################################################################################################################################################

#!#####################################################--THERE WE WILL SAVE ANSWERS (LEFT OR RIGHT) FOR LATER WRITHING TO EXCEL FILE--#####################
in_hight_answers = []
out_hight_answers = []
in_low_answers = []
out_low_answers = []
#!#########################################################################################################################################################

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Framing_1'  # from the Builder filename that created this script
expInfo = {'participant': 'S', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Администратор\\Desktop\\эксперимент\\Framing_1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation



# Setup the Window##############################################################--SETTINGS_OF_THE_MONITOR--##############################################################
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor2', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# #######################################################################################################################################################################



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
text = visual.TextStim(win=win, name='text',
    text='Инструкция\nВам будет представлена последовательность однотипных стимулов. \n\nОни представляют собой центральную контурную фигуру, изменяющуюся во времени по величине.\nПеред каждым стимулом будут предъявляться: центральная точка, затем изменяющаяся фигура, которая либо увеличивается от малого до большого размера, либо уменьшается от того же большого до того же маленького размера, и затем исчезает.\n\nПосле каждого предъявления фигуры ответьте на вопрос: \n\nЧто, на Ваш взгляд, видно лучше: большой или маленький размер фигуры?\n\nФигуре маленького размера соответствует нажатие «левой стрелки», а фигуре большого размера – «правой стрелки» на клавиатуре.\n\nДля начала каждого следующего предъявления стимула нажмите клавишу пробел.\n\nПо окончанию предъявления стимулов будет представлена надпись «Конец эксперимента»\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',units='cm', 
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Hex_in"
Hex_inClock = core.Clock()
polygon = visual.Polygon(
    win=win, name='polygon',units='pix', 
    edges=6, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=4, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Конец эксперимента\n\nСпасибо за участие!',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruct"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
InstructComponents = [text, key_resp]
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
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc

#!#####################################################--REPEAT TRIAL  AS MANY TIMES AS THE NUMBER OF FORMULAS IN THE LIST#################################################
trials = data.TrialHandler(nReps=repeats*len(start_functions_of_hex), 
#!#########################################################################################################################################################################
    method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:

#!#######################################################--RANDOM CHOOSING ONE OF THE POLYGON CHANGING SIZE FUNCTIONS FROM LIST--##########################
    last_index = len(functions_of_hex)-1
    function_of_hex = functions_of_hex[random.randint(0, last_index)]#take function from list 
#!#########################################################################################################################################################

    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Cross"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CrossComponents = [cross]
    for thisComponent in CrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cross"-------
    for thisComponent in CrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('cross.started', cross.tStartRefresh)
    trials.addData('cross.stopped', cross.tStopRefresh)
    
    # ------Prepare to start Routine "Hex_in"-------
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    Hex_inComponents = [polygon, key_resp_2]
    for thisComponent in Hex_inComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Hex_inClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Hex_in"-------
    while continueRoutine:
        # get current time
        t = Hex_inClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Hex_inClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:


        #!######################################--CHANGING OF FRAME AND POLIGON PARAMS FOR LOW OR HIGHT SPEED--################################################
            if function_of_hex == hex_in_low_speed or function_of_hex == hex_out_low_speed: #IF SPEED IS LOW - TAKE THIS PARAMS:
                last_frameN = last_frameN_low 
                polygon.lineWidth = line_low
            elif function_of_hex == hex_in_hight_speed or function_of_hex == hex_out_hight_speed:  #IF SPEED IS HIGHT - TAKE THIS PARAMS:
                last_frameN = last_frameN_hight
                polygon.lineWidth = line_hight
        #!######################################################################################################################################################

        #!#######################################################--CHANGHING OF STOP FRAME NUMBER--#############################################################
            if frameN >= (polygon.frameNStart + last_frameN):
        #!######################################################################################################################################################
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        if polygon.status == STARTED:  # only update if drawing
            
        #!########################################################--CHANGING OF POLYGON SIZE BY RANDOM CHOOSED FUNCTION#--######################################
            calculated_size = function_of_hex(frameN)
            polygon.setSize((calculated_size, calculated_size), log=False)
        #!######################################################################################################################################################
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Hex_inComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Hex_in"-------
    for thisComponent in Hex_inComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    
    #!###########################################################--ADD ANSWERS TO ANSWERS LIST--########################################################################
    if function_of_hex == hex_out_hight_speed:
        out_hight_answers.append(key_resp_2.keys)

    elif function_of_hex == hex_in_hight_speed:
        in_hight_answers.append(key_resp_2.keys)

    elif function_of_hex == hex_out_low_speed:
        out_low_answers.append(key_resp_2.keys)

    elif function_of_hex == hex_in_low_speed:
        in_low_answers.append(key_resp_2.keys)
    #!##################################################################################################################################################################
    
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Hex_in" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed all repeats of 'trials'

# ------Prepare to start Routine "End"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text_2]
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
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
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
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)

#!########################################################--WRITING RESULTS TO THE EXCEL FILE--##########################################################################
results = DataFrame({'in_hight': in_hight_answers, 'in_low': in_low_answers, 'out_hight' : out_hight_answers, 'out_low' : out_low_answers})
results.to_excel('results_of_{}.xlsx'.format(expInfo['participant']), sheet_name='sheet1', index = False)
#!#######################################################################################################################################################################

logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
