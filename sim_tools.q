\d .sim_tools

/ path method
/ 4 params [Sigma, Rate of Drift, Interval Time Step]
path:{[s;r;t]
    z:.stat_tools.norminv count[t]?1f;
    p:prds .stat_tools.gbm[s;r;deltas[first t;t]] z;
    p}


