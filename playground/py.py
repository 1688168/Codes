def ff(nums1, nums2):
    N1 = len(nums1)
    N2 = len(nums2)
    s1 = set(nums1)
    s2 = set(nums2)
    print("N1: ", N1, " N2: ", N2, " len s1: ", len(s1), " len s2: ", len(s2))
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()

    ii, jj = 0, 0

    res=set()
    while ii < len(l1) and jj < len(l2) and ii < N1//2 and jj < N2//2:
        if ii < N1//2 and l1[ii] < l2[jj]:
            res.add(l1[ii])
            ii+=1
            continue

        if ii < N1//2 and jj < N2//2 and l1[ii]==l2[jj]:
            res.add((l1[ii]))
            ii+=1
            jj+=1
            continue

        if jj < N2//2:
            res.add(l2[jj])
            jj+=1
            continue

        break

    print(" res: ", res, " ii: ", ii, " jj: ", jj)
    while ii < N1//2 and ii < len(l1):
        res.add(l1[ii])
        ii+=1

    while jj < N2//2 and jj < len(l2):
        res.add(l2[jj])
        jj+=1


    return len(res)


    # s11=set()
    # if len(s1) > N1//2:
    #     for n in s1:
    #         if n not in s2:
    #             s11.add(n)
    # else:
    #     s11=s1
    # s1=s11
    # s22=set()
    # if len(s2) > N2//2:
    #     for n in s2:
    #         if n not in s1:
    #             s22.add(n)
    # else:
    #     s22=s2
    #
    # s2=s22
    # final_set=set()
    #
    # print(" final s1: ", s1)
    # print(" final s2: ", s2)
    # cnt=0
    # for n in s1:
    #     final_set.add(n)
    #     cnt+=1
    #     if cnt ==N1//2: break
    #
    # cnt=0
    # for n in s2:
    #     final_set.add(n)
    #     cnt+=1
    #     if cnt == N2//2: break
    #
    # return len(final_set)




if __name__ == '__main__':
    nums1=[1,2,3,4,5,6] #[1,2,1,2]
    nums2=[2,3,2,3,2,3] # [1,1,1,1,]

    nums1=[1,1,2,2,3,3]
    nums2=[4,4,5,5,6,6]

    # expect 4
    nums1=[2, 4, 1, 4]
    nums2=[10, 2, 4, 10]
    ans=ff(nums1, nums2)
    print("ans: ", ans)