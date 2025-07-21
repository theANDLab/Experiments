%%Line Bisection  

subj              = input('SubjID: ','s');
% age               = input('age: ');
% gender            = input('gender: ', 's');
% hand              = input('hand: ', 's') ;
[window, windowoff, rect] = SETUP; 

% Three practice levels, short 

% Fixation, Stimulus until response, No Mask, Feedback
[window, windowoff] = practice1(subj, 1, 1, window, windowoff, rect); %first practice session--unlimited time to answer
[window,windowoff] = BREAK(window, windowoff, rect);

% Fixation, 1000ms Stimulus, No Mask, Feedback
[window, windowoff] = practice2b(subj, 1, 1, window, windowoff, rect); %second practice session--phase b--the line flashes for slightly less time
[window,windowoff] = BREAK(window, windowoff, rect);

% Fixation, 200ms Stimulus, Mask (SAME AS EXPERIMENT, But with Feedback)
[window,windowoff,NumCorrectTrials] = practice3(subj, 1, 1, window, windowoff, rect, 0.2); %third practice session--the line is covered by a mask and the subject responds in the presence of the mask
[window,windowoff] = BREAK(window, windowoff, rect);

% If accuracy is <=50% then increase the stimulus duration to 600ms
if sum(NumCorrectTrials) / length(NumCorrectTrials) * 100 <= 50
    [window,windowoff,NumCorrectTrials] = practice3(subj, 1, 1, window, windowoff, rect, 0.6); %third practice session--the line is covered by a mask and the subject responds in the presence of the mask
    [window,windowoff] = BREAK(window, windowoff, rect);

    % If accuracy is <=50% again, then end experiment
    if sum(NumCorrectTrials) / length(NumCorrectTrials) * 100 <= 50 
        [window,windowoff] = DONE(window, windowoff, rect);
        error("Failed Practice Round")

    else

        % % Four blocks of 20 lines, short, StimDur = 600ms
        [window,windowoff] = linebisection(subj, 1, 1, window, windowoff, rect, 0.6);
        [window,windowoff] = BREAK(window, windowoff, rect);
        [window,windowoff] = linebisection(subj, 2, 1, window, windowoff, rect, 0.6);
        [window,windowoff] = BREAK(window, windowoff, rect);
        [window,windowoff] = linebisection(subj, 3, 1, window, windowoff, rect, 0.6);
        [window,windowoff] = BREAK(window, windowoff, rect);
        [window,windowoff] = linebisection(subj, 4, 1, window, windowoff, rect, 0.6);
        [window,windowoff] = DONE(window, windowoff, rect);
    end
else

    % % Four blocks of 20 lines, short, StimDur = 200ms 
    [window,windowoff] = linebisection(subj, 1, 1, window, windowoff, rect, 0.2);
    [window,windowoff] = BREAK(window, windowoff, rect);
    [window,windowoff] = linebisection(subj, 2, 1, window, windowoff, rect, 0.2);
    [window,windowoff] = BREAK(window, windowoff, rect);
    [window,windowoff] = linebisection(subj, 3, 1, window, windowoff, rect, 0.2);
    [window,windowoff] = BREAK(window, windowoff, rect);
    [window,windowoff] = linebisection(subj, 4, 1, window, windowoff, rect, 0.2);
    [window,windowoff] = DONE(window, windowoff, rect);

end

%visualize_data(subj);


