\l stat_tools.q
\l sim_tools.q
\l tooling.q
\l data_cleaning.q

makeSampleDates:{[start;days] start+til days}

makeSampleTable:{
    DateTime: makeSampleDates[2001.01.01;1000000]
    Open: 1000000?100;
    High: 1000000?120;
    Low: 1000000?80;
    Close: 1000000?100;
    Volume: 1000000?10000;
    t:([] DateTime:DateTime ; Open:Open ; High:High ; Low:Low ; Close:Close; Volume:Volume);
    t}
