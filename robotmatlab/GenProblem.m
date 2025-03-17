function GenProblem

xMin=round(10*rand);
xMax=round(200*rand);
yMin=round(10*rand);
yMax=round(200*rand);
zMin=round(10*rand);
zMax=round(200*rand);

disp(['x_min = ' num2str(xMin) '    x_max = ' num2str(xMax)])
disp(['y_min = ' num2str(yMin) '    y_max = ' num2str(yMax)])
disp(['z_min = ' num2str(zMin) '    z_max = ' num2str(zMax)])

pObstacles=[xMin;yMin;zMin]+([xMax;yMax;zMax]-[xMin;yMin;zMin]).*rand(3,5);
pObstacles=pObstacles'

figure(1),clf,hold on
plot3(xMin, yMin, zMin, 'ko', 'MarkerSize',10, 'MarkerFaceColor','k');
plot3(xMax, yMax, zMax, 'go', 'MarkerSize',10, 'MarkerFaceColor','g');
plot3(pObstacles(:,1),  pObstacles(:,2), pObstacles(:,3), 'bo', 'MarkerSize',20, 'MarkerFaceColor','b');

view(60,30)
hold off