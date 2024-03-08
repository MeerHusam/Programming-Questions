def calculate_prefix_sequence(search_pattern):
    prefix_seq = [0] * len(search_pattern)
    length = 0
    for index in range(1, len(search_pattern)):
        while length > 0 and search_pattern[index] != search_pattern[length]:
            length = prefix_seq[length - 1]
        if search_pattern[index] == search_pattern[length]:
            length += 1
        prefix_seq[index] = length
    return prefix_seq

def pattern_search_kmp(search_pattern, main_text):
    prefix_sequence = calculate_prefix_sequence(search_pattern)
    search_results = []
    matched_length = 0
    for index in range(len(main_text)):
        while matched_length > 0 and main_text[index] != search_pattern[matched_length]:
            matched_length = prefix_sequence[matched_length - 1]
        if main_text[index] == search_pattern[matched_length]:
            matched_length += 1
        if matched_length == len(search_pattern):
            search_results.append(index - matched_length + 1)
            matched_length = prefix_sequence[matched_length - 1]
    return search_results

def continuous_search_mode():
    while True:
        try:
            user_pattern = input().strip()
            user_text = input().strip()
            found_matches = pattern_search_kmp(user_pattern, user_text)
            print(' '.join(map(str, found_matches)))
        except EOFError:
            break

continuous_search_mode()
