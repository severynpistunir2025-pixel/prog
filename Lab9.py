def rabin_karp_all_occurrences(haystack: str, needle: str) -> list[int]:
    n = len(haystack)
    m = len(needle)
    
    if m == 0 or m > n:
        return []
    
    base = 256
    prime = 101
    indices = []
    
    needle_hash = 0
    window_hash = 0
    h = 1
    
    for i in range(m - 1):
        h = (h * base) % prime
        
    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % prime
        window_hash = (base * window_hash + ord(haystack[i])) % prime
        
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            if haystack[i:i+m] == needle:
                indices.append(i)
                
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % prime
            if window_hash < 0:
                window_hash += prime
                
    return indices