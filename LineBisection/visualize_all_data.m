%visualize_data for all linebisection data files in the log folder

logFolder = 'C:\Users\andlab.AS-LF315-1\Documents\Experiments\LineBisection\log';

entries = dir(logFolder);

for i = 1:length(entries)
    entry = entries(i);

    sub_id = entry.name;
    
    try 
        fprintf('Processing subject %d...\n', sub_id);
        visualize_data(sub_id);
    catch ME
        warning('Error processing subject %d: %s', sub_id, ME.message);
    end
end
    
 

