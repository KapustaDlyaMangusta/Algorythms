import math


def calc_square_side(N, W, H):
    n_sqrt = math.sqrt(N)
    min_in_row = math.floor(n_sqrt)

    if abs(n_sqrt - min_in_row) == 0:
        return min_in_row * max(W, H)

    if W == H:
        return W * min_in_row + W

    if min_in_row == 1:
        return min(W, H) * N

    return max(W, H) * min_in_row


def calc_square_side_binary(N, W, H):
    left, right = max(W, H), max(W, H) * N

    counter = 0

    while left < right:
        counter = counter + 1

        mid = (left + right) // 2

        per_row = mid // W
        per_column = mid // H
        total_sheets = per_row * per_column

        if total_sheets >= N:
            right = mid
        else:
            left = mid + 1

    return left, counter


if __name__ == "__main__":
    N, W, H = 9000000, 1_000_000_000, 999_999_999
    print(calc_square_side_binary(N, W, H))
