################
# 220231007
################
from collections import deque


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        """
        - when we need to queue up -> priority_queue (deque)
        """
        entering_pool = collections.deque()
        exiting_pool = collections.deque()
        t = 0  # current time
        ii = 0  # the iith persion

        N = len(arrival)
        ans = [0] * N

        prev = 1  # default to exiting

        def process_exiting(curr_t, ii):
            nonlocal prev
            if exiting_pool:
                ans[exiting_pool.popleft()] = curr_t
                prev = 1
            else:
                if entering_pool:
                    process_entering(curr_t, ii)

        def process_entering(curr_t, ii):
            nonlocal prev
            if entering_pool:
                ans[entering_pool.popleft()] = curr_t
                prev = 0
            else:
                if exiting_pool:
                    process_exiting(curr_t, ii)
                else:
                    prev = 1

        while ii < N or entering_pool or exiting_pool:
            # get qualified persons enque
            while ii < N and arrival[ii] <= t:
                if state[ii] == 0:
                    entering_pool.append(ii)
                else:
                    exiting_pool.append(ii)
                ii += 1

            curr_t = t
            curr_ii = ii
            t += 1

            if prev == 1:
                # processing exit first
                process_exiting(curr_t, curr_ii)
                continue

            if prev == 0:
                process_entering(curr_t, curr_ii)
                continue

        return ans


###############
# 20230926
###############


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
