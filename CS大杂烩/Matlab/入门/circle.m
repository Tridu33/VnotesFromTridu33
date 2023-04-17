function sa = circle(r,s)
%CIRCLE		plot a circle of radii r in the line specified by s.
%	r			ָ���뾶����ֵ
%	s			ָ����ɫ���ַ���
%	sa			Բ���
%
% circle(r)			������ʵ�߻��뾶Ϊ r ��Բ����.
% circle(r,s)			���ô� s ָ������ɫ���뾶Ϊ r ��Բ����.
% sa=circle(r)		����Բ����������뾶Ϊ r ����ɫԲ��.
% sa=circle(r,s)		����Բ����������뾶Ϊ r �� s ɫԲ��.
if nargin>2
   error('��������̫�ࡣ');
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
