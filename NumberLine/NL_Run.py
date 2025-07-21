from psychopy import visual, core, event, data, gui
import random
import os
import csv
import re

######################## EXPERIMENT SETUP #####################################################################################################################################################################################################

exp_name = 'Number Line Task'
exp_info = {'participant_id': '','session': ''}
dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)
if dlg.OK == False:
    core.quit()

# Path to file where data will be saved
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

filename = os.path.join(data_folder, 'numline_' + exp_info['participant_id']+ exp_info['session'])
thisExp = data.ExperimentHandler(name=exp_name, version='',
                                 extraInfo=exp_info, runtimeInfo=None,
                                 originPath='',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

# Create a window
win = visual.Window(size = [1920, 1200], color="white", units="pix", fullscr=True, screen =1, monitor='Eizo',
winType='pyglet', allowGUI=False, allowStencil=False, blendMode='avg', useFBO=True,)
            

# Load images to display after each trial
image_paths = [
    "C:/Users/andlab.AS-LF315-1/Documents/Experiments/NumberLine/images/blue_andy.png",
    "C:/Users/andlab.AS-LF315-1/Documents/Experiments/NumberLine/images/green_andy.png",
    "C:/Users/andlab.AS-LF315-1/Documents/Experiments/NumberLine/images/purple_andy.png",
    "C:/Users/andlab.AS-LF315-1/Documents/Experiments/NumberLine/images/yellow_andy.png"
]

# Instructions text
welcome_text = '''
You are about to see a number line and a number.

Click where you think the number goes on the number line, then say "Ready" when you are ready to submit your answer. 

Let's practice!
'''
instructions = visual.TextStim(win, text=welcome_text, color="black", units='pix', height=60, wrapWidth = 1700)

# Display instructions and wait for the space bar to start the experiment
instructions.draw()
win.flip()
event.waitKeys(keyList=['space'])

########################  PARAMETERS ###############################################################################################################################################################################################################

# Marker characteristics
marker = visual.Circle(win, radius=6, fillColor="red", lineColor="red")

# Initialize lists pf target numbers. All pts will see the same experiment target #s
prac_targets = [10, int(random.uniform(1,9)), int(random.uniform(11,19))] # Always start with midpoint
exp_targets = [3,4,6,8,12,14,17,18,21,24,25,29,33,39,42,48,52,57,61,64,72,79,81,84,90,96] # From (Booth & Siegler, 2006)

######################## FUNCTIONS #################################################################################################################################################################################################################

# Running one trial
def run_trial(lower_bound, upper_bound, target_value):
    line_length = random.choice(range(500, 1001, 100))  # Random line length between 500 and 1000, in steps of 100
    line_start = (-line_length / 2, 0)  
    line_end = (line_length / 2, 0)  # Number line is centered in the middle of the screen

    # Create a line object
    line = visual.Line(win, start=line_start, end=line_end, lineColor="black", lineWidth=4)

    # Create tick objects for upper and lower bounds
    ticks = [
        visual.Line(win, start=(line_start[0], -14), end=(line_start[0], 10), lineColor="black",lineWidth=4),
        visual.Line(win, start=(line_end[0], -14), end=(line_end[0], 10), lineColor="black", lineWidth=4)
    ]

    # Create number labels for upper and lower bounds
    labels = [
        visual.TextStim(win, text=str(lower_bound), pos=(line_start[0], -30), color="black", height=30),
        visual.TextStim(win, text=str(upper_bound), pos=(line_end[0], -30), color="black", height=30)
    ]

    # Display target number
    target_text = visual.TextStim(win, text=f"{target_value}", pos=(line_start[0], 200), color="blue", height=40)

    # Variables to store response and timing
    selected_value = None
    rt_clock = core.Clock()

    while True:
        # Draw number line, ticks, labels, and target text
        line.draw()
        for tick in ticks:
            tick.draw()
        for label in labels:
            label.draw()
        target_text.draw()

        # Get mouse position and check for clicks
        mouse = event.Mouse(win=win)
        if mouse.getPressed()[0]:  # Check if left mouse button is clicked
            mouse_pos = mouse.getPos()
            # Map x coordinate to number line
            selected_value = ((mouse_pos[0] + line_length / 2) / line_length) * (upper_bound - lower_bound) + lower_bound
            # Stored selected value will always be within the number line bounds
            if selected_value < lower_bound:
                selected_value = lower_bound
            elif selected_value >upper_bound:
                selected_value = upper_bound
            
            # Update marker position, keeping it within number line bounds
            marker_x_pos = max(min(mouse_pos[0], line_end[0]), line_start[0])
            marker.pos = (marker_x_pos, 0)

        # Draw the marker if a selection has been made
        if selected_value is not None:
            marker.draw()

        win.flip()

        # Check for button press before moving to next trial
        keys = event.getKeys()
        if selected_value is not None and '1' in keys: 
            return target_value, selected_value, rt_clock.getTime(), line_length
        elif 'escape' in keys:
            core.quit()

######  RUNNING THE EXPERIMENT  ###############################################################################################################################################################################

# Run 3 practice trials on a smaller range (0,20)
print("Starting practice trials...")
for prac_target in prac_targets:
    target_value, selected_value, rt, line_length = run_trial(0, 20, prac_target)
    print(f" Target={prac_target}, Response={selected_value:.3f}, RT={rt:.3f}s")
    
    # Record data
    thisExp.addData('trial', 'Practice')
    thisExp.addData('target_value', prac_target)
    thisExp.addData('selected_value', round(selected_value,3))
    thisExp.addData('reaction_time', round(rt,3))
    thisExp.addData('line_length',line_length)
    thisExp.nextEntry()
    
# Confirm readiness for the main experiment
ready_text = "Great job on the practice! Now let's play the real game!"
ready_stim = visual.TextStim(win, text=ready_text, color="black", units='pix', height=60, wrapWidth = 1700)
ready_stim.draw()
win.flip()
event.waitKeys(keyList=['space'])

# Shuffle main experiment target presentation order for each participant
random.shuffle(exp_targets)

# Run experiment trials
print("Starting experiment trials...")
for target in exp_targets:
    target_value, selected_value, rt, line_length = run_trial(0, 100, target)
    print(f"Trial {exp_targets.index(target)+1}: Target={target}, Response={selected_value:.3f}, RT={rt:.3f}s")
    
    # Record data
    thisExp.addData('trial', exp_targets.index(target)+1)
    thisExp.addData('target_value', target)
    thisExp.addData('selected_value', round(selected_value,3))
    thisExp.addData('reaction_time', round(rt,3))
    thisExp.addData('line_length',line_length)
    thisExp.nextEntry()
    
    # Display randomly selected image after each trial    
    selected_image = random.choice(image_paths)
    image_stim = visual.ImageStim(win, image=selected_image, size=(100, 100))
    image_stim.draw()
    win.flip()
    
    # Image will display for 1 second
    core.wait(1.0)   
    
######  SAVING THE DATA  #####################################################################################################################################################################################

thisExp.saveAsWideText(filename + '.csv', delim=',')
thisExp.saveAsPickle(filename)
thisExp.abort()

print(f"Results saved as {filename}.")

######  ENDING THE EXPERIMENT  #########################################################################################################################################################################################

# Exit screen
exit_text = visual.TextStim(win, color='black', text='Great job! You finished the game!', units='pix', height=50, wrapWidth = 1700)
exit_text.draw()
win.flip()
event.waitKeys(keyList=['space'])

# Close the window after all trials are completed
win.close()
core.quit()
