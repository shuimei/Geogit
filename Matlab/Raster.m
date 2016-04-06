figure;

I=geotiffread('three_Huabei20140110_t175247.tif');
s=size(I);
B=I(:);
t=min(B):(max(B)-min(B))/10:max(B);
hist_B=hist(B,t);
subplot(121);
histogram(B);

J=geotiffread('three_Huabei20140102_t184143.tif');
r=size(J);
Q=J(:);
subplot(122);
histogram(Q);

