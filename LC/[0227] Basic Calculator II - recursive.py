#################
# 20231118
#################
class Solution:
    def calculate(self, s: str) -> int:
        N = len(s)

        def dfs(ii, ttl, prev, op):
            if ii == N:
                return ttl

            cc = s[ii]
            if cc.isdigit():  # get num
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1
                nn = int(s[ii:jj])
                ii = jj

                # we need to merge number here
                if op == "+":
                    ttl += nn
                    return dfs(ii, ttl, nn, op)
                elif op == "-":
                    ttl -= nn
                    return dfs(ii, ttl, -nn, op)
                elif op == "*":
                    ttl = ttl-prev + (pp := prev*nn)
                    return dfs(ii, ttl, pp, op)
                elif op == "/":
                    ttl = ttl-prev + (pp := abs(prev)//nn *
                                      (1 if prev > 0 else -1))
                    return dfs(ii, ttl, pp, op)
                else:
                    msg = f"Unexpected expression: nn=[{nn}], op=[{op}]"
                    raise Exception(msg)
            else:  # space or op
                if cc == " ":
                    return dfs(ii+1, ttl, prev, op)
                else:
                    return dfs(ii+1, ttl, prev, cc)

        return dfs(0, 0, 0, "+")


#################################
class Solution:
    def calculate(self, s: str) -> int:

        mulDiv = set(["*", "/"])
        ops = set(["*", "/", "+", "-"])

        def dfs(st, ttl, prev, op):
            # print(" st: ", st, " ttl: ", ttl, " prev: ", prev, " op: ", op)
            if st == len(s):
                return ttl

            if s[st] not in ops:  # got a num
                jj = st
                while jj < len(s) and s[jj] not in ops:
                    jj += 1
                nn = int(s[st:jj])
                st = jj
                if op == "+":
                    ttl += nn
                    return dfs(st, ttl, nn, op)
                elif op == "-":
                    ttl -= nn
                    return dfs(st, ttl, -nn, op)
                elif op == "*":
                    ttl = (ttl-prev) + (pp := prev * nn)
                    return dfs(st, ttl, pp, op)
                elif op == "/":
                    ttl = (ttl-prev) + (pp := abs(prev) //
                                        nn * (-1 if prev < 0 else 1))
                    return dfs(st, ttl, pp, op)
                else:
                    # print(" what is this? ", op)
                    pass
            else:
                return dfs(st+1, ttl, prev, s[st])

        return dfs(0, 0, 0, "+")
