function [window] = displayBlank(window,bgcolor)
%% Display blank screen.
Screen('FillRect', window, bgcolor);
Screen('Flip', window);


