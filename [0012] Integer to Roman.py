class Solution:
    def intToRoman(self, num: int) -> str:
        """
        0. I~III, IV, V, 6~8, IX, X

        1. XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIV, XX
                          ^^^^^^^^
        The range of number: 1~3999
        : r1+r2+r3+r4
        """

        if num < 1 or num > 3999:
            return None


        mm={
            1:'I',
            2:'II',
            3:'III',
            4:'IV',
            5:'V',
            6:'VI',
            7:'VII',
            8:'VIII',
            9:'IX',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'

        }


        def get1():
            """
            : get last digit: 0~9
            """
            d1=num%10
            if d1==0: return ""
            return str(mm[d1])


        def get2():
            """
            X
            XX
            XXX
            XL <<
            L  <
            LX
            LXX
            LXXX
            XC <<
            """
            d2=(num%100)//10
            r2=""
            if d2==4:
                r2="XL"
            elif d2==5:
                r2=mm[50]
            elif d2==9:
                r2='XC'
            elif d2==0:
                r2=''
            else:
                if d2 <=3:
                    r2='X'*d2
                elif d2 >= 5 and d2 < 9:
                    r2= 'L'+'X'*(d2-5)
            return r2


        def get3():
            d3=(num//100)%10
            r3=""


            if d3 == 0:
                pass
            elif d3==4:
                r3="CD"
            elif d3==5:
                r3="D"
            elif d3==9:
                r3="CM"
            elif d3<5:
                r3=""+'C'*d3
            else:
                r3="D"
                r3='D'+'C'*(d3-5)

            return r3

        def get4():
            d4=num//1000

            r4=''+'M'*d4


            return r4


        rr1=get1()
        rr2=get2()
        rr3=get3()
        rr4=get4()
        # print("rr1: ", rr1)
        # print("rr2: ", rr2)
        # print("rr3: ", rr3)
        # print("rr4: ", rr4)
        res=rr4+rr3+rr2+rr1

        #print("res: ", res)
        return res
