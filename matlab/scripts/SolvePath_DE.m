function DE
% Differential evolution DE/best/2/bin
% by Sujin Bureerat
% fun = m-file for objective function
% foutput = mat-flie for output results
% nloop = no. of generations
% nsol = population size
% nvar = no. of design variables
% nbit = no. of binary bits for each design 
% variable (in cases of the method using binary strings)
% a = vector of lower limits
% b = vector of upper limits

fun='PathObjtive3D';%objective function name 
nloop=30;
nsol=30;
nvar=15;


% obj=VideoWriter('DEpathanimate.avi');
% obj.Quality=100;
% obj.FrameRate=20;
% open(obj)



a=zeros(nvar,1);
b=ones(nvar,1); 
% predefined parameters
pc=0.7;% crossover probability
F=0.5;% Scaling factor for differentail evolution (DE) operator
CR=0.8;% probability of chosing element from offspring in crossover

rand('state',sum(100*clock));

[x0,f0] = de_initial(fun,nvar,nsol,a,b);

iter=0;neval=0;
while iter < nloop
    iter=iter+1;
    % DE mutation, crossover & selection
    [x1,f1]=de_reproduct(fun,x0,f0,a,b,pc,F,CR);
    neval=neval+length(f1);       
    f0=f1;x0=x1;
    [ffmin,nmin]=min(f0);
    xbest=x0(:,nmin);
%     feval(fun,xbest,1);
%     pic=getframe(gcf);
%     writeVideo(obj,pic)
    pause(1)
end
[f,crossOb]=feval(fun,xbest,1);
disp(['Totla distance = ' num2str(f)])
%%%%%%%%%% Sub-programs %%%%%%%%%%%%%%
function [x,f] = de_initial(fun,nvar,nsol,a,b)
%
% Randomly initiate the population, design variables 
% nvar=no. of variables
% nsol is a number of individuals
% 
x = rand(nvar,nsol);
for i=1:nsol
    x(:,i)=a+(b-a).*x(:,i);
    f(i)=feval(fun,x(:,i));
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [x1,f1] = de_reproduct(fun,x0,f0,a,b,pc,F,CR)
% best/2/bin strategy
[m0,n0]=size(x0);
[fbest,nmin]=min(f0);
xbest=x0(:,nmin);
% DE point generation for n1 parents (x1)
% x0 = population from the previous generation
% f0 = corresponding objective values

for i=1:n0
    nr=randperm(n0);
    i1=nr(1);i2=nr(2);i3=nr(3);i4=nr(4);
    xr1=x0(:,i1);% Randomly seletced individual 1
    xr2=x0(:,i2);% Randomly seletced individual 2
    xr3=x0(:,i3);% Randomly seletced individual 3
    xr4=x0(:,i4);% Randomly seletced individual 4

    F=0.6+rand*0.3;
    Ci=xbest+F*(xr1+xr2-xr3-xr4);
    % force Ci to its bounds
    for j=1:m0
        Ci(j)=max(min(Ci(j),b(j)),a(j));
    end
    
    if rand < pc
        for j=1:m0 % binomial crossover
            if rand < CR
                Vi(j,1)=Ci(j);
            else
                Vi(j,1)=x0(j,i);
            end
        end
        Ci=Vi;
    end
    xx0(:,i)=Ci;
end
for i=1:n0
    Ci=xx0(:,i);
    fCi=feval(fun,Ci,1);
    if fCi <= f0(i)
        x1(:,i)=Ci;
        f1(i)=fCi;
    else
        x1(:,i)=x0(:,i);
        f1(i)=f0(i);
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

