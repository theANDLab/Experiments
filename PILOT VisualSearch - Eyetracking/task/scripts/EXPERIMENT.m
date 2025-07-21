function [window] = EXPERIMENT(window, SubID, TaskCB, FeatureCB, searchType, featureType, outputDirectory)

% Disable keyboard, hide cursor
ListenChar(2);
HideCursor;

global EP;
global FP;
global CP;
global FV;
global CV;

if strcmp(searchType, 'feature') && strcmp(featureType, 'luminance')

    % Translate the human-readable esthetics structure into something easier
    % for PsychToolBox to operate with.
    visualTypes = GetVisualTypes(FV.luminance, window);
    visualMotionTypes = GetVisualTypes(FV.luminanceMotion, window);
    
    BaseStructParams = FP.luminance;
    
elseif strcmp(searchType, 'feature') && strcmp(featureType, 'color')
    
	% Translate the human-readable esthetics structure into something easier
    % for PsychToolBox to operate with.
    visualTypes = GetVisualTypes(FV.color, window);
    visualMotionTypes = GetVisualTypes(FV.colorMotion, window);
    
    BaseStructParams = FP.color;

elseif strcmp(searchType, 'conjunction') && strcmp(featureType, 'luminance')
    
    % Translate the human-readable esthetics structure into something easier
    % for PsychToolBox to operate with.
    visualTypes = GetVisualTypes(CV.luminance, window);
    
    BaseStructParams = CP.luminance;
    
elseif strcmp(searchType, 'conjunction') && strcmp(featureType, 'color')
    
    visualTypes = GetVisualTypes(CV.color, window);
    
    BaseStructParams = CP.color;
    
else 
    error('ERROR: invalid searchType and/or featureType')
    
end

% make background color specific to feature manipulation 
Screen('FillRect', window, BaseStructParams.BackgroundColor);

% Let PTB know what keys to monitor.
KbName('UnifyKeyNames');
leftresponseKey = KbName('1!'); % left key
rightresponseKey = KbName('2@'); % right key
repeatKey = KbName('r');
escKey = KbName('ESCAPE'); %
spaceKey = KbName('Space');
activeKeys = [leftresponseKey, rightresponseKey, repeatKey, escKey, spaceKey];
RestrictKeysForKbCheck(activeKeys);

% Produce two practice structures; one for walk through and one realistic.
numTrueTrials = 10;
[pracInstruct, pracTrials, pracMotionTrials] = GenPracticeStructure(...
    BaseStructParams, numTrueTrials, searchType);


%% INSTRUCTIONS

instructFiles = dir(strcat(pwd, filesep, ...
    'instructions', ...
    filesep, searchType, ...
    filesep, featureType, ...
    filesep, '*Instructions*png'));

completeInstruction = false; 
repeatInstruction = true;
while repeatInstruction
    for i = 1:size(instructFiles,1)
        % specifiy and read instruction images
        instructName = [instructFiles(i).folder filesep instructFiles(i).name];
        [instructImg, ~, ~] = imread(instructName, 'png');
        imgPtr = Screen('MakeTexture', window, instructImg);

        [dstRect] = scaleImgToScreen(instructImg, 1, EP.W_WIDTH/2, EP.W_HEIGHT/2);

        Screen('DrawTexture', window, imgPtr, [], dstRect);

        % display image
        Screen('Flip', window);
        WaitSecs(.25);

            % wait for spaceKey to advance to next image
            wait=true;
            while wait
                [~, ~, keyCode, ~] = KbCheck; 

               if keyCode(spaceKey)
                    wait=false;

                end
                
                if(keyCode(escKey)), break; end

            end % while wait
            
            if(keyCode(escKey)), break; end
            
    end % for instructFiles
    
    %% Check to see if instructions should be repeated
    line1 = 'Instructions';
    line2 = '\n AGAIN?';
    [nx, ny, ~] = DrawFormattedText(window, [line1 line2], 'center', 'center', 1);
    Screen('DrawText', window, '', nx, ny, [255, 0, 0, 255]);

    Screen('Flip', window);
    WaitSecs(.25);

    wait=true;
    while wait
        [~, ~, keyCode] = KbCheck; 

        if keyCode(spaceKey)
            completeInstruction = true; 
            repeatInstruction=false;
            wait=false;
            
            % displayFixation

        end

        if keyCode(repeatKey)
            repeatInstruction = true;
            wait=false;

        end
        
        if(keyCode(escKey)), break; end

    end % while wait
    
    if(keyCode(escKey)), break; end
    
 end % while repeatInstruction

%% PRACTICE 

if completeInstruction

    switch searchType

        case 'feature'

            line1 = 'Try some practice!';
            [nx, ny, ~] = DrawFormattedText(window, line1, 'center', 'center', 1);
            Screen('DrawText', window, '', nx, ny, [255, 0, 0, 255]);
            Screen('Flip', window); 
            
            % wait for spaceKey to advance to next practice round
            wait=true;
            while wait
                [~, ~, keyCode] = KbCheck; 
            
                if keyCode(spaceKey)
                    wait=false;
            
                end
            
            end % while wait
            
            displayFixation

        switch FeatureCB

            case '1' % STATIC, DYNAMIC

                % Run the 'real' STATIC practice structure.
                pracacc = 0;
                while pracacc < 60
    
                    [pracoutput] = RunPractice(window, searchType, featureType, pracTrials, BaseStructParams, visualTypes);
                    pracacc = (sum(pracoutput.Accuracy)/length(pracTrials))*100;
    
                    if pracacc >= 60
                        % Show 'great job' and wait for keypress to continue.
                        line1 = 'Great job!';
    
                    elseif pracacc <60
                        % Show 'let's try again!' and wait for keypress to continue.
                        line1 = 'Let`s try again!';
                    end 
    
                    [nx, ny, ~] = DrawFormattedText(window, line1, 'center', 'center', 1);
                    Screen('DrawText', window, '', nx, ny, [255, 0, 255]);
                    Screen('Flip', window);
                    WaitSecs(.25);
    
                    % wait for spaceKey to advance to next practice round
                    wait=true;
                    while wait
                        [~, ~, keyCode] = KbCheck; 
                    
                        if keyCode(spaceKey)
                            wait=false;
                    
                        end
                    
                    end % while wait
                    
                    displayFixation
    
                end
    
                % Run the 'real' DYNAMIC practice structure.
                pracacc = 0;
                while pracacc < 60
    
                    [pracoutput] = RunPractice(window, searchType, featureType, pracMotionTrials, BaseStructParams, visualMotionTypes);
                    pracacc = (sum(pracoutput.Accuracy)/length(pracTrials))*100;
    
                    if pracacc >= 60
                        % Show 'great job' and wait for keypress to continue.
                        line1 = 'Great job!';
    
                    elseif pracacc <60
                        % Show 'let's try again!' and wait for keypress to continue.
                        line1 = 'Let`s try again!';
                    end 
    
                    [nx, ny, ~] = DrawFormattedText(window, line1, 'center', 'center', 1);
                    Screen('DrawText', window, '', nx, ny, [255, 0, 255]);
                    Screen('Flip', window);
                    WaitSecs(.25);
    
                    % wait for spaceKey to advance to next practice round
                    wait=true;
                    while wait
                        [~, ~, keyCode] = KbCheck; 
                    
                        if keyCode(spaceKey)
                            wait=false;
                    
                        end
                    
                    end % while wait
    
                    displayFixation

                end
            
            case '2' % DYNAMIC, STATIC

                % Run the 'real' DYNAMIC practice structure.
                pracacc = 0;
                while pracacc < 60
    
                    [pracoutput] = RunPractice(window, searchType, featureType, pracMotionTrials, BaseStructParams, visualMotionTypes);
                    pracacc = (sum(pracoutput.Accuracy)/length(pracTrials))*100;
    
                    if pracacc >= 60
                        % Show 'great job' and wait for keypress to continue.
                        line1 = 'Great job!';
    
                    elseif pracacc <60
                        % Show 'let's try again!' and wait for keypress to continue.
                        line1 = 'Let`s try again!';
                    end 
    
                    [nx, ny, ~] = DrawFormattedText(window, line1, 'center', 'center', 1);
                    Screen('DrawText', window, '', nx, ny, [255, 0, 255]);
                    Screen('Flip', window);
                    WaitSecs(.25);
    
                    % wait for spaceKey to advance to next practice round
                    wait=true;
                    while wait
                        [~, ~, keyCode] = KbCheck; 
                    
                        if keyCode(spaceKey)
                            wait=false;
                    
                        end
                    
                    end % while wait
    
                    displayFixation
                end

                % Run the 'real' STATIC practice structure.
                pracacc = 0;
                while pracacc < 60
    
                    [pracoutput] = RunPractice(window, searchType, featureType, pracTrials, BaseStructParams, visualTypes);
                    pracacc = (sum(pracoutput.Accuracy)/length(pracTrials))*100;
    
                    if pracacc >= 60
                        % Show 'great job' and wait for keypress to continue.
                        line1 = 'Great job!';
    
                    elseif pracacc <60
                        % Show 'let's try again!' and wait for keypress to continue.
                        line1 = 'Let`s try again!';
                    end 
    
                    [nx, ny, ~] = DrawFormattedText(window, line1, 'center', 'center', 1);
                    Screen('DrawText', window, '', nx, ny, [255, 0, 255]);
                    Screen('Flip', window);
                    WaitSecs(.25);
    
                    % wait for spaceKey to advance to next practice round
                    wait=true;
                    while wait
                        [~, ~, keyCode] = KbCheck; 
                    
                        if keyCode(spaceKey)
                            wait=false;
                    
                        end
                    
                    end % while wait
                    
                    displayFixation
    
                end
        end

        case 'conjunction'

            displayFixation

            % Run the 'walk through' practice structure.
            RunWalkThrough(window, pracInstruct, visualTypes);
            displayFixation
    
            % Run the 'real' practice structure.
            pracacc = 0;
            while pracacc < 60
    
                [pracoutput] = RunPractice(window, searchType, featureType, pracTrials, BaseStructParams, visualTypes);
                pracacc = (sum(pracoutput.Accuracy)/length(pracTrials))*100;
    
                if pracacc >= 60
                    % Show 'great job' and wait for keypress to continue.
                    line1 = 'Great job!';
    
                elseif pracacc <60
                    % Show 'let's try again!' and wait for keypress to continue.
                    line1 = 'Let`s try again!';
                end 
    
                [nx, ny, ~] = DrawFormattedText(window, line1, 'center', 'center', 1);
                Screen('DrawText', window, '', nx, ny, [255, 0, 255]);
                Screen('Flip', window);
                WaitSecs(.25);
    
                % wait for spaceKey to advance to next practice round
                wait=true;
                while wait
                    [~, ~, keyCode] = KbCheck; 
                
                    if keyCode(spaceKey)
                        wait=false;
                
                    end
                
                end % while wait
                
                displayFixation
    
            end

    end
    
elseif ~completeInstruction 

    Screen('CloseAll')
    
    % bring cursor back to command window
    ListenChar(0);
    ShowCursor;
    
    error('Instructions not presented.')
    
end

% Show 'Press to start' and wait for keypress to continue.
line1 = 'Are you ready?';
[nx, ny, ~] = DrawFormattedText(window, line1, 'center', 'center', 1);
Screen('DrawText', window, '', nx, ny, [255, 0, 255]);
Screen('Flip', window);
WaitSecs(.25);

% wait for spaceKey to advance e
wait=true;
while wait
    [~, ~, keyCode] = KbCheck; 

    if keyCode(spaceKey)
        wait=false;

    end

end % while wait

%% Display fixation screen.

displayFixation

%initialize dataset structure
userData = table([],[],[],[],[],[],[],[],[],[],[]);

%% RUN TRIALS

for block = 1:BaseStructParams.NumBlocks

    % Run the trial using the user's trial structure, experiment parameters,
    % and the description of type esthetics. Returns an array of the user's
    % response time for each trial, with -1 denoting no-response.

    %% ADD IF STATEMENT TO CHOOSE WHICH GenUserStructure FUNCTION TO USE
    switch searchType

        case 'feature'

            % Produce this user's (real) trial structure for each block.
            switch FeatureCB

                case '1'

                    switch mod(block,2)   

                        case 1
                        % if block is odd then do this
                        userStructure = GenUserStructure(BaseStructParams);
                        
                        motionType = 'NoMotion';
                        
                        save(strcat(outputDirectory, SubID, '_',... 
                            searchType, '_', featureType, '_', motionType, ...
                            '_', 'userStructure.mat'), 'userStructure')
                        
                        [userOutput] = RunTrial(window, searchType, featureType, ...
                            userStructure, BaseStructParams, visualTypes);

                        case 0
                        % if block is even, then do this 
                        % userStructure = GenUserStructureMixed(BaseStructParams);
                        userStructure = GenUserStructure(BaseStructParams);
                        
                        motionType = 'Motion';
                        
                        save(strcat(outputDirectory, SubID, '_',... 
                            searchType, '_', featureType, '_', motionType, ...
                            '_', 'userStructure.mat'), 'userStructure')
                        
                       [userOutput] = RunTrial(window, searchType, featureType, ...
                            userStructure, BaseStructParams, visualMotionTypes);
                        
                    end

                case '2'

                    switch mod(block,2)   

                        case 1
                        % if block is odd then do this
                        % userStructure = GenUserStructureMixed(BaseStructParams);
                        userStructure = GenUserStructure(BaseStructParams);
                        
                        motionType = 'Motion';
                        
                        save(strcat(outputDirectory, SubID, '_',... 
                            searchType, '_', featureType, '_', motionType, ...
                            '_', 'userStructure.mat'), 'userStructure')
                        
                        [userOutput] = RunTrial(window, searchType, featureType, ...
                            userStructure, BaseStructParams, visualMotionTypes);

                        case 0
                        % if block is even, then do this 
                        userStructure = GenUserStructure(BaseStructParams);
                        
                        motionType = 'NoMotion';
                        
                        save(strcat(outputDirectory, SubID, '_',... 
                            searchType, '_', featureType, '_', motionType, ...
                            '_', 'userStructure.mat'), 'userStructure')
                        
                        [userOutput] = RunTrial(window, searchType, featureType, ...
                            userStructure, BaseStructParams, visualTypes);

                    end
            end

        case 'conjunction'

            userStructure = GenUserStructure(BaseStructParams);
            
            motionType = 'Motion';
            
            save(strcat(outputDirectory, SubID, '_',... 
                searchType, '_', featureType, '_', motionType, ...
                '_', 'userStructure.mat'), 'userStructure')
            
            [userOutput] = RunTrial(window, searchType, featureType, ...
                userStructure, BaseStructParams, visualTypes);

    end




%% Combine block data with trial output

    numTrials = numel(userStructure);
    blockData = array2table(transpose([...
    transpose(str2num(SubID) .* ones(numTrials,1)); ...
    transpose(block .* ones(numTrials,1))]));

    motionPresent = cellstr(repmat(motionType,numTrials,1));    

    blockData = [blockData motionPresent];

    blockData.Properties.VariableNames = {...
            'SubID', 'Block', 'MotionPresent'};
    
    userResults=[blockData userOutput];
    
    userData.Properties.VariableNames = userResults.Properties.VariableNames;
    
    userData = [userData; userResults];

    %take a break between blocks
    if block < BaseStructParams.NumBlocks
        takeBreak(window);
    end

end

% reorder variable names for export
userData = movevars(userData, 'MotionPresent', 'After', 'Feature');


%% Export data
writetable(userData, strcat(outputDirectory, SubID, '_',...
    searchType, '_', featureType,...
    '_output.txt'), 'Delimiter', '\t')

calculateVariables(SubID, outputDirectory, searchType, featureType, userData);

%% Take a break & Wait for Next Experiment, exit with any key press
window = waitNextExperiment(window, EP.W_WIDTH, EP.W_HEIGHT);

%% bring cursor back to command window
ListenChar(0);
ShowCursor;

% Clear and close all open screens.
% sca;
% clearvars -except SubID userData

end

%% NESTED FUNCTIONS

function [window] = waitNextExperiment(window, width, height)

    % Begin drawing screen
    Screen('DrawText', window, 'Ready for NEXT EXPERIMENT?', (width/4), (height/2), 1);
    %need to move this once screen size is determined
    % Flip to the screen
    Screen('Flip', window);

    KbWait;

end 