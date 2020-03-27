clc;clear all;close all;

t=0:1/100:2;
f=2;
Ts=1/16;
ts=0:Ts:2;
n=ts./Ts;
xct=cos(2*pi*f*t);
xn=cos(2*pi*f*ts);

figure(1)
subplot(2,1,1)
plot(t,xct)
xlabel('t(sec)')
ylabel('cos(4\pi t)')
title('Cos signal')

subplot(2,1,2)
stem(n,xn,'r-.','filled')
xlabel('n(integer)')
ylabel('cos(4\pi n Ts)')
title('Sampled Cos signal')

w=linspace(-8*pi,8*pi,length(t));
for i=1:length(w)
xcw(i)=trapz(t,xct.*exp(-j*w(i).*t));
xnw(i)=sum(xn.*exp(-j.*w(i)*n));
end
figure(2)
subplot(2,1,1)
plot(w,abs(xcw))
xlabel('\omega (radian)')
ylabel('F(cos(4\pit))')
title('Fourier transform of cosine signal')
subplot(2,1,2)
plot(w,abs(xnw))
xlabel('\omega (radian)')
ylabel('F(cos(4\pi n Ts))')
title('Fourier transform of digital cosine signal')