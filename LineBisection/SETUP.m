function [window, windowOff, rect] = SETUP()

Screen('Preference', 'SkipSyncTests', 2);
ScreenNum = max(Screen('Screens'));
[window, rect] = Screen('OpenWindow', ScreenNum, [128, 128, 128], []);        % open the screen
windowOff = Screen(window, 'OpenOffscreenWindow', [128, 128, 128], []);    % Offscreen buffers