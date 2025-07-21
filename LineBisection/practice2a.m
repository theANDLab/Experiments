%%% Practice round 2a---line is flashed quickly and then they make their decision 

%Practice trial

function practice2a(subj, blockNum, blockType)


    DevId      = -1;

    % HideCursor                     % hide the mouse
    rand('twister',sum(100*clock)); % initialize rand to a different state each time
    ListenChar(2);                  % suppress output to command window


    % --------------------------------------------------------- set up screen variables --------------------------------------------------------- %

    p.mon_width  	= 31.4; 
    p.v_dist 		= 30; 

    Screen('Preference', 'SkipSyncTests', 2);

    ScreenNum = max(Screen('Screens'));
    [wPtr, rect] = Screen('OpenWindow', ScreenNum, [128, 128, 128], []);            % open the screen
    wOff         = Screen(wPtr, 'OpenOffscreenWindow', [128, 128, 128], []);        % Offscreen buffers% open the screen

    center = [rect(3) rect(4)]/2;                                                   % center of screen (pixel coordinates), has x and y value
    centerLocx=center(1);                                                           % x coordinate of the center of the screen
    centerLocy=center(2);                                                           % y coordinate of the center of the screen

    pix_per_deg = pi * rect(3) / atan(p.mon_width/p.v_dist/2) / 360;                % pixels per degree
    lineThick = 0.1 * pix_per_deg;
    Screen('TextSize',wPtr,20);    
    QuestionLoc = centerLocy - 4 * pix_per_deg;

    % draw vertical line
    verLength = 2;
    verY_1 = centerLocy - 0.5 * verLength * pix_per_deg; 
    verY_2 = centerLocy + 0.5 * verLength * pix_per_deg; 

    % mask presentation 
    Scene_imagesizeh = 640;                                                          % pixels of images- horizontal
    Scene_imagesizev = 480;                                                          % pixels of images- vertical
    Scene_Rect       = [0 0 Scene_imagesizeh Scene_imagesizev];

    
    Img_smile = imread('smiley2.jpg');
    SmileTexture = Screen('MakeTexture', wPtr, Img_smile);

    % --------------------------------------------------------- set up timing variables --------------------------------------------------------- %
    % exp.SceneDuration   = 1/60 * SceneDuration;         %change the refreshing rate 
    exp.FixQuestion     = 4;  % fixation with question for the following block 
    exp.DelayPeriod     = 1.5;
    exp.StimDuration    = 0.2;
    exp.MaskDuration    = 2;

    % ------------------------------------------------------------- set up trials ------------------------------------------------------------------ %
    Lengths = [20 21 22 23];    % line lengths = 20, 21, 22, 23 degrees visual angle
    Types = [1 2];            % location of vertical line = left (-shift) or right (+shift)
    verticalIdx = [-1 1];
    nTrials = 8;
    
    repeat_length = nTrials / length(Lengths);
    repeat_type   = nTrials / length(Types);
    % blockType = 1;              % 1 = shorter, 2 = longer (reversed)
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

    keys     = [KbName('1!'), KbName('2@')]; % left, right, respectively 

    % --------------------------------------------------------- set up growing variables  ---------------------------------------------------------------- %

    response        = zeros(nTrials,1);
    RT              = zeros(nTrials,1);
    TrialOnsetTime  = zeros(nTrials,1);
    StimulusOnset   = zeros(nTrials,1);
    StimulusOffset  = zeros(nTrials,1);
    MaskOnset       = zeros(nTrials,1);
    VerLocations    = zeros(nTrials,1);
    isCorrect       = zeros(nTrials,1);
    

    % ------------------------------------------------------------- Start of trial loop ------------------------------------------------------------------ %
    
    % Instruction screen
    QuestionLoc1 = centerLocy - 8 * pix_per_deg;
    QuestionLoc2 = centerLocy - 4 * pix_per_deg;
    QuestionLoc2_x = centerLocx + 6 * pix_per_deg; 
    QuestionLoc3_x = centerLocx - 6 * pix_per_deg;
    QuestionLoc4 = centerLocy + 8 * pix_per_deg;
    QuestionLoc5 = centerLocy - 12 * pix_per_deg;
    
    txt2 = 'Right';
    txt3 = 'Left';
    txt4 = 'Tell the experimenter when you understand the instructions.';
    txt5 = '***THIS IS A PRACTICE ROUND***';
    
    if blockType == 1
        txtshort = 'Which side is shorter?';
        bounds = TextBounds(wOff, txtshort);
        txtsize = (bounds(3)-bounds(1))/2;       
        Screen('DrawText',wPtr,txtshort, centerLocx-txtsize*0.8,QuestionLoc1);
    elseif blockType == 2
        txtlong = 'Which side is longer?';
        bounds = TextBounds(wOff, txtlong);
        txtsize = (bounds(3)-bounds(1))/2;       
        Screen('DrawText',wPtr,txtlong, centerLocx-txtsize*0.8,QuestionLoc1);
    end

    bounds = TextBounds(wOff, txt4);
    txtsize = (bounds(3)-bounds(1))/2;
    
    Screen('DrawText',wPtr,txt2, QuestionLoc2_x, QuestionLoc2, [255 225 0]);
    Screen('DrawText',wPtr,txt3, QuestionLoc3_x, QuestionLoc2, [0 0 255]);
    Screen('DrawText',wPtr,txt4, centerLocx - txtsize*0.8, QuestionLoc4, [0 0 0]);

    bounds2 = TextBounds(wOff, txt5);
    txtsize2 = (bounds2(3)-bounds2(1))/2;    
    Screen('DrawText',wPtr,txt5, centerLocx - txtsize2*0.8, QuestionLoc5, [0 0 0]);

    img = imread('InstructLine.jpg');
    ImgTexture = Screen('MakeTexture', wPtr, img);
    Screen('DrawTexture', wPtr, ImgTexture);
    
    Screen('Flip', wPtr);

    keyisdown=0;
    [keyisdown, secs, keyCode] = KbCheck(DevId);
    while ~keyisdown
        [keyisdown, secs, keyCode] = KbCheck(DevId);
    end
    
    rightcount = 0;
    VerLocations(1) = 1; % start from 1 pixels away from the center 
    
    for trial = 1:nTrials

        pressed = 0;

        % ------- delay period (1.5 sec) ------ %
        
        Screen('DrawTexture', wPtr, SmileTexture);

        TrialOnset(trial) = Screen('Flip', wPtr);
        while GetSecs - TrialOnset(trial) < exp.DelayPeriod
            [keyisdown, secs, keyCode] = KbCheck(DevId);
            if find(keyCode)==27; Screen('CloseAll'); ListenChar(0); return; end
        end

        % ------- stimulus presentation ------ %
        lineLength = exp.Lengths(trial);
        verLocation = centerLocx + VerLocations(trial) * verticalIdx(exp.Types(trial)) * pix_per_deg;
        lineX_1 = centerLocx - 0.5 * lineLength * pix_per_deg; 
        lineX_2 = centerLocx + 0.5 * lineLength * pix_per_deg; 

        Screen('DrawLine', wPtr,  [0 0 0], lineX_1, centerLocy, lineX_2, centerLocy, lineThick);
        Screen('DrawLine', wPtr,  [0 0 0], verLocation, verY_1, verLocation, verY_2, lineThick);

        StimulusOnset(trial) = Screen('Flip', wPtr);
        
        exp.StimDurationPract    = 2;  %%%This tells how long the line will appear on the screen before disappearing
        
        while GetSecs - StimulusOnset(trial) < exp.StimDurationPract
            [keyisdown, secs, keyCode] = KbCheck(DevId);
            if and(keyisdown,~isempty(find(keyCode(keys),1)))
                if length(find(keyCode))<2
                    if pressed==0
                        RT(trial,1) = secs-StimulusOnset(trial);
                        response(trial) = find(keyCode(keys));
                        pressed = 1;
                        if response(trial) == exp.CorrAns(trial)
                            isCorrect(trial) = 1;
                        end
                    end
                end
            end
            if find(keyCode)==27; Screen('CloseAll'); ListenChar(0); return; end
        end
        
        StimulusOffset(trial) = Screen('Flip', wPtr);
        
        keyisdown=0;
        [keyisdown, secs, keyCode] = KbCheck(DevId);
        
        if ~pressed
            while ~keyisdown
                [keyisdown, secs, keyCode] = KbCheck(DevId);
                if and(keyisdown,~isempty(find(keyCode(keys),1)))
                    if length(find(keyCode))<2
                        if pressed==0
                            RT(trial,1) = secs-StimulusOnset(trial);
                            response(trial) = find(keyCode(keys));
                            pressed = 1;
                            if response(trial) == exp.CorrAns(trial)
                                isCorrect(trial) = 1;
                            end
                        end
                    end
                end
            end
        end

        VerLocations(trial+1)  = VerLocations(trial);


        
        % ------------ Feedback ----------------- %

        if isCorrect(trial) == 1
            Feedback = 'Correct! Great job!';
        elseif isCorrect(trial) == 0
            Feedback = 'Uh oh, incorrect but you can do it!';
        end

        bounds2 = TextBounds(wOff, Feedback);
        txtsize2 = (bounds2(3)-bounds2(1))/2;    
        Screen('DrawText',wPtr,Feedback, centerLocx - txtsize2*0.8, centerLocy, [0 0 0]);
    
        Screen('Flip', wPtr);
        
        WaitSecs(2);

    end

    % ---------------------------------------------------------- End of experiment  ----------------------------------------------------------------- %
    outDir = ['./log/', subj];
    mkdir(outDir);
    save(fullfile(outDir, [subj 'linebisection_practice2a' num2str(blockNum) '_results.mat']));
    
    
    % ---------------------------------------------------------- End Screen  ----------------------------------------------------------------- 

    Screen('CloseAll');
    ListenChar(0);

return;                                                                 

