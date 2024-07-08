\l stat_tools.q

/ path method
/ 4 params [Sigma, Rate of Drift, Interval Time Step]
path:{[s;r;t]
    z:norminv count[t]?1f;
    p:prds gbm[s;r;deltas[first t;t]] z;
    p}


