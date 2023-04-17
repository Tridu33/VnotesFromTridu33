function output = fact(n) 
if n == 1
 output = 1; 
return; 
end 
output = n*fact(n-1);