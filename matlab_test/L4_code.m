%% Financial Econometrics
% Lecture 4 - Time Series
% Colin Ward

close all
clear all
clc

% In this lecture we go through some basic concepts in time series.  Tsay's
% book, listed in the syllabus, will be useful for additional context and
% details.  Our first goal is to connect the two constructions of
% time series; namely, one as a realization of sample and two as a
% theoretical (probability) model that describes the time series behavior
% of the sample in question.  

% We do this by constructing artificial data sets under the
% assumption of a particular data generating process (DGP) (examples of
% DGPs are ARMA(1,1) or MA(3) or AR(2)).  We then use the simulated data to
% compute conditional and unconditional means and variances or ACFs to
% compare with the true DGP.  A more advanced class carries this 
% observation further.

% The point of artificial data is to understand the model before applying
% it to actual data.  Thus artificial data allows us to vet our
% estimations, allowing us to see if we are estimating well the underlying
% process


%% Monte Carlo Simulation
% AR(2) model x(t) = mu + phi1*x(t-1) +phi2*x(t-1) + e(t)

T = 200; % Number of observations

% Parameters
mu = 0.1; % Intercept of the process -- not the mean
sigma = 0.04; % Volatility of white noise
phi1 = 0.8; % Size of first AR component
phi2 = -0.5; % Size of second AR component 

rng(1) % Tthis command fixed a seed for our pseudo-random number generator
% I'll discuss why they're called pseudo and how rng's work in class 

wn = sigma*randn(T,1); % Simulate Gaussian white noise ~ N(0,sigma^2)
% White noise is our time series building block.  randn constructs them 
% as iid.  

x = zeros(T,1); % Initialize the size of x
x(1) = mu/(1-phi1-phi2); % Set x(1) to the unconditional mean, Ex
x(2) = mu/(1-phi1-phi2) + sigma*wn(2); % x(2) = Ex + noise

% Now construct the DGP (the model) from stochastic realizations of our
% white noise building blocks
for t = 3:T
    x(t) = mu + phi1*x(t-1) + phi2*x(t-2) + wn(t);
end
% This is our artificial data series

% Notice that a simulated persistent process like an AR(1) or ARMA(1,1), etc., 
% depends on the first realization of the process, x(1), an input that we
% control.  When estimating our model we do not want our estimates to be
% effected by our starting choice.  That said, a common practice is to
% burn-in the first z% of observations so that the initial values effect
% has had sufficient time to die out.  The magnitude of z depends on the
% persistence of the process (high phi in AR(1) requires a longer burn-in).
% Values of z = 50% are common.

x = x(T*0.1:end); % This burns in the first 10 percent

% Now let's compute sample moments with our theoretical moments
mean(x)
Ex = mu/(1-phi1-phi2)

std(x)
% Two versions of exact std
stdx = sqrt( (1-phi2)/(1+phi2)/((1-phi2)^2-phi1^2) * sigma^2 )
stdx_v2 = sqrt( sigma^2/( (1-phi1^2-phi2^2) - 2*phi1^2*phi2/(1-phi2)))

% How well do you think our sample moments recover our true theoretical
% moments as T->infty?

% Moving on, let's compute the model's ACF
ac = acf(x,10);

figure;
stem(0:10,ac,'filled'), xlabel('Lag'), legend('Sample ACF')
print('-depsc','AR2acf.eps')
% We spent some time shutting down phi1,phi2 and looking at different T

% Now once we have the model generated, we can estimate the parameters.
% Since it is an AR process we can use OLS.  For MA or ARMA processes we
% need to use maximum likelihood (next lecture)

y = x(3:end);
X = [ones(length(y),1) x(2:end-1) x(1:end-2)];
[T K] = size(X);
b = X\y
e = y-X*b;
sigmahat = sqrt(e'*e/(T-K)) 
% This last variable is the estimate of error stdev (recall wn~N(0,sigma^2))

% That concludes all of the parameters that we can estimate in an AR(2)
% model: mu, phi1, phi2, and sigma


% Is our process stationary?  Recall that for a AR(1) it simply is if
% |phi|<1.  For MAs it is as long as theta(q) is finite.  
% In the case of an AR(p) where p>1 it is if the "roots lie outside the
% unit circle".  Using Matlab we can look at the roots of the equation 
% (1-phi1*z-phi2*z^2) = 0 that is a function of z.

% Check if roots lie outside unit circle
R = roots([-phi2 -phi1 1])
sqrt(real(R).^2+imag(R).^2)

% Time series models are widely used to forecast.  We first "fit" a time 
% series model to the data.  Once it is properly fit you can then forecast.  
% To assess fit we look at the residuals of the
% fitted model.  The idea is that if all of the "signal" has been extracted
% from the data, the residuals should contain only "noise"; ie, no
% information left---that is, they should look like white noise---iid at
% all leads and lags.  Looking at an ACF allows us to judge this.

figure;
stem(0:20,acf(e,20),'filled')

% Now check Bartlett standard errors to see if they statistically look like
% white noise

hold on
plot([0 20], [1.96/sqrt(T) 1.96/sqrt(T)],'k--')
plot([0 20],-[1.96/sqrt(T) 1.96/sqrt(T)],'k--')
hold off

% Since they look like white noise, we are then free to forecast

% That, in a nutshell is what time series analysis is about.  These are
% only for univariate series.  More generally, people use vector
% autoregressions (VARs) to forecast multiple series at a time.  The point
% of my showing you how to generate fake data and the estimating it is
% something that you would need to understand if you decide to ever
% estimate a more complicated model.  You need to be able to test that your
% estimation in fact returns the true DGP.  After you confirm that your
% estimation is correct, then you feed in the data.

% We can now turn to an forecasting application of our univariate time 
% series model

%% Application - Shiller's CAPE
load ShillerCAPE.txt

yr = ShillerCAPE(:,1);
PE = ShillerCAPE(:,2);

figure;
plot(yr,PE), ylabel('Cyclically-Adjusted Price-Earnings Ratio')
print('-depsc','CAPE.eps')

%% Forecasting exercise
% Academics and professionals take seriously the idea of 
% out-of-sample forecasting performance.  You fit the model within a subsample of your
% complete data set.  You then forecast and see how well the model predicts
% out of that subsample.

% So carrying on with this idea, let's compute a forecast at a certain 
% date, say 1981, using data only up until that date

% First restrict the data to only up until 1981
t1981 = find(yr<=1981);
PE1981 = PE(t1981);

% Now given this subsample we're going to fit our model and forecast

%% Fitting the model

% The idea behind fitting a model is equivalent is to figuring out the 
% (p,q) order of a general ARMA(p,q) model.  Recall that looking at the ACF
% and PACF helps us determine if the model is a pure MA(q) or else a pure
% AR(p)

% We begin by computing the ACF and PACF
% We can use our ACF code from before
% Note that Matlab provides a function autocorr for computing ACFs.  
% I'll leave it for you to look it up and figure it out.  Sometimes it is
% just better to program things yourself
L = 10;
ac = acf(PE1981,L);
figure;
stem(0:L,ac,'filled'), xlabel('Lag'), ylabel('Price-Earnings Sample ACF')
print('-depsc','CAPEacf.eps')

% PACF 
% I'll leave it to you to write a loop and define a function pacf(x,L)
% analogously to our acf(x,L) function
% Alternatively, Matlab provides a parcorr function
% Since I know the order is going to be low, I'll just compute the PACF
% step-by-step
y = PE1981(2:end);
X = [ones(length(y),1) PE1981(1:end-1)];
b = X\y;
pacf1 = b(end);

y = PE1981(3:end);
X = [ones(length(y),1) PE1981(2:end-1) PE1981(1:end-2)];
b = X\y;
pacf2 = b(end);

y = PE1981(4:end);
X = [ones(length(y),1) PE1981(3:end-1) PE1981(2:end-2) PE1981(1:end-3)];
b = X\y;
pacf3 = b(end);

% We'll collect the pacf coefficients in a vector and compare it with a
% null hypothesis of phi_j = 0 for j = 1,2,3
[pacf1 pacf2 pacf3]
% We use Bartlett standard errors under our null: 1/sqrt(T).  At the
% two-tailed 5% significance level we compute 
ac_crit = norminv(1-0.05/2)/sqrt(T)

% Since only the first value is statistically different from zero, we'll
% run with an AR(1).  We begin by estimating an AR(1) and then assessing
% its fit

%% 1. Estimate our AR(1) specification
y = PE1981(2:end);
X = [ones(length(y),1) PE1981(1:end-1)];
[T K] = size(X);
b = X\y % These are our intercept and AR(1) coefficient
e = y - X*b; % Residuals
sigma = sqrt(e'*e/(T-K)); % This is the estimate of error variance

muy = b(1)/(1-b(2));
stdy = sqrt(sigma^2/(1-b(2)^2));

% Let's compare model moments with sample moments.  These should be close
[mean(y) muy] 
[std(y) stdy]

%% 2. Check residuals
% Recall that if the model is sufficient, the residuals should look like
% white noise---uncorrelated at all leads and lags
ace = acf(e,L);
figure;
stem(0:L,ace,'filled'), xlabel('Lag'), ylabel('Residual''s Sample ACF')
hold on
    plot([0 L],[ac_crit ac_crit],'k--')
    plot([0 L],-[ac_crit ac_crit],'k--')
hold off
print('-depsc','uacf.eps')

% Formal test (Ljung-Box)
Q3 = T*(T+2)*sum(ace(2:4).^2./[T-1;T-2;T-3])
Q3_crit = chi2inv(1-0.05,3)

% It seems that the Q test statistic is less than the critical value, so
% the null that autocorrelation is present in the residuals is not
% rejected. Both the "eyeball" test on the residual's ACF and the Ljung-Box
% test suggest we have removed all temporal dependence in the residuals.
% We can now move on to forecasting.

%% 3. Forecasting
% Before forecasting, let's take a quick look at our fitted values and
% compare them with the full sample of data 
figure;
plot(yr,PE)
hold on
    plot(yr,[nan;X*b;nan(length(yr)-T-1,1)],'r')
    plot([1981 1981],ylim,'k-')
hold off
legend('CAPE','$\widehat{CAPE}$','location','best')
ylabel('Cyclically-adjusted Price-Earnings Ratio')
print('-depsc','fitted.eps')

% Now we will forecast.  First, we specify a forecast horizon.  Let's just
% set it to be equal to the length of the remaining sample post 1981
H = length(PE)-length(PE1981); % Forecast horizon length

% We'll preallocate our forecast and forecast error vectors
yfore = zeros(H,1); % Forecast
e = zeros(H,1); % Forecast errors

% One thing that we noticed when forecasting is that there is a recursive
% structure to it---once we've forecasted one-period out, our two-period's
% best forecast is based on our one-period forecast, etc.

% We begin initializing our forecasting using the AR(1) and our last data
% point
yfore(1) = b(1) + y(end)*b(2); % First forecast 1982, given data up to 1981
e(1) = PE(max(t1981)+1) - yfore(1); % First forecast error

% Now we can compute our recursive forecast for the rest of the sample
forecast_variance_factor = ones(H,1);
for h = 2:H 
    % The next equation is the recursive forecast.  It's easy to compute
    % and loop over it
    yfore(h) = b(1) + b(2)*yfore(h-1); 
    
    % The next two equations are the forecast errors and the factor for 
    % the variance of forecast errors
    e(h) = PE(max(t1981)+h) - yfore(h);
    
    % Forecast error variance factor takes the form: 1+phi^2+phi^4+...+phi^{h-1}
    % This is a recursive construction
    forecast_variance_factor(h) = forecast_variance_factor(h-1) + b(2)^(2*(h-1)); 
end

% Now we can compute forecast error variance using our constructed forecast_factor
sigmae = sqrt([nan(length(y)+1,1); forecast_variance_factor*sigma^2]);

% Practitioners (and some academics) would be interested a summary measure
% of the out-of-sample forecasting performance of a model.  Two common
% measures are root mean square error (RMSE) and mean absolute deviation
% (MAD)
RMSE = sqrt(mean(e.^2))
MAD = sum(abs(e))/(H-1)

% You would compare the RMSE of our AR(1) with other models like an
% ARMA(1,1) or a MA(3).  Whichever model has the lowest RMSE/MAD would be
% the best out-of-sample forecaster.

% Note that it is possible that there could be the case where, say, 
% an AR(1) and an ARMA(1,1) are both well-fitted models, in the sense that
% their residuals both look like white noise.  How to pick which model
% then?  One option is to choose the one with the better out of sample
% performance.  Another option is the choose the one that is the most
% parsimonious (has the least parameters).  Parsimony is preferred because
% it's less likely that you're overfitting the data, that should make your
% forecasts more robust.  

% Note also that there isn't a clearly defined scientific way to choose 
% the best model.  Forecasting is an art and requires judgment.  

%% 4. Conclusion
% We can now summarize the results of our forecasting exercise with a
% picture.

figure;
% This plots the data
plot(yr,PE)

hold on
    % These first two equations plot the forecast and the models
    % unconditional mean
    plot(yr,[nan;X*b;yfore],'r')
    plot([min(yr) max(yr)],[muy muy],'k--')
    
    % The next three equations plot the forecast error variance around the
    % unconditional mean
    plot(yr,[ [nan;X*b;yfore]-sigmae [nan;X*b;yfore]+sigmae ],'r:')
    plot([min(yr) max(yr)],[muy+stdy muy+stdy],'k:')
    plot([min(yr) max(yr)],[muy-stdy muy-stdy],'k:')
    
    % And finally our 1981 end-of-sample vertical marker
    plot([1981 1981],ylim,'k-')
hold off
ylim([3 27]) % Change the ylimit to zoom in on the forecast

legend('Data','1981 model and conditional forecast','1981 unconditional mean and stdev','location','best')
print('-depsc','forecast.eps')

%%
% function ac = acf(x,L)
% % L is lag of ACF
% % x is time series vector
% 
% ac0 = var(x);
% ac = zeros(L,1);
% for l = 1:L
%     ac(l) = diag(cov(x(1+l:end),x(1:end-l),1),-1);
% end
% 
% ac = [1; ac./ac0];