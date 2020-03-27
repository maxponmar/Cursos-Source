t=0:0.001:20;
f=2;
xct=coss(2*pi*f*t);
%plot(t,xct)
%xlabel('t (sec)')
%ylabel('cos(4\pit)')
%title('Cosine Signal')
w=linspace(-8*pi,8*pi,length(t));
for i=1:length(w)
xcw(i)=trapz(t,xct.*exp(-j*w(i).*t));
end
figure
plot(w,abs(xcw))
xlabel('\omega')
ylabel('F(cos(4\pit))')
title('Fourier transform of cosine signal')