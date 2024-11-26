# PyStats

CLI utility to compute stats/visualize streams of data

e.g.

```console
aneesh@earth:~/pystats$ head example.csv 
0 9
1 13
2 13
3 95
4 4
5 14
6 64
7 70
8 3
9 59
aneesh@earth:~/pystats$ cat example.csv | awk "{ print \$2 }" | pystats avg
50.388
aneesh@earth:~/pystats$ cat example.csv | awk "{ print \$2 }" | pystats std
28.83306185614008
aneesh@earth:~/pystats$ cat example.csv | awk "{ print \$2 }" | pystats max
100.0
aneesh@earth:~/pystats$ cat example.csv | awk "{ print \$2 }" | pystats min
0.0
aneesh@earth:~/pystats$ cat example.csv | awk "{ print \$2 }" | pystats histogram
```

Note that histogram uses `matplotlib` to render a histogram and will open a GUI window.
