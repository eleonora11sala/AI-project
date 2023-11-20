clear all
close all
clc 
%%
path= 'C:\Users\user\Desktop\AI-project\train\';

ppg=load(fullfile(path,"S001_128.mat"))
ppg=ppg.ppg;

spk=load(fullfile(path,"S001_128_spk.mat"))
spk=spk.speaks;

lab=load(fullfile(path,"S001_128_ann.mat"))
lab=lab.labels;

csvwrite('test.csv',transpose(ppg[:,0:1000]))

%% Visualization

fs=128;

t=linspace(0,1/fs,length(ppg));

figure(), 
subplot(1,3,1), plot(t,ppg);
title('All recording')
subplot(1,3,2), plot(t(:,1:60*128),ppg(1:60*128,:));
title('First 60 sec')
subplot(1,3,3), plot(t(:,1:30*128),ppg(1:30*128,:));
title('First 30 sec')

%% Preprocessing

[b,a]=butter(2,[0.5,8]/(fs/2),'bandpass');
filtsig=filter(b,a,ppg);

figure(), 
plot(t(:,1:30*128),ppg(1:30*128,:));
hold on
plot(t(:,1:30*128),filtsig(1:30*128,:));

sig = filtsig(spk,1)

filtsig=detrend(filtsig);
figure(), 
plot(t(:,1:30*128),ppg(1:30*128,:));
hold on
plot(t(:,1:30*128),filtsig(1:30*128,:));
hold on
plot(t(spk(1:30,1)),sig(1:30,:),'*')



