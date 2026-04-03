import sys

def query(i, x):
    print(f"? {i} {x}")
    sys.stdout.flush()
    b = int(input())
    if b == -1:
        exit()
    return b

t = int(input())
for _ in range(t):
    n = int(input())
    
    sum_known = 0
    seen_numbers = set()
    max_bits = n.bit_length()
    
    for i in range(1, n):
        val = 0
        for b in range(max_bits):
            bit_mask = 1 << b
            trial_val = val | bit_mask
            if trial_val in seen_numbers:
                continue
            res = query(i, bit_mask)
            if res == 1:
                val |= bit_mask
        seen_numbers.add(val)
        sum_known += val
    total_sum = n * (n + 1) // 2
    p_n = total_sum - sum_known
    print(f"! {p_n}")
    sys.stdout.flush()