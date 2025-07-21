

DevId      = -1;

HideCursor                     % hide the mouse
rand('twister',sum(100*clock)); % initialize rand to a different state each time
% ListenChar(2);                  % suppress output to command window

% --------------------------------------------------------- set up screen variables --------------------------------------------------------- %

param.mon_width  	= 31.4; % monitor width = macbook screen 31.4 
param.v_dist 		= 30;   % distance - make sure you seat your subject 30~40 cm away 

Screen('Preference', 'SkipSyncTests', 2);

ScreenNum = max(Screen('Screens'));
% [wPtr, rect] = PsychImaging('OpenWindow',ScreenNum,[128, 128, 128],[0 0 800 600],32,2,[],[],kPsychNeed32BPCFloat);
[wPtr, rect] = Screen('OpenWindow', ScreenNum, [128, 128, 128], []);        % open the screen
wOff         = Screen(wPtr, 'OpenOffscreenWindow', [128, 128, 128], []);    % Offscreen buffers


center = [rect(3) rect(4)]/2;                                               % center of screen (pixel coordinates), has x and y value
centerLocx=center(1);                                                       % x coordinate of the center of the screen
centerLocy=center(2);                                                       % y coordinate of the center of the screen

pix_per_deg = pi * rect(3) / atan(param.mon_width/param.v_dist/2) / 360;            % pixels per degree
lineThick = 0.1 * pix_per_deg;
Screen('TextSize',wPtr,20);
QuestionLoc = centerLocy - 6 * pix_per_deg;

% draw vertical line
verLength = 2;
verY_1 = centerLocy - 0.5 * verLength * pix_per_deg; 
verY_2 = centerLocy + 0.5 * verLength * pix_per_deg; 

% mask presentation 
Scene_imagesizeh = 640;                                                      % pixels of images- horizontal
Scene_imagesizev = 480;                                                      % pixels of images- vertical
Scene_Rect       = [0 0 Scene_imagesizeh Scene_imagesizev];

% read mask files
for p = 1:12
    Img = imread('Mask_BW.jpg');
    Img = cat(1, Img, Img);
    Img = cat(2, Img, Img);
    MaskText(p) = Screen('MakeTexture', wPtr, double(Img));
end

Img_smile = imread('smiley2.jpg');
SmileTexture = Screen('MakeTexture', wPtr, Img_smile);

pressed = 0;

% ------- delay period (1.5 sec) ------ %

% smiley face for fixation
Screen('DrawTexture', wPtr, SmileTexture);
txt = 'Measure the size of Smiley face - diameter should roughly be 1.8cm. Press any key to move on.';
bounds = TextBounds(wOff, txt);
txtsize = (bounds(3)-bounds(1))/2;
Screen('DrawText',wPtr,txt, centerLocx - txtsize*0.8, QuestionLoc, [0 0 0]);

Screen('Flip', wPtr);
keyisdown=0;
[keyisdown, secs, keyCode] = KbCheck(DevId);
while ~keyisdown
    [keyisdown, secs, keyCode] = KbCheck(DevId);
end
WaitSecs(1);

% ------- stimulus presentation ------ %
lineLength = 20;
verLocation = centerLocx + 1 * pix_per_deg;
lineX_1 = centerLocx - 0.5 * lineLength * pix_per_deg; 
lineX_2 = centerLocx + 0.5 * lineLength * pix_per_deg; 

Screen('DrawLine', wPtr,  [0 0 0], lineX_1, centerLocy, lineX_2, centerLocy, lineThick);
Screen('DrawLine', wPtr,  [0 0 0], verLocation, verY_1, verLocation, verY_2, lineThick);

txt = 'Horizontal line = 10.5cm; Vertical line = 1cm. Press any key to move on.';
bounds = TextBounds(wOff, txt);
txtsize = (bounds(3)-bounds(1))/2;
Screen('DrawText',wPtr,txt, centerLocx - txtsize*0.8, QuestionLoc, [0 0 0]);


Screen('Flip', wPtr);
keyisdown=0;
[keyisdown, secs, keyCode] = KbCheck(DevId);
while ~keyisdown
    [keyisdown, secs, keyCode] = KbCheck(DevId);
end
WaitSecs(1);

% ------- mask presentation ------ %

Screen('DrawTexture', wPtr, MaskText(1), Scene_Rect);  

txt = 'Width = 14.3cm; Height = 10.8cm (or bigger than this). Press any key to move on.';
bounds = TextBounds(wOff, txt);
txtsize = (bounds(3)-bounds(1))/2;
Screen('DrawText',wPtr,txt, centerLocx - txtsize*0.8, QuestionLoc, [0 0 0]);
Screen('Flip', wPtr);

keyisdown=0;
[keyisdown, secs, keyCode] = KbCheck(DevId);
while ~keyisdown
    [keyisdown, secs, keyCode] = KbCheck(DevId);
end

ShowCursor;
Screen('CloseAll');
ListenChar(0);


