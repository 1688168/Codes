###########
# 20231118
###########
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        1. determine the max_len (calc the min remove cnt)
        2. DFS to find all valid parentheses after removal
        - think of memo
        - the pruning strategy
        - remove duplicate strategy
        """
        N = len(s)
        left_cnt = 0
        remove_cnt = 0
        for ii, cc in enumerate(s):
            if cc.isalpha():
                continue
            elif cc == "(":
                left_cnt += 1
            else:
                if left_cnt > 0:
                    left_cnt -= 1
                else:
                    remove_cnt += 1

        remove_cnt += left_cnt
        valid_len = N-remove_cnt
        print(" expected parentheses len: ", valid_len)

        res = []

        def dfs(st, path, left_cnt):
            if left_cnt < 0:
                return
            if len(path) > valid_len:
                return
            # pruning
            if st == N and len(path) == valid_len and left_cnt == 0:
                res.append(path)
                return

            if st >= N:
                return
            # remove duplicate
            """
            if s[ii] == path[-1]: must select
            else:
                select or not select
            """
            cc = s[st]
            if cc.isalpha():
                dfs(st+1, path+s[st], left_cnt)
            else:
                dfs(st+1, path+cc, left_cnt+(1 if cc == "(" else -1))
                if path == "" or cc != path[-1]:
                    dfs(st+1, path, left_cnt)

        path = ""
        dfs(0, path, 0)
        return res


####################################
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        1. from LC921, we know how to find out num of parentheses to remove
        2. from 1, we know the max len after removing the invalid parentheses. 
        3. DFS to find all strings with the pruning strategy to avoid duplicates

        """
        # figure out the max len -> figure out min to remove
        cnt = 0
        to_remove = 0

        N = len(s)
        for ii, cc in enumerate(s):
            if cc == "(":
                cnt += 1
            elif cc == ")":
                cnt -= 1
                if cnt < 0:
                    to_remove += 1
                    cnt = 0

        to_remove += cnt
        mxl = N-to_remove  # the max len of the valid parenthesis after removing min

        def dfs(ii, cnt, path):
            """
            ii: current index into s
            cnt: current unbalanced left-paren
            path: current output string
            """
            if cnt < 0:
                return
            if len(path) > mxl:
                return
            if ii == N:  # reached the end
                # if not remaining unbalanced left-paren
                if cnt == 0 and len(path) == mxl:
                    # and output string path==maxLen allowed
                    res.append(path)
                return

            if (s[ii] not in ["(", ")"]):
                dfs(ii+1, cnt, path+s[ii])
            else:
                # we always can select
                dfs(ii+1, cnt + (1 if s[ii] == "(" else -1), path+s[ii])
                # pruning strategy, we can only skip if not equal than prev or we are the first one
                if len(path) == 0 or s[ii] != path[-1]:
                    dfs(ii+1, cnt, path)

        res = []
        dfs(0, 0, "")

        return res
