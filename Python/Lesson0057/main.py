from functools import lru_cache
import time

# ------------------- VÍ DỤ 1: Fibonacci với và không dùng lru_cache -------------------

# Fibonacci không dùng cache - chậm với n lớn
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# Fibonacci dùng lru_cache - tối ưu hóa mạnh
@lru_cache(maxsize=None)
def fibonacci_fast(n):
    if n <= 1:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

# Đo thời gian thực thi
print("Đang đo thời gian tính Fibonacci(35)...")

start = time.time()
result_slow = fibonacci_slow(35)
duration_slow = time.time() - start

start = time.time()
result_fast = fibonacci_fast(35)
duration_fast = time.time() - start

print(f"Kết quả (slow): {result_slow}, Thời gian: {duration_slow:.4f}s")
print(f"Kết quả (fast): {result_fast}, Thời gian: {duration_fast:.4f}s")
print()

# ------------------- VÍ DỤ 2: Số cách đi lên cầu thang -------------------
# Một người có thể đi 1 hoặc 2 bước. Đếm số cách lên bậc n.
@lru_cache(maxsize=None)
def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n-1) + count_ways(n-2)

print("Số cách đi lên các bậc cầu thang:")
for i in range(1, 11):
    print(f"Bậc {i}: {count_ways(i)} cách")
print()

# ------------------- VÍ DỤ 3: Độ dài dãy con chung lớn nhất (LCS) -------------------
# Tìm độ dài dãy con chung lớn nhất của hai chuỗi
@lru_cache(maxsize=None)
def lcs_length(s1, s2):
    if not s1 or not s2:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + lcs_length(s1[:-1], s2[:-1])
    else:
        return max(lcs_length(s1[:-1], s2), lcs_length(s1, s2[:-1]))

str1 = "ABAZDC"
str2 = "BACBAD"
lcs_len = lcs_length(str1, str2)
print(f"Độ dài dãy con chung lớn nhất của '{str1}' và '{str2}' là: {lcs_len}")
print("Cache info:", lcs_length.cache_info())

# Xóa cache nếu cần
# lcs_length.cache_clear()