% linebisection.m
% 
% 
% June 2016
% written by Na Yeon Kim 
%
% This is a clean version of linebisection.m
% This script takes three input values:
% subj = subject ID (in letter string)
% blockNum = run number 
% blockType = type of block 
%             (1 = 'which side is shorter?'; 2 = 'which side is longer?')
%
% April 2019 edited by Na Yeon Kim

function [wPtr,wOff] = linebisection(subj, blockNum, blockType, wPtr, wOff, rect, stimdur)

    DevId      = -1;
    
    HideCursor                     % hide the mouse
    rand('twister',sum(100*clock)); % initialize rand to a different state each time
    ListenChar(2);                  % suppress output to command window

    % --------------------------------------------------------- set up screen variables --------------------------------------------------------- %

    p.mon_width  	= 53.28; % monitor width = EIZO 53.28  
    p.v_dist 		= 60;   % distance - make sure you seat your subject 60 cm away 

    center = [rect(3) rect(4)]/2;                                               % center of screen (pixel coordinates), has x and y value
    centerLocx=center(1);                                                       % x coordinate of the center of the screen
    centerLocy=center(2);                                                       % y coordinate of the center of the screen

    pix_per_deg = pi * rect(3) / atan(p.mon_width/p.v_dist/2) / 360;            % pixels per degree
    lineThick = 0.1 * pix_per_deg;
    Screen('TextSize',wPtr,round(1*pix_per_deg));                               % font size
    QuestionLoc = centerLocy - 3 * pix_per_deg;

    % draw vertical line
    verLength = 2;
    verY_1 = centerLocy - 0.5 * verLength * pix_per_deg; 
    verY_2 = centerLocy + 0.5 * verLength * pix_per_deg; 

    % mask presentation 
    % Scene_imagesizeh = 640; % pixels of images- horizontal
    Scene_imagesizeh = rect(3)/2;
    % Scene_imagesizev = 480; % pixels of images- vertical
    Scene_imagesizev = rect(4)/2;
    Scene_Rect       = [0 0 Scene_imagesizeh Scene_imagesizev];

    % read mask files
    for m = 1:12
        Img = imread('Mask_BW.jpg');
        Img = cat(1, Img, Img);
        Img = cat(2, Img, Img);
        MaskText(m) = Screen('MakeTexture', wPtr, double(Img));
    end
    
    [Img_andy,~,alpha] = imread('green_andy.png');
    Img_andy(:,:,4) = alpha;
    AndyTexture = Screen('MakeTexture', wPtr, Img_andy);

    % % Load audio files
    % [nemoAudio, ~] = audioread('Nemo1.wav');
    % [doryAudio, Fs] = audioread('Dory1.wav');
    % 
    % % Upsample Nemo by factor of two to match Dory audio sampling period.
    % nemoAudio = repelem(nemoAudio,2,1);
    % 
    % % Add channel to Dory to move it from Mono to Stereo sound.
    % doryAudio = [doryAudio,doryAudio];
    % 
    % % Resample audio from 44.1kHz to 48kHz (for Windows audio driver).
    % nemoAudio = audioresample(nemoAudio, InputRate=Fs, OutputRate=48e3);
    % doryAudio = audioresample(doryAudio, InputRate=Fs, OutputRate=48e3);
    % Fs = 48e3;
    % 
    % InitializePsychSound(1); % Init sound driver and push for low-latency (1).
    % pahandle = PsychPortAudio('Open', [], 1, 1, Fs, 2);

    % --------------------------------------------------------- set up timing variables --------------------------------------------------------- %
    % exp.SceneDuration   = 1/60 * SceneDuration;         %change the refreshing rate 
    exp.FixQuestion     = 4;  % fixation with question for the following block 
    exp.DelayPeriod     = 1.5;
    exp.StimDuration    = stimdur;
    exp.MaskDuration    = 2;

    % ------------------------------------------------------------- set up trials ------------------------------------------------------------------ %
    Lengths = [20 21 22 23];    % line lengths = 20, 21, 22, 23 degrees visual angle
    Types = [1 2];              % location of vertical line = left (-shift) or right (+shift)
    verticalIdx = [-1 1];
    nTrials = 20;
    
    repeat_length = nTrials / length(Lengths);
    repeat_type   = nTrials / length(Types);
    exp.Lengths = Shuffle(repmat(Lengths, 1, repeat_length));
    exp.Types = Shuffle(repmat(Types, 1, repeat_type));
    exp.CorrAns = zeros(1, nTrials);
    if blockType == 1
        exp.CorrAns = exp.Types;
    elseif blockType == 2
        exp.CorrAns(exp.Types == 2) = 2;
        exp.CorrAns(exp.Types == 2) = 1;
        exp.CorrAns(exp.Types == 1) = 2;    % reversing the answers for the "longer" question 
    end

    % Must use number and symbol in order for external buttons to work. 
    KbName('UnifyKeyNames');
    keys     = [KbName('1!'), KbName('2@')]; % left, right, respectively
    spaceKey = KbName('Space');
    escKey = KbName('ESCAPE'); %

    % --------------------------------------------------------- set up growing variables  ---------------------------------------------------------------- %

    response        = zeros(nTrials,1);
    RT              = zeros(nTrials,1);
    TrialOnsetTime  = zeros(nTrials,1);
    StimulusOnset   = zeros(nTrials,1);
    MaskOnset       = zeros(nTrials,1);
    VerLocations    = zeros(nTrials,1);
    isCorrect       = zeros(nTrials,1);
    

    % ------------------------------------------------------------- Start of trial loop ------------------------------------------------------------------ %
    
     % Instruction screen
    QuestionLoc1 = centerLocy - 6 * pix_per_deg;
    QuestionLoc2 = centerLocy - 3 * pix_per_deg;
    QuestionLoc2_x = centerLocx + 4 * pix_per_deg; 
    QuestionLoc3_x = centerLocx - 4 * pix_per_deg;
    QuestionLoc4 = centerLocy + 6 * pix_per_deg;

    txt2 = 'Right';
    txt3 = 'Left';
    txt4 = 'Tell the experimenter when you are ready to begin the game!';
    
    if blockType == 1
        txtshort = 'Which side is shorter?';
        bounds = TextBounds(wOff, txtshort);
        txtsize = (bounds(3)-bounds(1))/2;       
        Screen('DrawText',wPtr,txtshort, centerLocx-1.5*txtsize,QuestionLoc1);
    elseif blockType == 2
        txtlong = 'Which side is longer?';
        bounds = TextBounds(wOff, txtlong);
        txtsize = (bounds(3)-bounds(1))/2;       
        Screen('DrawText',wPtr,txtlong, centerLocx-1.5*txtsize,QuestionLoc1);
    end
    
    Screen('DrawText',wPtr,txt2, QuestionLoc2_x, QuestionLoc2, [255 225 0]);
    Screen('DrawText',wPtr,txt3, QuestionLoc3_x, QuestionLoc2, [0 0 255]);

    bounds = TextBounds(wOff, txt4);
    txtsize = (bounds(3)-bounds(1))/2;
    Screen('DrawText',wPtr,txt4, centerLocx-1.5*txtsize, QuestionLoc4, [0 0 0]);
    
    img = imread('InstructLine.jpg');
    ImgTexture = Screen('MakeTexture', wPtr, img);
    Screen('DrawTexture', wPtr, ImgTexture);

    Screen('Flip', wPtr);

    keyisdown=0;
    [keyisdown, secs, keyCode] = KbCheck(DevId);
    while ~keyisdown
        [~, ~, keyCode] = KbCheck(DevId);
         if keyCode(spaceKey)
             keyisdown = 1;
         end

         if(keyCode(escKey)), break; end
    end

    % Start 
    
    rightcount = 0;
    VerLocations(1) = 1; % start from 1 deg away from the center 

    for trial = 1:nTrials

        pressed = 0;

        % ------- delay period (1.5 sec) ------ %

        % andy face for fixation
        Screen('DrawTexture', wPtr, AndyTexture);

        TrialOnset(trial) = Screen('Flip', wPtr);
        while GetSecs - TrialOnset(trial) < exp.DelayPeriod
            [keyisdown, secs, keyCode] = KbCheck(DevId);
            if keyCode(escKey); Screen('CloseAll'); ListenChar(0);ShowCursor; return; end
        end
        %

        % ------- stimulus presentation ------ %
        lineLength = exp.Lengths(trial);
        verLocation = centerLocx + VerLocations(trial) * verticalIdx(exp.Types(trial)) * pix_per_deg;
        lineX_1 = centerLocx - 0.5 * lineLength * pix_per_deg; 
        lineX_2 = centerLocx + 0.5 * lineLength * pix_per_deg; 

        Screen('DrawLine', wPtr,  [0 0 0], lineX_1, centerLocy, lineX_2, centerLocy, lineThick);
        Screen('DrawLine', wPtr,  [0 0 0], verLocation, verY_1, verLocation, verY_2, lineThick);

        StimulusOnset(trial) = Screen('Flip', wPtr);
        while GetSecs - TrialOnset(trial) < (exp.DelayPeriod + exp.StimDuration)
            [keyisdown, secs, keyCode] = KbCheck(DevId);
            if and(keyisdown,~isempty(find(keyCode(keys),1)))
                if length(find(keyCode))<2
                    if pressed==0
                        RT(trial,1) = secs-StimulusOnset(trial);
                        response(trial) = find(keyCode(keys));
                        pressed = 1;
                    end
                end
            end
        end


        % ------- mask presentation ------ %

        Screen('DrawTexture', wPtr, MaskText(randsample(1:12,1)), Scene_Rect);  
        MaskOnset(trial) = Screen('Flip', wPtr);

        while GetSecs - TrialOnset(trial) < (exp.DelayPeriod + exp.StimDuration + exp.MaskDuration)
            [keyisdown, secs, keyCode] = KbCheck(DevId);
            if and(keyisdown,~isempty(find(keyCode(keys),1)))
                if length(find(keyCode))<2
                    if pressed==0
                        RT(trial,1) = secs-StimulusOnset(trial);
                        response(trial) = find(keyCode(keys));
                        pressed = 1;
                    end
                end
            end
        end
        % ------------ Feedback Audio ----------------- %

        % if isCorrect(trial) == 1
        %     PsychPortAudio('FillBuffer', pahandle, nemoAudio');
        % elseif isCorrect(trial) == 0
        %     PsychPortAudio('FillBuffer', pahandle, doryAudio');
        % end
        % 
        % PsychPortAudio('Start', pahandle);

        % ------- line bisection staircase ------ %
        isCorrect(trial) = (response(trial) == exp.CorrAns(trial));

        if isCorrect(trial) == 1

            rightcount = rightcount + 1;

            if rightcount == 2                        % if this is the second right trial in a row (rightcount is at 2)
                rightcount = 0;                         % reset the tally to 0
                VerLocations(trial+1)  = VerLocations(trial) * 0.8; % reduce the shift to 80%

            elseif rightcount < 2
                VerLocations(trial+1) = VerLocations(trial);
            end

        elseif isCorrect(trial) == 0
            rightcount = 0;
            VerLocations(trial+1) = VerLocations(trial) / 0.8;
        end

    end

    % ---------------------------------------------------------- End of experiment  ----------------------------------------------------------------- %
    outDir = ['./log/', subj];
    mkdir(outDir);
    save(fullfile(outDir, [subj 'linebisection_block' num2str(blockNum) '_results.mat']));
    
    


return;