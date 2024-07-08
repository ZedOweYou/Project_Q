/ Box Mueller
/ convert 2 uniform random variates to 2 normal random variates
bm:{
    if [count[x] mod2; '`length];
    x:2 0N#x;
    r:sqrt -2f*log x 0;
    theta: 2f*acos[-1]*x 1;
    x: r*cos theta;
    x,:r*sin theta;
    x}

/ Beasley Springer 
/ inverse cumulative normal
cnorminv:{
    a:-25.44106049637 41.39119773534 -18.61500062529 2.50662823884;
    b: 3.13082909833 -21.06224101826 23.08336743743 -8.47351093090 1;
    x*:horner[a;s]%horner[b] s:x*x-:.5;
    x}

/ Horner's method 
/ like the "scalar from vector" operator but for many values instead of single
horner:{{z+y*x}[y]/[x]}

/ exponetially weighted moving averages
ewma:{first[y] (1f-x)\x*y}

/ Chebyshev approximation by Boris Moro
/ normal inverse approximation for tailend
tnorminv:{
    a:0.0000003960315187 0.0000002888167364 0.0000321767881768
      0.0003951896511919 0.0038405729373609 0.0276438810333863
      0.1607979714918209 0.9761690190917186 0.3374754822726147;
    x:horner[a] log neg log 1f-x;
    x}

/ Beasley Springer Moro
/ uses Beasley Springer polynomial approximation to compute inverse cumulative normal
/ uses the Chebyshev approximation for tail regions
norminv:{
    i:x<0.5;
    x:?[i;1f-x;x];
    x:?[x<0.92;cnorminv x; tnorminv x];
    x:?[i; neg x; x];
    x}

/ Geometric Brownian Motion
/ 4 params [Sigma, Rate of Drift, Interval Time Step, Normal Random Realizations]
gbm:{[s;r;t;z] exp(t*r-.5*s*s)+z*s*sqrt t}