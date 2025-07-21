from psychopy import visual, core, event, data, gui
import random
import os

######################## EXPERIMENT SETUP #####################################################################################################################################################################################################

exp_name = 'Hearts and Flowers Task'
exp_info = {'Participant ID': '','Session': ''}
dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)
if dlg.OK == False:
    core.quit()

# Path to file where data will be saved
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

filename = os.path.join(data_folder, exp_info['Participant ID']+ '_heartsflowers' + exp_info['Session'])
thisExp = data.ExperimentHandler(name=exp_name, version='',
                                 extraInfo=exp_info, runtimeInfo=None,
                                 originPath='',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

# Window setup for EIZO monitor
win = visual.Window(fullscr=True, color="white",
            size=[1920, 1200], screen=1,
            winType='pyglet', allowStencil=False,
            monitor='Eizo', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='cm', 
            checkTiming=False)

# Stimuli setup
stimulus_rect = visual.Rect(win, width=39, height=10, lineColor='black', lineWidth ='3', fillColor=None)
fixation = visual.TextStim(win, text='+', height=2, color="black")
heart_image = visual.ImageStim(win, image='stim/heart.png', size=(3.8, 3.9))
flower_image = visual.ImageStim(win, image='stim/flower.png', size=(3.8, 3.9))

# Display instructions, wait for a key press before starting practice trials
instructions = visual.TextStim(win, text='', height=2, color="black", wrapWidth = 52)
instructions2 = visual.TextStim(win, text='', height=2, color="black", wrapWidth = 40)
instructions.text = ("Welcome to the Hearts and Flowers Game!")
instructions.draw()
win.flip()
event.waitKeys(keyList=['space'])

########################  PARAMETERS ###############################################################################################################################################################################################################

fixation_duration = 0.5 # Fixation cross displayed for 500 ms
blank_duration = 0.5 # After fixation cross disappears, blank screen for 500 ms
stim_duration = 1.2  # Stimuli displayed for 1200 ms
total_resp_time = 2.5  # Maximum response time, starting from stimulus onset

response_keys = ['1', '2'] 
conditions = ['congruent', 'incongruent', 'mixed']
practice_trials = 8 #Even number ensures stimuli will be presented on left and right side an equal number of times

######################## FUNCTIONS #################################################################################################################################################################################################################

# Turn codition.csv file into a tuple stimulus list with (stim_type, stim_position)
def read_csv(filename):
    stim_dict = data.importConditions(filename)
    stim_list = [(stim['stim_type'],stim['stim_position']) for stim in stim_dict]
    
    return stim_list

# Ensure that there are no more than 4 of the same response in a row
def check_consec(stim_list, response_keys):
    def check_consecutive_responses(trials):
        consecutive_count = 0
        last_response = None
        for stim_type, stim_position in trials:
            # Determine the correct response for the current trial
            if stim_type == 'heart':
                correct_response = '1' if stim_position == 'left' else '2'
            elif stim_type == 'flower':
                correct_response = '2' if stim_position == 'left' else '1'

            # Check if the response is the same as the last response
            if correct_response == last_response:
                consecutive_count += 1
            else:
                consecutive_count = 1  # Reset counter for different response
            last_response = correct_response
            
            # If there are more than 4 consecutive responses, return False
            if consecutive_count > 4:
                return False
        return True

    # Try different permutations until the condition is satisfied
    while not check_consecutive_responses(stim_list):
        random.shuffle(stim_list)  # Shuffle the list if the condition is not met
    
    return stim_list

# Function to run practice and experiment blocks within a condition
def run_condition(condition, practice=True):
    trial_number = 0
    correct_count = 0
    stim_list = []

    # Create stimulus list for the current condition
    if condition == 'congruent':
        stim_list = read_csv(f'conds/{condition}.csv') if not practice else [('heart', 'left'), ('heart', 'right')] * (practice_trials // 2)
        random.shuffle(stim_list)
        stim_list = check_consec(stim_list, response_keys)
    elif condition == 'incongruent':
        stim_list = read_csv(f'conds/{condition}.csv') if not practice else [('flower', 'left'), ('flower', 'right')] * (practice_trials // 2)
        random.shuffle(stim_list)
        stim_list = check_consec(stim_list, response_keys)
    elif condition == 'mixed':
        stim_list = read_csv(f'conds/{condition}.csv')

    # Loop through the stimulus list and run trials
    for stim_type, stim_position in stim_list:
        if not practice: 
            trial_number += 1
        # Check for escape key to exit the experiment
        if event.getKeys(keyList=["escape"]):
            core.quit()
            
        # Draw fixation cross
        stimulus_rect.draw()
        fixation.draw()
        win.flip()
        core.wait(fixation_duration)
        
        # Blank screen before stimulus presentation
        stimulus_rect.draw()
        win.flip()
        core.wait(blank_duration)

        # Stimulus presentation
        if stim_type == 'heart':
            heart_image.pos = (-12.96, 0) if stim_position == 'left' else (12.96, 0)
            heart_image.draw()
        elif stim_type == 'flower':
            flower_image.pos = (-12.96, 0) if stim_position == 'left' else (12.96, 0)
            flower_image.draw()
        stimulus_rect.draw()
        win.flip()

        # Record stimulus onset time using core.Clock
        trial_clock = core.Clock()
        trial_clock.reset()  # Reset clock to when stimulus is first presented; beginning of response window
        stim_onset = trial_clock.getTime()  # Record stimulus onset

        # Display stimulus for stimulus duration, then show blank screen
        core.wait(stim_duration)
        stimulus_rect.draw()
        win.flip()

        # Blank screen displays until the end of the response window
        response = None
        while trial_clock.getTime() < total_resp_time:
            keys = event.getKeys(keyList=response_keys + ["escape"], timeStamped=trial_clock)
            if keys:
                key, rt = keys[0]
                rt = rt - stim_onset  # Calculate RT as the time elapsed from stimulus onset
                # Handle anticipatory response (RT < 200ms)
                if rt < 0.2: 
                    rt = None
                    correct = None
                    break 
                if key == 'escape':
                    core.quit()
                    break
                break
        else:
            key = None
            rt = None
            correct = None
        
        # Calculate response accuracy
        correct = False
        if key in response_keys:
            if stim_type == 'heart':
                if (stim_position == 'left' and key == '1') or (stim_position == 'right' and key == '2'):
                    correct = True
            elif stim_type == 'flower':
                if (stim_position == 'left' and key == '2') or (stim_position == 'right' and key == '1'):
                    correct = True
        
        # Display feedback for practice trials for 1 second
        if practice:
            feedback = "Correct!" if correct else "Try again!"
            feedback_text = visual.TextStim(win, text=feedback, height=2, color="black")
            feedback_text.draw()
            stimulus_rect.draw()
            win.flip()
            core.wait(1)
        
        # Blank screen immediately before next trial
        stimulus_rect.draw()
        win.flip()
        core.wait(blank_duration)

        # Record data
        thisExp.addData('Trial Number', trial_number)
        thisExp.addData('Condition', condition)
        thisExp.addData('Stimulus', stim_type)
        thisExp.addData('Position', stim_position)
        thisExp.addData('Key', key)
        thisExp.addData('Correct', correct)
        thisExp.addData('RT', rt)
        thisExp.nextEntry()

        # Update correct count for practice trials
        if practice and correct:
            correct_count += 1

    return correct_count

######################## RUNNING EXPERIMENT ###############################################################################################################################################################################################

prac_level = 0
exp_level = 0
# Run congruent and incongruent blocks -- with practice trials before experiment 
for condition in conditions[0:2]:
    correct_count = 0
    prac_level += 1
    repeat_count = 0  # Track how many times a practice level has been repeated

    while repeat_count < 2:  # Limit to 2 practice tries
        instructions.text = f"Practice Level {prac_level}\n\n\n\n\n\n\n\n\n"
        stimulus_rect.draw()
        fixation.draw()
        if condition == 'congruent':
            instructions2.text = "\n\n\n\n\n\n\n\n\nPress the button that's on the SAME SIDE as the heart!"
            heart_image.pos = (12.96, 0)
            heart_image.draw()
        elif condition == 'incongruent':
            instructions2.text = "\n\n\n\n\n\n\n\n\nPress the button that's on the OPPOSITE side as the flower!"
            flower_image.pos = (-12.96, 0)
            flower_image.draw()
        instructions.draw()
        instructions2.draw()
        win.flip()
        event.waitKeys(keyList=['space'])

        # Run the practice trials for the current condition
        correct_count = run_condition(condition, practice=True)
        
        # Check if accuracy is below 75%, end experiment if practice is failed twice in any block
        accuracy = (correct_count / practice_trials) * 100
        if accuracy < 75:
            repeat_count += 1
            print(f"{condition} Repeat {repeat_count}/2")
            if repeat_count == 2:
                instructions.text = "You finished the game!"
                instructions.draw()
                win.flip()
                event.waitKeys(keyList=['space'])
                print(f"Experiment Ended in condition: {condition}")
                core.quit()
            else:
                instructions.text = "Let's try that again!"
            instructions.draw()
            win.flip()
            event.waitKeys(keyList=['space'])
        else:
            break

    instructions.text = "Great job on that practice level!"
    instructions.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    # Running experimental trials
    exp_level += 1
    instructions.text = f"Game Level {exp_level}\n\nAre you ready?"
    instructions.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    run_condition(condition, practice=False)

# Running mixed trial -- no practice level
exp_level += 1
instructions.text = f"Game Level {exp_level}\n\nAre you ready?"
instructions.draw()
win.flip()
event.waitKeys(keyList=['space'])
run_condition('mixed', practice=False)

######################## SAVING DATA AND ENDING THE EXPERIMENT ###############################################################################################################################################################################################

thisExp.saveAsWideText(filename + '.csv', delim=',')
thisExp.saveAsPickle(filename)
thisExp.abort()

instructions.text = "Great job, you finished the game!"
instructions.draw()
win.flip()
event.waitKeys(keyList=['space'])
core.quit()
