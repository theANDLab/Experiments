function T = extractvalues(subj, block)
% Pulling out data for each block 

    
    load(fullfile(pwd, 'log', subj, [ subj 'linebisection_block' num2str(block) '_results.mat']))
    
    stimdur = repmat(exp.StimDuration,20,1);
    
    % Make Trial Number
    trialnum = (1:20);
    trialnumT = trialnum.';

    % Transpose Variables into 20x1
    LengthsT = exp.Lengths.';
    TypesT = exp.Types.';
    CorrAnsT = exp.CorrAns.';

    % Get rid of last row in VerLocations
    VerLocationsT = VerLocations(1:20);

    % Make one table
    T = table(stimdur, trialnumT, response, TypesT, CorrAnsT, isCorrect, LengthsT, RT, VerLocationsT);


