close all;
clear all;
clc;
v=6;b=10;r=5;
A=zeros(v,b);

for i=1:v
    for j=1:b
        lambda=1;flag=1;sum_row=0;sum_col=0;
        
        for k=1:j  
        sum_row=sum_row+A(i,k);
        end
        
        for h=1:i   
        sum_col=sum_col+A(h,j);
        end
        
        if(i>1&&(sum_row!=2))
       %have a try A(i,j)=1;    
            for m=1:(i-1)s
                lambda=sum(A(m,:).*A(i,:));
                if lambda==2
                    flag=0;
                else
                   flag=1;
                end
            end
        end
        
%         if((sum_row<=5)&&(sum_col<3)&&flag)
%             A(i,j)=1
%         end
%         
    end
end
















