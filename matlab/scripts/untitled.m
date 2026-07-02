% Define the joint variables for each joint
theta1 = 0;    % Initial joint angle for Link 1
theta2 = 0;    % Initial joint angle for Link 2
theta3 = 0;    % Initial joint angle for Link 3
theta4 = 0;    % Initial joint angle for Link 4
theta5 = 0;    % Initial joint angle for Link 5
theta6 = 0;    % Initial joint angle for Link 6

% Define the link offsets (d) and lengths (a)
d1 = 18;        % Fixed offset for Link 1
d2 = 0;         % Fixed offset for Link 2
d3 = 0;         % Fixed offset for Link 3
d4 = 0;         % Fixed offset for Link 4
d5 = 70;        % Fixed offset for Link 5
d6 = 32;        % Fixed offset for Link 6

a1 = 0;
a2 = 0;
a3 = 104;
a4 = 147;
a5 = 0;
a6 = 0;

alpha1 = 0;
alpha2 = pi/2;
alpha3 = 0;
alpha4 = 0;
alpha5 = pi/2;
alpha6 = 0;

% Define the DH parameters using the variables
L1 = Link('revolute', 'd', d1, 'a', a1, 'alpha', alpha1, 'offset', theta1, 'modified');
L2 = Link('revolute', 'd', d2, 'a', a2, 'alpha', alpha2, 'offset', theta2, 'modified');
L3 = Link('revolute', 'd', d3, 'a', a3, 'alpha', alpha3, 'offset', theta3, 'modified');
L4 = Link('revolute', 'd', d4, 'a', a4, 'alpha', alpha4, 'offset', theta4, 'modified');
L5 = Link('revolute', 'd', d5, 'a', a5, 'alpha', alpha5, 'offset', theta5, 'modified');
L6 = Link('revolute', 'd', d6, 'a', a6, 'alpha', alpha6, 'offset', theta6, 'modified');
L = [L1, L2, L3, L4, L5, L6];  % Create an array of links

% Create a SerialLink object
My6R = SerialLink(L, 'name', '6DOF');

% Define joint angles (qi: initial, qd: desired)
qi = [pi/3 pi/4 pi/5 pi/6 pi/7 pi/8];
qd = [2*pi/3 2*pi/4 2*pi/5 2*pi/6 2*pi/7 2*pi/8];

% Calculate forward kinematics for the initial and desired joint angles
Ti = My6R.fkine(qi);  % Forward kinematics for initial joint angles
Td = My6R.fkine(qd);  % Forward kinematics for desired joint angles

% Display the transformation matrices
disp('Forward Kinematics - Initial Position (Ti):');
disp(Ti);

disp('Forward Kinematics - Desired Position (Td):');
disp(Td);

% Plot the robot at the initial position
figure;
My6R.plot(qi);
view(3);

% Plot the robot at the desired position
figure;
My6R.plot(qd);
view(3);

% Set joint limits
L(1).qlim = [-pi/2, pi/2];
L(2).qlim = [-pi/2, pi/2];
L(3).qlim = [-pi/2, pi/2];
L(4).qlim = [-pi/2, pi/2];
L(5).qlim = [-pi/2, pi/2];
L(6).qlim = [-pi/2, pi/2];

% Plot the robot with the desired initial joint angles and set up the workspace
My6R.plot([0 pi/2 0 pi/2 0 0], 'workspace', [-200 200 -200 200 -200 200]);

% Use the teach function for manual control of the robot with the desired initial joint angles
My6R.teach([0 pi/2 0 pi/2 0 0]);