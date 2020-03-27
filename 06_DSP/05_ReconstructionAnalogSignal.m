close all; clear all; clc;

t=0:1/1000:2;
F=4;
x_t=sin(2*pi*F*t); %original signal

Ts=1/2000;
ts=0:Ts:2;
x_n_vec=sin(2*pi*F*ts); %sampled signal (digital)
n_vec=ts/Ts;

x_r_t=zeros(1,length(t));
for n_indx=1:length(n_vec)
xn =x_n_vec(1,n_indx);
n=n_vec(1,n_indx);
temp= xn *sinc((t- n *Ts)/Ts);
x_r_t= x_r_t+ temp;
end

plot(t,x_r_t,'r+:'); %reconstructed signal
hold on
plot(t,x_t,'k-');
xlabel('t');
legend('Reconstructed signal', 'Original signal');
