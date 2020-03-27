clc;
clear;
close all;

% Generate Data
W = randn(1000,2);
A = rand(2,2);
X = W*A;

% Covariance Matrix
C = cov(X);

% Find PC1
[V,E] = eig(C);
[emax, emax_id] = max(diag(E));
u = V(:,emax_id);

% Transform Data
z = X*u;

% Decide DAta
Y = z*u';

% Plot results
figure;
scatter(X(:,1),X(:,2));
hold on;
scatter(Y(:,1),Y(:,2));