
%%%%%%%%%%%%% MAIN SCRIPT TO BE CALLED FOR EACH NEW USER %%%%%%%%%%%%%%%%%

% Clear the workspace and the screen, start from a fresh interpreter
sca;
clear all; 
close all;

addpath(strcat(pwd,filesep,'scripts'))

%% Experimenter input

% --------------------
%       SUBID
% --------------------
inputCheck = 0;
while inputCheck == 0
    SubID = input('Please enter SubID: ', 's');
    if ~isempty(SubID)
        inputCheck = 1;
    end
end

% --------------------------------------------------------------------------------
%                        COUNTERBALANCE TABLE
%	CB number	% Feature Order     % Search Order          % Motion Order
%	1           LUMINANCE, COLOR    FEATURE, CONJUNCTION    STATIC, DYNAMIC
%   2           LUMINANCE, COLOR    CONJUNCTION, FEATURE    STATIC, DYNAMIC
%	3           LUMINANCE, COLOR    FEATURE, CONJUNCTION    DYNAMIC, STATIC
%   4           LUMINANCE, COLOR    CONJUNCTION, FEATURE    DYNAMIC, STATIC
%   5           COLOR, LUMINANCE    FEATURE, CONJUNCTION    STATIC, DYNAMIC
%   6           COLOR, LUMINANCE    CONJUNCTION, FEATURE    STATIC, DYNAMIC
%   7           COLOR, LUMINANCE    FEATURE, CONJUNCTION    DYNAMIC, STATIC
%   8           COLOR, LUMINANCE    CONJUNCTION, FEATURE    DYNAMIC, STATIC
%
% --------------------------------------------------------------------------------
inputCheck = 0;
while inputCheck == 0
    CB = input('Please enter COUNTERBALANCE number: ', 's');
    if ~isempty(CB)
        inputCheck = 1;
    end
end

% Set up parameters and screen
[window, outputDirectory] = SETUP(SubID);

%% ASSIGN COUNTERBALANCE
switch CB  
    case '1'
    %	1           LUMINANCE, COLOR    FEATURE, CONJUNCTION    STATIC, DYNAMIC
        FeatureCB = '1';
        FirstFeature = 'luminance';
        SecondFeature = 'color';

        SearchCB = '1';
        FirstSearch = 'feature';
        SecondSearch = 'conjunction';

        MotionCB = '1';
        FirstMotion = 'static';
        SecondMotion = 'dynamic';

    case '2'
    %   2           LUMINANCE, COLOR    CONJUNCTION, FEATURE    STATIC, DYNAMIC
        FeatureCB = '1';
        FirstFeature = 'luminance';
        SecondFeature = 'color';

        SearchCB = '2';
        FirstSearch = 'conjunction';
        SecondSearch = 'feature';

        MotionCB = '1';
        FirstMotion = 'static';
        SecondMotion = 'dynamic';
    
    case '3'
    %	3           LUMINANCE, COLOR    FEATURE, CONJUNCTION    DYNAMIC, STATIC
        FeatureCB = '1';
        FirstFeature = 'luminance';
        SecondFeature = 'color';

        SearchCB = '1';
        FirstSearch = 'feature';
        SecondSearch = 'conjunction';

        MotionCB = '2';
        FirstMotion = 'dynamic';
        SecondMotion = 'static';

    case '4'
    %   4           LUMINANCE, COLOR    CONJUNCTION, FEATURE    DYNAMIC, STATIC
        FeatureCB = '1';
        FirstFeature = 'luminance';
        SecondFeature = 'color';

        SearchCB = '2';
        FirstSearch = 'conjunction';
        SecondSearch = 'feature';

        MotionCB = '2';
        FirstMotion = 'dynamic';
        SecondMotion = 'static';

    case '5'
    %   5           COLOR, LUMINANCE    FEATURE, CONJUNCTION    STATIC, DYNAMIC
        FeatureCB = '2';
        FirstFeature = 'color';
        SecondFeature = 'luminance';

        SearchCB = '1';
        FirstSearch = 'feature';
        SecondSearch = 'conjunction';

        MotionCB = '1';
        FirstMotion = 'static';
        SecondMotion = 'dynamic';

    case '6'
    %   6           COLOR, LUMINANCE    CONJUNCTION, FEATURE    STATIC, DYNAMIC
        FeatureCB = '2';
        FirstFeature = 'color';
        SecondFeature = 'luminance';

        SearchCB = '2';
        FirstSearch = 'conjunction';
        SecondSearch = 'feature';

        MotionCB = '1';
        FirstMotion = 'static';
        SecondMotion = 'dynamic';

    case '7'
    %   7           COLOR, LUMINANCE    FEATURE, CONJUNCTION    DYNAMIC, STATIC
        FeatureCB = '2';
        FirstFeature = 'color';
        SecondFeature = 'luminance';

        SearchCB = '1';
        FirstSearch = 'feature';
        SecondSearch = 'conjunction';

        MotionCB = '2';
        FirstMotion = 'dynamic';
        SecondMotion = 'static';

    case '8'
    %   8           COLOR, LUMINANCE    CONJUNCTION, FEATURE    DYNAMIC, STATIC
        FeatureCB = '2';
        FirstFeature = 'color';
        SecondFeature = 'luminance';

        SearchCB = '2';
        FirstSearch = 'conjunction';
        SecondSearch = 'feature';

        MotionCB = '2';
        FirstMotion = 'dynamic';
        SecondMotion = 'static';

    otherwise
        error(['ERROR: Invalid Counterbalance specification.', ...
            '\n 	CB number	% Feature Order     % Search Order          % Motion Order', ...
            '\n     1           LUMINANCE, COLOR    FEATURE, CONJUNCTION    STATIC, DYNAMIC', ...
            '\n     2           LUMINANCE, COLOR    CONJUNCTION, FEATURE    STATIC, DYNAMIC', ...
            '\n 	3           LUMINANCE, COLOR    FEATURE, CONJUNCTION    DYNAMIC, STATIC', ...
            '\n     4           LUMINANCE, COLOR    CONJUNCTION, FEATURE    DYNAMIC, STATIC', ...
            '\n     5           COLOR, LUMINANCE    FEATURE, CONJUNCTION    STATIC, DYNAMIC', ...
            '\n     6           COLOR, LUMINANCE    CONJUNCTION, FEATURE    STATIC, DYNAMIC', ...
            '\n     7           COLOR, LUMINANCE    FEATURE, CONJUNCTION    DYNAMIC, STATIC', ...
            '\n     8           COLOR, LUMINANCE    CONJUNCTION, FEATURE    DYNAMIC, STATIC'], ...
            class(length('ERROR: Invalid Counterbalance specification.')))

end

%% RUN TASK

% FirstSearch, FirstFeature
connectEyetracker(SubID)
[window] = calibrateEyetracker(window);
window = INTRO(window,FirstSearch,FirstFeature);        
window = EXPERIMENT(window, SubID, CB, MotionCB, FirstSearch,FirstFeature,outputDirectory);
window = disconnectEyetracker(SubID,FirstSearch,FirstFeature, window);

% SecondSearch, FirstFeature
connectEyetracker(SubID)
[window] = calibrateEyetracker(window);
window = INTRO(window,SecondSearch,FirstFeature);        
window = EXPERIMENT(window, SubID, CB, MotionCB, SecondSearch,FirstFeature,outputDirectory);
window = disconnectEyetracker(SubID,SecondSearch,FirstFeature, window);

% FirstSearch, SecondFeature
connectEyetracker(SubID)
[window] = calibrateEyetracker(window);
window = INTRO(window,FirstSearch,SecondFeature);        
window = EXPERIMENT(window, SubID, CB, MotionCB, FirstSearch,SecondFeature,outputDirectory);
window = disconnectEyetracker(SubID,FirstSearch,SecondFeature, window);

% SecondSearch, SecondFeature
connectEyetracker(SubID)
[window] = calibrateEyetracker(window);
window = INTRO(window,SecondSearch,SecondFeature);  
window = EXPERIMENT(window, SubID, CB, MotionCB, SecondSearch,SecondFeature, outputDirectory);
window = disconnectEyetracker(SubID,SecondSearch,SecondFeature,window);

DONE(window);