% Define the joint variables for each joint
theta1 = 0;    % Initial joint angle for Link 1
theta2 = 0;    % Initial joint angle for Link 2
theta3 = 0;    % Initial joint angle for Link 3
theta4 = 0;    % Initial joint angle for Link 4
theta5 = 0;    % Initial joint angle for Link 5

% Define the link offsets (d) and lengths (a)
d1 = 65;        % Fixed offset for Link 1
d2 = 0;        % Fixed offset for Link 2
d3 = 0;        % Fix
% ed offset for Link 3
d4 = 0;        % Fixed offset for Link 4
d5 = 182;        % Fixed offset for Link 5

a1 = 0;
a2 = 27;
a3 = 105;
a4 = 133;
a5 = 0;

alpha1 = 0;
alpha2 = pi/2;
alpha3 = 0;
alpha4 = pi;
alpha5 = pi/2;

% Define the DH parameters using the variables
L1 = Link('revolute', 'd', d1, 'a', a1, 'alpha', alpha1, 'offset', theta1, 'modified');
L2 = Link('revolute', 'd', d2, 'a', a2, 'alpha', alpha2, 'offset', theta2, 'modified');
L3 = Link('revolute', 'd', d3, 'a', a3, 'alpha', alpha3, 'offset', theta3, 'modified');
L4 = Link('revolute', 'd', d4, 'a', a4, 'alpha', alpha4, 'offset', theta4, 'modified');
L5 = Link('revolute', 'd', d5, 'a', a5, 'alpha', alpha5, 'offset', theta5, 'modified');
L = [L1, L2, L3, L4, L5];  % Create an array of links
My3R = SerialLink(L, 'name', '5DOF');

qi = [pi/3 pi/4 pi/5 pi/6 pi/7];%pi/3 pi/4 pi/5 pi/6 pi/7
qd = [2*pi/3 2*pi/4 2*pi/5 2*pi/6 2*pi/7];%2*pi/3 2*pi/4 2*pi/5 2*pi/6 2*pi/7
qc = [1.5708 0.523599 1.39626 0.174533 1.5708];

% Calculate forward kinematics for the initial and desired joint angles
Ti = My3R.fkine(qi);  % Forward kinematics for initial joint angles
Td = My3R.fkine(qd);  % Forward kinematics for desired joint angles
Tc = My3R.fkine(qc);
% Display the transformation matrices
disp('Forward Kinematics - Initial Position (Ti):');
disp(Ti);

disp('Forward Kinematics - Desired Position (Td):');
disp(Td);

disp('Forward Kinematics - Desired Position (Tc):');
disp(Tc);


plot(My3R, qi), view(2);
plot(My3R, qd), view(2);

L(1).qlim = [0,pi];
L(2).qlim = [0,pi];
L(3).qlim = [0,pi];
L(4).qlim = [0,pi];
L(5).qlim = [0,pi];

My3R.plot([0 0 0 0 0], 'workspace', [-10 10 -10 10 -10 10]);
My3R.teach([0 0 0 0 0 ]);