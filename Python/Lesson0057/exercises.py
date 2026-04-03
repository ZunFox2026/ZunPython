####################
# BÀI TẬP THỰC HÀNH
####################

# Bài 1: Viết hàm tính giai thừa đệ quy với @lru_cache
# So sánh tốc độ với hàm không dùng cache

def factorial_slow(n):
    # TODO: Viết hàm giai thừa đệ quy không dùng cache
    pass

# TODO: Viết hàm factorial_fast với @lru_cache

# Bài 2: Đếm số cách phân tích số n thành tổng các số nguyên dương ≥ 1
# Các cách phân tích không phân biệt thứ tự (ví dụ: 3 = 1+2 và 2+1 là giống nhau)
# Gợi ý: Dùng tham số max_num để đảm bảo thứ tự không giảm

def count_partitions(n, max_num):
    # TODO: Viết hàm đệ quy và dùng @lru_cache
    pass

# Bài 3: Tìm số lượng cách tạo chuỗi đối xứng từ một chuỗi có ký tự thay thế
# Giả sử mỗi vị trí có thể chọn một trong hai ký tự cho trước
# Ví dụ: positions = [('a','b'), ('c','d')] -> tạo chuỗi 2 ký tự, kiểm tra xem có bao nhiêu cách tạo thành đối xứng

def count_palindromic_choices(choices):
    # TODO: Viết hàm dùng @lru_cache để đếm số cách tạo chuỗi đối xứng
    # Gợi ý: Dùng tham số là chỉ số bắt đầu và kết thúc
    pass

# Bài 4: Maximum Subarray bằng đệ quy và @lru_cache
# Cho danh sách số, tìm tổng lớn nhất của một dãy con liên tiếp
# Gợi ý: Xét tất cả các cặp (i, j), hoặc dùng chia để trị

def max_subarray_sum(arr, start, end):
    # TODO: Viết hàm đệ quy tìm tổng lớn nhất của dãy con từ start đến end
    pass

# Bài 5: Kiểm tra có thể chia danh sách thành 2 nhóm có tổng bằng nhau không?
# (Partition Problem)
# Gợi ý: Dùng đệ quy với tổng mục tiêu là total_sum // 2, và dùng @lru_cache với tham số (index, current_sum)

def can_partition(nums, index, target_sum, current_sum):
    # TODO: Viết hàm kiểm tra khả năng phân nhóm
    pass