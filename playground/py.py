# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict


def solution(V, A, B):
    """
    N projs: 0~N-1
    V[K]: value of proj K
    M requirements
    A[L], B[L] ???
    at most two proj, sequential order
    => highest value
    """
    mxv = 0

    g = defaultdict(set)
    vii = []
    for ii, vv in enumerate(V):
        vii.append((vv, ii))
    # sort value so we can be greedy
    vii.sort(key=lambda x: -x[0])  # sort in decreasing order per value

    print("vii: ", vii)

    # to lookup B's prerequisits
    for ii in range(len(B)):
        g[B[ii]].add(A[ii])

    print("g: ", g)
    # try from the highest value proj see if that works
    for ii in range(len(vii)):
        print(" ii: ", ii, " mxv: ", mxv)
        first_pv = vii[ii][0]  # first project value
        if first_pv <= 0: continue

        print(" first_pv: ", first_pv)
        #### case you have prerequisite
        # what's the prerequisite
        if vii[ii][1] in g and len(g[vii[ii][1]]) > 1:  # need to complete more then two prerequisites
            print(" proj ", vii[ii][1], " has > 1 pre-requisites, continue")
            continue  # dropping this proj as too many prerequisites

        if vii[ii][1] in g and len(g[vii[ii][1]]) == 1:
            # do you have more prerequisites
            for p in g[vii[ii][1]]:
                prerequisite_proj = p  # get the only prerequisite from set
            print(" got prerequisite proj: ", prerequisite_proj)
            if prerequisite_proj in g:
                print(" this prerequisite proj has more pre-requisite, skipping")
                continue  # cannot do this combination as exceeding two projs

            # now we can use this
            mxv = max(mxv, first_pv + V[prerequisite_proj])
            print(" case 1 mxv: ", mxv)
            continue
        mxv=max(mxv, first_pv)
        print(" finding 2nd proj ============== ")
        ### case you don't have prerequisite ---> find the next hightest value proj that has no pre-requisite
        for jj in range(len(vii)):
            if jj==vii[ii][1]: continue
            if jj in g:  # more prerequisites:
                print(" proj 2: ", jj, " has more prerequisites, skipping")
                continue
            second_proj_value = V[jj]
            print(" 2nd proj jj: ", jj)
            if second_proj_value <= 0: break  # no need to add an independent negative value proj, it's only do harm.
            mxv = max(mxv, first_pv + second_proj_value)
            break
    print(" =============== mxv: ", mxv)

    return mxv

#print("mxv: ", solution([-3, 5, 7, 2, 3], [3, 1], [2, 4]))
print("mxv: ", solution([13, 32, 5, 17, 50],[], []))
