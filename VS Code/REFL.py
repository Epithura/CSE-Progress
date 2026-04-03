def get_twice(n):
    return 2 * n

def get_thrice(n):
    return 3 * n

current = None

print("Enter a number, or type commands like ‘Get Twice’ / ‘Get Thrice’. Type ‘quit’ to exit.")
while True:
    cmd = input(">>> ").strip()
    if cmd.lower() in ("quit","exit"):
        break

    # If it's just a number, set current
    if cmd.isdigit():
        current = int(cmd)
        print(current)
        continue

    # If it's a Get-command, apply to current
    parts = cmd.split()
    if len(parts) >= 2 and parts[0].lower() == "get":
        if current is None:
            print("No current value yet. Enter a number first.")
            continue

        op = parts[1].lower()
        if op == "twice":
            current = get_twice(current)
        elif op == "thrice":
            current = get_thrice(current)
        else:
            print(f"Unknown operation: {parts[1]}")
            continue

        print(current)
        continue

    print("Unrecognized input. Enter a number or ‘Get Twice’ / ‘Get Thrice’.")