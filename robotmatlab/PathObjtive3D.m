function [f,crossOb]=PathObjtive(x,ploton)

if (nargin == 1)
   ploton=0; 
end

xMin=0; xMax=38;
yMin=7; yMax=91;
zMin=4; zMax=157;

xInit=xMin; yInit=yMin; zInit=zMin; %initial point for planner
xGoal=xMax; yGoal=yMax;  zGoal=zMax; %goal for planner


pObstacles =[  10.7669   77.6749  139.8150
   22.1727   39.5241   52.0252
   31.5296   51.7466  140.3754
   24.1503   84.9911   89.9872
   30.3343   44.3949  110.2274];

xOb=pObstacles(:,1); 
 
yOb=pObstacles(:,2);
 
zOb=pObstacles(:,3);


xall=linspace(xMin+1,xMax-1,100);
yall=linspace(yMin+1,yMax-1,100);
zall=linspace(zMin+1,zMax-1,100);

a=ones(length(x),1);
b=100*ones(length(x),1);


x0=a+(b-a).*x;
x0=round(x0);
xp=xall(x0(1:5));
yp=yall(x0(6:10));
zp=zall(x0(11:15));


[xp,nsort]=sort(xp);
yp=yp(nsort);
zp=zp(nsort);


xp=[xInit xp xGoal];
yp=[yInit yp yGoal];
zp=[zInit zp zGoal];

gcheck=0;
for i=1:length(xp)-1
    Ab=[xp(i+1);yp(i+1);zp(i+1)]-[xp(i);yp(i);zp(i)];
    for ii=1:length(xOb)
        Ac=[xOb(ii);yOb(ii);zOb(ii)]-[xp(i);yp(i);zp(i)];
        crossOb =cross(Ab,Ac); 
        if norm(crossOb)<10
            f=1e5;
            gcheck=1;
            break
        else
        end
    end
    distOb(i) = sqrt((xp(i+1)-xp(i))^2 + (yp(i+1)-yp(i))^2+ (zp(i+1)-zp(i))^2);
end
if gcheck==0
    f=sum(distOb);
end
    

 if ploton~=0
    figure(1),clf, hold on
    plot3(xMin, yMin, zMin, 'ko', 'MarkerSize',10, 'MarkerFaceColor','k');
    plot3(xMax, yMax, zMax, 'go', 'MarkerSize',10, 'MarkerFaceColor','g');
    plot3(xOb,  yOb, zOb, 'bo', 'MarkerSize',20, 'MarkerFaceColor','k');

    for i=1:length(xp)-1
         plot3([xp(i) xp(i+1)], [yp(i) yp(i+1)],[zp(i) zp(i+1)], 'b', 'Linewidth', 3);
    end
    view(30,60)
    hold off
    
end