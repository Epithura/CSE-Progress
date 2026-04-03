import sys

# Set up fast input reading
def input():
    return sys.stdin.readline().strip()

def solve():
    """
    Reads the array and determines the minimum number of elements to remove
    to make the remaining array "good."
    """
    try:
        # Read n, the number of elements
        n_str = input()
        if not n_str:
            return
        n = int(n_str)
    except EOFError:
        return
    except ValueError:
        return

    # Read the array elements
    try:
        a = list(map(int, input().split()))
    except EOFError:
        return
    except ValueError:
        # Handle cases where input line might be empty or malformed
        if n > 0:
            # If n > 0 but no elements were read, something is wrong, skip
            return
        a = []

    # Counters for odd and even elements
    count_odd = 0
    count_even = 0

    # The core logic: A good array can be formed by keeping only elements of
    # the same parity (all odd or all even). The maximum length good array
    # is achieved by choosing the parity with the higher count.
    for x in a:
        if x % 2 != 0:
            count_odd += 1
        else:
            count_even += 1

    # The maximum number of elements we can keep
    max_kept_elements = max(count_odd, count_even)

    # The minimum number of elements to remove is the total minus the maximum we keep
    min_removals = n - max_kept_elements

    print(min_removals)

def main():
    """
    Handles multiple test cases.
    """
    try:
        # Read the number of test cases t
        t_str = input()
        if not t_str:
            return
        t = int(t_str)
    except EOFError:
        return
    except ValueError:
        return

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()