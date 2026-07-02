% % An example of rapidly-exploring random trees and path planning in 2-D
% % Ref: "Rapidly-Exploring Random Trees: A New Tool for Path Planning",
% % Steven M. LaValle, 1998
%~~~~
% Code can also be converted to function with input format
% [tree, path] = RRT(K, xMin, xMax, yMin, yMax, xInit, yInit, xGoal, yGoal, thresh)
% K is the number of iterations desired.
% xMin and xMax are the minimum and maximum values of x
% yMin and yMax are the minimum and maximum values of y
% xInit and yInit is the starting point of the algorithm
% xGoal and yGoal are the desired endpoints
% thresh is the allowed threshold distance between a random point the the
% goal point.
% Output is the tree structure containing X and Y vertices and the path
% found obtained from Init to Goal
%~~~~ 
% Written by: Omkar Halbe, Technical University of Munich, 31.10.2015
%~~~~ 
clear all; close all;
K=2000;
xMin=10; xMax=120;
yMin=1; yMax=73;
zMin=8; zMax=186;


pObstacles =[ 101.3393   48.9491   20.8392
   69.5211    7.0780   58.1964
   95.1998   53.8065  133.1433
   30.5401   58.9710  137.2822
   46.7674   12.6221  113.0750];

xOb=pObstacles(:,1); 
 
yOb=pObstacles(:,2);
 
zOb=pObstacles(:,3);
 
% obj=VideoWriter('rrtanimate','MPEG-4');
% obj.Quality=100;
% obj.FrameRate=20;
% open(obj)

xInit=xMin; yInit=yMin; zInit=zMin; %initial point for planner
xGoal=xMax; yGoal=yMax;  zGoal=zMax; %goal for planner


thresh=20;           %acceptable threshold for solution
tree.vertex(1).x = xInit;
tree.vertex(1).y = yInit;
tree.vertex(1).z = zInit;

tree.vertex(1).xPrev = xInit;
tree.vertex(1).yPrev = yInit;
tree.vertex(1).zPrev = zInit;

tree.vertex(1).dist=0;
tree.vertex(1).ind = 1; tree.vertex(1).indPrev = 0;
xArray=xInit; yArray = yInit; zArray = zInit;
figure(1); hold on; grid on;


plot3(xInit, yInit, zInit, 'ko', 'MarkerSize',10, 'MarkerFaceColor','k');
plot3(xGoal, yGoal, zGoal, 'go', 'MarkerSize',10, 'MarkerFaceColor','g');
plot3(xOb,  yOb, zOb, 'bs', 'MarkerSize',20, 'MarkerFaceColor','k');
% f=getframe(gcf);
% writeVideo(obj,f);
view(30,40)
for iter = 2:K
    
    distOb=zeros(1,length(xOb));
    
    while min(distOb)<5
        
        xRand = xMin+(xMax-xMin)*rand;
        yRand = yMin+(yMax-yMin)*rand;
        zRand = zMin+(zMax-zMin)*rand;
        for j = 1:length(distOb)
            distOb(j) = sqrt( (xRand-xOb(j))^2 + (yRand-yOb(j))^2+(zRand-zOb(j))^2);
        end
    end
    
    dist = Inf*ones(1,length(tree.vertex));
    
    for j = 1:length(tree.vertex)
        dist(j) = sqrt( (xRand-tree.vertex(j).x)^2 + (yRand-tree.vertex(j).y)^2 + (zRand-tree.vertex(j).z)^2);
    end
    [val, ind] = sort(dist);
    j=1;
    crossLine=1;
    while crossLine>1e-5
        crossOb=zeros(1,length(xOb));
        for jj = 1:length(xOb)
            Ab=[xRand;yRand;zRand]-[tree.vertex(ind(j)).x;tree.vertex(ind(j)).y;tree.vertex(ind(j)).z];
            Ac=[xRand;yRand;;zRand]-[xOb(jj);yOb(jj);zOb(jj)];
            crossOb = cross(Ac,Ab);
        end
        if norm(crossOb)>1
            crossLine=0;
        else
            j=j+1;
            if j>length(tree.vertex)
                while min(distOb)<5
                    
                    xRand = xMin+(xMax-xMin)*rand;
                    yRand = yMin+(yMax-yMin)*rand;
                    zRand = zMin+(zMax-zMin)*rand;
                    for j = 1:length(distOb)
                        distOb(j) = sqrt( (xRand-xOb(j))^2 + (yRand-yOb(j))^2+(zRand-zOb(j))^2);
                    end
                end
                
                dist = Inf*ones(1,length(tree.vertex));
                
                for j = 1:length(tree.vertex)
                    dist(j) = sqrt( (xRand-tree.vertex(j).x)^2 + (yRand-tree.vertex(j).y)^2 + (zRand-tree.vertex(j).z)^2);
                end
                [val, ind] = sort(dist);
                j=1;
            end
        end
    end
    tree.vertex(iter).x = xRand; tree.vertex(iter).y = yRand; tree.vertex(iter).z = zRand;
    tree.vertex(iter).dist = val(j);
    tree.vertex(iter).xPrev = tree.vertex(ind(j)).x;
    tree.vertex(iter).yPrev = tree.vertex(ind(j)).y;
    tree.vertex(iter).zPrev = tree.vertex(ind(j)).z;
    tree.vertex(iter).ind = iter;
    tree.vertex(iter).indPrev = ind(j);
    
    plot3([tree.vertex(iter).x; tree.vertex(ind(j)).x],[tree.vertex(iter).y; tree.vertex(ind(j)).y],[tree.vertex(iter).z; tree.vertex(ind(j)).z], 'r');
    plot3(tree.vertex(ind(j)).x,tree.vertex(ind(j)).y,tree.vertex(ind(j)).z, 'ok');
    text(tree.vertex(ind(j)).x,tree.vertex(ind(j)).y,tree.vertex(ind(j)).z, num2str(ind(j)))
    
    
    if sqrt( (xRand-xGoal)^2 + (yRand-yGoal)^2+ (zRand-zGoal)^2 ) <= thresh
       break
    end
    
%     f=getframe(gcf);
%     writeVideo(obj,f)
    pause(0);
end


if iter < K
    path.pos(1).x = xGoal; 
    path.pos(1).y = yGoal;
    path.pos(1).z = zGoal;
    path.pos(2).x = tree.vertex(end).x; 
    path.pos(2).y = tree.vertex(end).y; 
    path.pos(2).z = tree.vertex(end).z;    
    pathIndex = tree.vertex(end).indPrev;
    j=0;
    while 1
        path.pos(j+3).x = tree.vertex(pathIndex).x;
        path.pos(j+3).y = tree.vertex(pathIndex).y;
        path.pos(j+3).z = tree.vertex(pathIndex).z;
        pathIndex = tree.vertex(pathIndex).indPrev; %% index or iter that closest to current iter
        
        if pathIndex == 1
            break
        end
        j=j+1;
    end
    path.pos(end+1).x = xInit; path.pos(end).y = yInit; path.pos(end).z = zInit;
    for j = 2:length(path.pos)
        plot3([path.pos(j).x; path.pos(j-1).x;], [path.pos(j).y; path.pos(j-1).y], [path.pos(j).z; path.pos(j-1).z], 'b', 'Linewidth', 3);
    %     plot([tree.vertex(i).x; tree.vertex(ind).x],[tree.vertex(i).y; tree.vertex(ind).y], 'r');
    %     pause(0);
%     f=getframe(gcf);
%     writeVideo(obj,f)
    end
        
else
    disp('No path found. Increase number of iterations and retry.');
end
