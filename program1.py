def is_accepted_by_dfa(binary_string):
    # DFA states: 0 (mod 3 == 0), 1 (mod 3 == 1), 2 (mod 3 == 2)
    state = 0  # Start in state 0

    for bit in binary_string:
        if bit not in '01':
            return False  # Reject non-binary strings
        if bit == '1':
            state = (state + 1) % 3
        # bit == '0' -> state remains the same

    return state == 0  # Accept only if final state is 0


# Test cases
test_strings = ["", "0", "1", "11", "111", "1101", "10101", "111111"]
for s in test_strings:
    result = is_accepted_by_dfa(s)
    print(f"String '{s}': {'Accepted' if result else 'Rejected'}")
