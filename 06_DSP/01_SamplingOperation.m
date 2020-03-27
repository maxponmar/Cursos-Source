
%Original Signal
t=0:1/1000:2;
F=4;
x_t=sin(2*pi*F*t);

% Sampling signal
Ts=1/64;
ts=0:Ts:2;
x_n =sin(2*pi*F*ts);

n=ts/Ts;

%plot(t,x_t);
%hold on;
stem(n,x_n,'filled');

%xlabel('t');
%ylabel('sin(8\pi t)');
%title('sin(8\pi t)');