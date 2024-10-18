function EMGfilt = filterEMG(EMGraw, sampleRate, highPassCutOff, lowPassCutOff)
% This function will filter EMG according to prepare for synergy
% extraction:
%    (1) High pass filter (usually 35 Hz)
%    (2) Demean
%    (3) Rectify (full wave rectify to flip negative values over the axis)
%    (4) Low pass filter (usually 10 Hz)
%
% Inputs: 
%   - EMG - raw EMG matrix
%   - sampleRate - analog sample rate for calculating Nyquist frequency
%   - highPassCutOff - cut off for high pass filter (Hz)
%   - lowPassCutOff - cut off for low pass filter (Hz)
%
% Outputs: EMGfilt - filtered EMG matrix
%
% Created: 10/26/2021 HDC
% Modified:

% calculate Nyquist frequency for filters
nyquistFreq = sampleRate/2;

%--- Create Filters ---
% High pass filter 
[filt_high_B,filt_high_A] = butter(3,highPassCutOff/nyquistFreq,'high');
% Low pass filter at 10 Hz
[filt_low_B,filt_low_A] = butter(3,lowPassCutOff/nyquistFreq,'low');

%--- Filter EMG signals ---
% High pass filter
emg = filtfilt(filt_high_B, filt_high_A,EMGraw);
% Demean and rectify
emg_mean = repmat(mean(emg(1:sampleRate,:),1),size(emg,1),1);
emg = abs(emg-emg_mean);
% Low pass filter at 10 Hz
EMGfilt = filtfilt(filt_low_B, filt_low_A,emg);

end
