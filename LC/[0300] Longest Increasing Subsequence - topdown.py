def lengthOfLIS_with_cache(self, nums):  # time exceeded
    """
    :20210925: adding cache
    :param nums:
    :return:
    : Time: O(N^2).  T(N)=T(n-1)+T(n-1)
    """
    def hp(st=0, prev=-1):
        if st >= len(nums): return 0
        if dp[st][prev] != -1: return dp[st][prev]


        tke = 0
        if prev == -1 or nums[st] > nums[prev]:
            tke = 1 + hp(st + 1, st)

        ntk = hp(st + 1, prev)

        dp[st][prev]=max(tke, ntk)
        return dp[st][prev]

    dp=[[-1]*len(nums) for _ in range(len(nums)+1)]

    return hp()

############################################################
def lengthOfLIS_with_lru_cache(self, nums):  # time exceeded
    """
    :20210925: adding cache
    :param nums:
    :return:
    : Time: O(N^2).  T(N)=T(n-1)+T(n-1)
    """

@lru_cache(None)
def hp(st=0, prev=-1):
    if st >= len(nums): return 0

    tke = 0
    if prev == -1 or nums[st] > nums[prev]:
        tke = 1 + hp(st + 1, st)

    ntk = hp(st + 1, prev)

    return max(tke, ntk)

return hp()

def lengthOfLIS_brutal_force(self, nums): # time exceeded
    """
    :20210925: brutal force solution
    :param nums:
    :return:
    : Time: O(N^2).  T(N)=T(n-1)+T(n-1)
    """
    def hp(st=0, prev=-1):
        if st >= len(nums): return 0

        tke=0
        if prev == -1 or nums[st] > nums[prev]:
            tke = 1 + hp(st+1, st)

        ntk=hp(st+1, prev)

        return max(tke, ntk)


    return hp()
