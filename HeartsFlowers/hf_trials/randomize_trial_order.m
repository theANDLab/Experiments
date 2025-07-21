trials = readtable("HF.csv");
q = 1;
rand_orders = cell(size(trials,1),1);
count_monitor = zeros(1,1);
Frep_monitor = zeros(1,1);
Irep_monitor = zeros(1,1);
Lrep_monitor = zeros(1,1);
Rrep_monitor = zeros(1,1);

for c = 1:q
    tic
    n = 0;
    z = 0;
    Frep = 5;
    Irep = 5;
    Lrep = 5;
    Rrep = 5;
    count = 0;

    while (double(z==1) + double(n==16) + ...
            double(Frep<5) + double(Lrep<5)) ~=4
        % randomly shuffle trial order
        trials = trials(randperm(size(trials,1)),:);
        trials.pairs = cell(size(trials,1),1);
    
        % Label trial pairs (N+1)
        for i = 1:size(trials,1)-1
        
            trials.pairs(i+1) = cellstr([num2str(cell2mat(trials.Cond(i))) '_' ...
                                num2str(cell2mat(trials.Cond(i+1))) '_' ...
                                num2str(cell2mat(trials.Resp(i))) '_' ...
                                num2str(cell2mat(trials.Resp(i+1)))]);
        end
    
        % find the unique trial pair types
        [C, ia, ic] = unique(trials.pairs(2:end));
        
        % count the number of unique trial pairs
        n = length(C);
    
        % count the number of times each trial pair occurs
        a_counts = accumarray(ic,1);
    
        % check to see if the number of trial pair occurances is equal
        z = length(unique(a_counts));

        dF = [true; diff(double(strcmp(trials.Cond, 'F'))) ~= 0; true];
        fF = diff(find(dF));
        YF = repelem(fF, fF);
        Frep = max(YF);
        
        % dI = [true; diff(double(strcmp(trials.Cond, 'I'))) ~= 0; true];
        % fI = diff(find(dI));
        % YI = repelem(fI, fI);
        % Irep = max(YI);

        dL = [true; diff(double(strcmp(trials.Resp, 'L'))) ~= 0; true];
        fL = diff(find(dL));
        YL = repelem(fL, fL);
        Lrep = max(YL);

        % dR = [true; diff(double(strcmp(trials.Resp, 'R'))) ~= 0; true];
        % fR = diff(find(dR));
        % YR = repelem(fR, fR);
        % Rrep = max(YR);

        count = count + 1;
            
    end % z

    rand_orders(:,c) = trials.pairs;
    count_monitor(c) = count;
    Frep_monitor(c) = Frep;
    Irep_monitor(c) = Irep;
    Lrep_monitor(c) = Lrep;
    Rrep_monitor(c) = Rrep;
    
end % c
toc

writetable(trials,"forpython.csv")

% cond_odd = trials.Cond(1:2:end);
% cond_even = trials.Cond(2:2:end);
% 
% cond_trans = [cond_odd(1:end-1) cond_even];
% 
% resp_odd = trials.Resp(1:2:end);
% resp_even = trials.Resp(2:2:end);
% 
% resp_trans = [resp_odd(1:end-1) resp_even];

