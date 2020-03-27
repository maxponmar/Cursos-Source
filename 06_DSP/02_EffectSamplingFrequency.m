
close all; clear all; clc;
% Generate the sine signal
t=0:1/1000:2;
F=4;
x_t=sin(2*pi*F*t);

% Perform the sampling operation
Ts=1/512;
ts=0:Ts:2;
x_n=sin(2*pi*F*ts);

% Plot continuous sine signal, and show the taken samples on the same
% signal
plot(t,x_t);
hold on;
stem(ts,x_n,'r-.','filled');
xlabel('t');
ylabel('cos(2\pi4t)');

% Plot the digital signal wrt its index values
figure;
n=ts/Ts;
stem(n,x_n,'b-.','filled');
xlabel('n');
ylabel('x[n]');