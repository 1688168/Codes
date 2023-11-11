> consider odd case

p[i]: extended radius of the longest palindromic substring centered at i
A                 B
1 2 3 4 5 6 7 8 9 0 1 2 3 
x x x x x x x x x x x x x} x x x 
            ^
           ctr
    j             i
                        ctr_right


consider p[j]
assume p[j]=2
A1==A4
A2==A5

consider p[ctr]
A1==A5==A9
A2==A4==B0
A3==B0

