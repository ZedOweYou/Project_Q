box_muller:{[x]
    if [count[x] mod2; '`length];
    x:2 0N#x;
    r:sqrt -2f*log x 0;
    theta: 2f*acos[-1]*x 1;
    x: r*cos theta;
    x,:r*sin theta;
}