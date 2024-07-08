/ import method from library to use in current directory
use:{system["d"] upsert $[99h=type v:get x;v;(-1#` vs x)!1#v]}

/ filter list of dates to only list of weekdays
wday:{x where 1<x mod 7}

/ generate list of numbers
/ stride width, starting value, ending value
range:{[w;s;e] s+ w*til ceiling(e-s)%w}

/ rounding
round:{x*"j"$y%x}