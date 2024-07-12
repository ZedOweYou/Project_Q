\d .data_cleaning

norm:{[x] 1+(100*x-first x)%first x}
return:{[x]}

normTable:{[t]
    t: update N_Open: norm[Open], N_High: norm[High], N_Low: norm[Low], N_Close: norm[Close] from t;
    t: update R_Open: deltas N_Open, R_High: deltas N_High, R_Low: deltas N_Low, R_Close: deltas N_Close from t;
    t: update C_Open: (sums R_Open)-1, C_High: (sums R_High)-1, C_Low: (sums R_Low)-1, C_Close: (sums R_Close)-1 from t;
    t: update R_Open: 0.0, R_High: 0.0, R_Low: 0.0, R_Close: 0.0 from t where i=0;
    t}
