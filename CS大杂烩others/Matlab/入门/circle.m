function sa = circle(r,s)
%CIRCLE		plot a circle of radii r in the line specified by s.
%	r			指定半径的数值
%	s			指定线色的字符串
%	sa			圆面积
%
% circle(r)			利用蓝实线画半径为 r 的圆周线.
% circle(r,s)			利用串 s 指定的线色画半径为 r 的圆周线.
% sa=circle(r)		计算圆面积，并画半径为 r 的蓝色圆面.
% sa=circle(r,s)		计算圆面积，并画半径为 r 的 s 色圆面.
if nargin>2
   error('输入宗量太多。');
end;
if nargin==1
   s='b';
end;
clf;
t=0:pi/100:2*pi;
x=r*exp(i*t);
if nargout==0
   plot(x,s);
else
   sa=pi*r*r;
   fill(real(x),imag(x),s)
end
axis('square')
