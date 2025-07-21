% visualize_data

function [] = visualize_data(subj)

    % find number of blocks
    
    file_pattern = sprintf('%slinebisection_block*_results.mat', subj);

    files = dir(fullfile(pwd, 'log', subj, file_pattern));

    nBlocks = numel(files);
    % nBlocks = 4;
    
    % Initialize temp cell arrays
    StimDuration_all = cell(nBlocks, 1);
    Types_all = cell(nBlocks, 1);
    VerLocations_all = cell(nBlocks, 1);
    isCorrect_all = cell(nBlocks, 1);
    
    % Combine Data
    
    for b = 1:nBlocks
        block = extractvalues(subj, b);
        StimDuration_all{b} = block.stimdur;
        Types_all{b} = block.TypesT;
        VerLocations_all{b} = block.VerLocationsT;
        isCorrect_all{b} = block.isCorrect; 
    end
    
    StimDuration = vertcat(StimDuration_all{:});
    Types = vertcat(Types_all{:});
    VerLocations = vertcat(VerLocations_all{:});
    isCorrectAll = vertcat(isCorrect_all{:});

    %% Get Data ready for Sigmoid

    actual_locations = VerLocations;
    left_right = Types;
    actual_locations(left_right==1) = actual_locations(left_right==1) * -1;

    % Did they say left or right was correct?
    judged_left_right = zeros(length(isCorrectAll),1);
    for i = 1:length(isCorrectAll)
        if left_right(i) == 1
            judged_left_right(i) = ~isCorrectAll(i); %these will not be output--gets rid of the incorrect trials
        elseif left_right(i) == 2
            judged_left_right(i) = isCorrectAll(i);
        end
    end

    % Make x and y values to spit into the sigmoid function
    x_vals = -1.6:0.1:1.6;
    y_vals = nan(1,length(x_vals));
    binNums = nan(1,length(x_vals));
    numSeen = nan(1,length(x_vals));
    weights = nan(1,length(x_vals));
    y_plot = nan(1,length(x_vals));
    for i = 1:length(x_vals)
        if i == length(x_vals)
            this_x = actual_locations >= x_vals(i);
        else
            this_x = actual_locations >= x_vals(i) & ...
                actual_locations < x_vals(i+1);
        end
         numSeen(i) = sum(this_x);
         binNums(i) = sum(judged_left_right(this_x));
         y_vals(i) = binNums(i);
         weights(i) = numSeen(i);
         y_plot(i) = (binNums(i)/numSeen(i));
    end

    x_vals(numSeen==0) = [];
    y_vals(numSeen==0) = [];
    weights(numSeen==0) = [];
    y_plot(numSeen==0) = [];


    %% Fit sigmoid function
    targets = 0.5; % 50% performance

    [coeffs, stats, curve, threshold] = FitPsycheCurveLogit(x_vals, y_vals, weights, targets);

    SubjID = cellstr(subj);
    stimduration = mean(StimDuration);
    fit = stats.sfit;
    coef1 = coeffs(1);
    coef2 = coeffs(2);
    
    output = table(SubjID,stimduration, fit, coef1, coef2, threshold);

    writetable(output,[pwd, '\log\', subj, '\', subj, '_LineBisection_Data.csv'])

    %% Graph

    f = figure('visible','off');clf;

    scatter(x_vals,y_plot,200,'*', 'r');
    
    hold on
    x=[0 0];
    y=[0 1.05];
    line(x,y,'Color','magenta','LineStyle','--')
    ylim([0 1.05]);
    xlim([-1.6 1.6]);
    set(gca,'Xtick',-1.6:0.2:1.6)

    plot(curve(:,1),curve(:,2)./100,'k')
    hold on

    %Make box
    x1 = [-2.4 threshold];
    y1 = [.5 .5];
    plot(x1, y1, 'b');
    hold on
    x2 = [threshold threshold];
    y2 = [.5 0];
    plot(x2, y2, 'b');

    
    set(gca, 'FontSize', 20)

    if threshold < 0
        title([subj ' Leftward Bias = ' num2str(threshold)])
    elseif threshold > 0
        title([subj ' Rightward Bias = ' num2str(threshold)])
    end
    
    saveas(f,[pwd, '\log\', subj, '\', subj, '_LineBisection_Figure.jpg']);

