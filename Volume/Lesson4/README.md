# Tìm số nguyên tố
## Giới thiệu
Số nguyên tố là một số tự nhiên lớn hơn 1, chỉ có hai ước là 1 và chính nó. Bài viết này sẽ giới thiệu về cách tìm số nguyên tố bằng ngôn ngữ lập trình Python. Đây là một chủ đề cơ bản nhưng rất quan trọng trong lĩnh vực toán học và lập trình.

## Lý thuyết
Một số được coi là nguyên tố nếu nó thỏa mãn các điều kiện sau:
- Là số tự nhiên lớn hơn 1.
- Chỉ có hai ước là 1 và chính nó.
Ví dụ, số 5 là số nguyên tố vì chỉ có hai ước là 1 và 5. Ngược lại, số 6 không phải là số nguyên tố vì ngoài 1 và 6, nó còn có thể chia hết cho 2 và 3.

Để kiểm tra một số có phải là nguyên tố hay không, chúng ta có thể sử dụng thuật toán đơn giản sau:
- Kiểm tra số đó có chia hết cho bất kỳ số nào từ 2 đến căn bậc hai của số đó hay không.
- Nếu số đó không chia hết cho bất kỳ số nào trong范围 trên, thì nó là số nguyên tố.

## Ví dụ
Dưới đây là ví dụ về cách kiểm tra số nguyên tố bằng Python:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ví dụ sử dụng
print(is_prime(5))  # True
print(is_prime(6))  # False
```
Trong ví dụ trên, hàm `is_prime(n)` kiểm tra số `n` có phải là nguyên tố hay không. Hàm này sử dụng vòng lặp để kiểm tra số `n` có chia hết cho bất kỳ số nào từ 2 đến căn bậc hai của `n` hay không.

## Bài tập
Bài tập này yêu cầu bạn viết một chương trình Python để tìm tất cả các số nguyên tố trong phạm vi từ 1 đến 100. Chương trình nên sử dụng hàm `is_prime(n)` đã được định nghĩa ở trên.
- Đầu tiên, bạn cần viết hàm `find_primes(limit)` để tìm tất cả các số nguyên tố trong phạm vi từ 1 đến `limit`.
- Sau đó, bạn cần sử dụng hàm `find_primes(limit)` để tìm tất cả các số nguyên tố trong phạm vi từ 1 đến 100 và in kết quả ra màn hình.
- Ngoài ra, bạn có thể mở rộng chương trình để cho phép người dùng nhập phạm vi tìm kiếm và in ra các số nguyên tố trong phạm vi đó.