function [window, windowOff] = BREAK(window, windowOff,rect)

KbName('UnifyKeyNames');
spaceKey = KbName('Space');
escKey = KbName('ESCAPE'); %

p.mon_width  	= 53.28; % monitor width = EIZO 53.28  
p.v_dist 		= 60;   % distance - make sure you seat your subject 30~40 cm away 

center = [rect(3) rect(4)]/2;                                               % center of screen (pixel coordinates), has x and y value
centerLocx=center(1);                                                       % x coordinate of the center of the screen
centerLocy=center(2);                                                       % y coordinate of the center of the screen

pix_per_deg = pi * rect(3) / atan(p.mon_width/p.v_dist/2) / 360;            % pixels per degree
% QuestionLoc = centerLocy - 3 * pix_per_deg;

txtencourage = 'You are doing a great job! Keep it up!';
bounds = TextBounds(windowOff, txtencourage);
txtsize = (bounds(3)-bounds(1))/2;

Screen('DrawText',window,txtencourage, centerLocx - 1.73*txtsize, centerLocy, [0 0 0]);
Screen('Flip', window);

% wait for spaceKey to advance to next image
wait=true;
while wait
   [~, ~, keyCode, ~] = KbCheck; 

   if(keyCode(spaceKey)); wait=false; end
    
   if(keyCode(escKey)), break; end

end % while wait

WaitSecs(1);
