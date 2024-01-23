def kmp_search(haystack, needle):
    n = len(haystack)
    m = len(needle)
    if m == 0:
        return [i for i in range(n + 1)]

    prefix_table = build_prefix_table(needle)
    occurrences = []

    j = 0
    for i in range(n):
        while j > 0 and haystack[i] != needle[j]:
            j = prefix_table[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)
            j = prefix_table[j - 1]

    return occurrences


def build_prefix_table(pattern):
    m = len(pattern)
    prefix_table = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j
    return prefix_table
