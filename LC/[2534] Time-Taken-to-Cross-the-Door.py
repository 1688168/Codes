###############
# 20230926
###############

from collections import deque


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        """
        * n: (0, n-1) - number of person
        * 1 door
        * arrival[ii] - arrival time of person ii
        * state[ii] - (0-enter, 1-exit) person ii is enter or exit
        * prev_state
        * return answer[ii]: 
        """
        entering_pool = deque()
        exiting_pool = deque()
        N = len(arrival)
        ct = 0  # current time
        ii = 0
        prev_state = 1
        ans = [-1]*N

        def enter():
            nonlocal prev_state
            if len(entering_pool) > 0:
                idx = entering_pool.popleft()
                ans[idx] = ct
                prev_state = 0
            else:
                if len(exiting_pool) > 0:
                    exit()
                else:
                    prev_state = 1

        def exit():
            nonlocal prev_state
            if len(exiting_pool) > 0:
                idx = exiting_pool.popleft()
                ans[idx] = ct
                prev_state = 1
            else:
                if len(entering_pool) > 0:
                    enter()

        # need crossing time for each person, queue need to be empty @ the end
        while ii < N or entering_pool or exiting_pool:
            # enqueue all those @ door
            while ii < N and arrival[ii] <= ct:
                if state[ii] == 0:
                    entering_pool.append(ii)
                if state[ii] == 1:
                    exiting_pool.append(ii)
                ii += 1

            if prev_state == 0:
                enter()
            elif prev_state == 1:
                exit()

            ct += 1

        return ans


############################################


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        entering_pool = deque()
        existing_pool = deque()
        N = len(arrival)
        ans = [-1]*N
        prev_state = 1
        ct = 0
        ii = 0

        def entering():
            nonlocal prev_state
            curr = entering_pool.popleft()
            ans[curr] = ct
            prev_state = 0

        def existing():
            nonlocal prev_state
            curr = existing_pool.popleft()
            ans[curr] = ct
            prev_state = 1

        while ii < N or entering_pool or existing_pool:

            # get those at the door to the queue
            while ii < N and arrival[ii] <= ct:
                if state[ii] == 0:
                    entering_pool.append(ii)
                else:
                    existing_pool.append(ii)
                ii += 1

            if prev_state == 0:  # previously entering
                if entering_pool:
                    entering()
                    ct += 1
                    continue

                if existing_pool:
                    existing()
                    ct += 1
                    continue

                prev_state = 1

            else:  # previously existing
                # exit first
                if existing_pool:
                    existing()
                    ct += 1
                    continue
                if entering_pool:
                    entering()
                    ct += 1
                    continue

                prev_state = 1

            ct += 1
        return ans


################


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enter_pool, exit_pool = deque(), deque()
        cur_time = 0
        prev_state = 1
        i = 0
        ans = [0 for _ in range(len(arrival))]
        while i < len(arrival) or enter_pool or exit_pool:
            while i < len(arrival) and arrival[i] <= cur_time:
                if state[i] == 0:
                    enter_pool.append(i)
                else:
                    exit_pool.append(i)
                i += 1
            if prev_state == 1:
                if exit_pool:
                    ans[exit_pool.popleft()] = cur_time
                elif enter_pool:
                    ans[enter_pool.popleft()] = cur_time
                    prev_state = 0
            else:
                if enter_pool:
                    ans[enter_pool.popleft()] = cur_time
                elif exit_pool:
                    ans[exit_pool.popleft()] = cur_time
                    prev_state = 1
                else:
                    prev_state = 1
            cur_time += 1
        return ans
