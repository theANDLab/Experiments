% linebisection_short.m 

subj              = input('SubjID: ','s');
% age               = input('age: ');
% gender            = input('gender: ', 's');
% hand              = input('hand: ', 's');


% practice1(subj, 1, 2, age, gender, hand);   %first practice session--unlimited time to answer
% practice2a(subj, 1, 1);   %second practice session--phase a--the line flashes and then the subject responds 
% practice2b(subj, 1, 1);    %second practice session--phase b--the line flashes for slightly less time
% practice3(subj, 1, 1);    %third practice session--the line is covered by a mask and the subject responds in the presence of the mask

% Four blocks of 20 lines 
linebisection(subj, 1, 1);
% linebisection(subj, 2, 1);
% linebisection(subj, 3, 1);
% linebisection(subj, 4, 1);


% visualize_data(subj);