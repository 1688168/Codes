class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook = [a, b]
        bishop = [c, d]
        queen = [e, f]
        rook_move = math.inf
        bishop_move = math.inf

        def is_rook_in_btn(r, b, q):
            # is in the range
            if r[0] < min(b[0], q[0]) or r[0] > max(b[0], q[0]):
                return False
            if r[1] < min(b[1], q[1]) or r[1] > max(b[1], q[1]):
                return False

            if r[1] == q[1] or b[1] == q[1]:
                return False

            # is on diagnol
            return (r[0]-q[0])/(r[1]-q[1]) == (b[0]-q[0])/(b[1]-q[1])

        def is_bishop_in_btn(r, b, q):

            if r[0] == b[0] == q[0] and b[1] < max(r[1], q[1]) and b[1] > min(r[1], q[1]):
                return True
            if r[1] == b[1] == q[1] and b[0] < max(r[0], q[0]) and b[0] > min(r[0], q[0]):
                return True

            return False


#         print(" is bishop in btn: ", is_bishop_in_btn(rook, bishop, queen))
#         print(" is rook in btn: ", is_rook_in_btn(rook, bishop, queen))

        # rook
        if ((a == e or b == f) and not is_bishop_in_btn(rook, bishop, queen)):
            return 1

        # bishop
        if abs(d-f) == abs(c-e) and not is_rook_in_btn(rook, bishop, queen):
            return 1

        return 2
