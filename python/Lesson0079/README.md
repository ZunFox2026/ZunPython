# Tìm số chính phương
## Giới thiệu
Bài viết này sẽ hướng dẫn bạn cách tìm số chính phương bằng ngôn ngữ lập trình Python. Số chính phương là số có căn bậc hai là một số nguyên, tức là số có thể biểu diễn dưới dạng n^2, trong đó n là một số nguyên.

## Lý thuyết
Để tìm số chính phương, bạn có thể sử dụng công thức sau: 
- Nếu một số x có căn bậc hai là một số nguyên, thì x là một số chính phương.
- Ngược lại, nếu x là một số chính phương, thì căn bậc hai của x là một số nguyên.

Ví dụ, số 16 là một số chính phương vì căn bậc hai của 16 là 4, là một số nguyên. Ngược lại, số 20 không phải là một số chính phương vì căn bậc hai của 20 không phải là một số nguyên.

Trong Python, bạn có thể sử dụng hàm `math.sqrt()` để tính căn bậc hai của một số, và hàm `math.isclose()` để kiểm tra xem một số có gần bằng với một số nguyên hay không.

## Ví dụ
Dưới đây là một ví dụ về cách tìm số chính phương bằng Python:
```python
import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = math.sqrt(n)
    return math.isclose(sqrt, round(sqrt))

# Kiểm tra số 16
print(is_perfect_square(16))  # True

# Kiểm tra số 20
print(is_perfect_square(20))  # False
```
Trong ví dụ trên, hàm `is_perfect_square()` kiểm tra xem một số có phải là số chính phương hay không bằng cách tính căn bậc hai của số đó và kiểm tra xem nó có gần bằng với một số nguyên hay không.

## Bài tập
Bài tập cho bạn:
- Viết một chương trình Python để tìm tất cả số chính phương trong một phạm vi số cho trước.
- Ví dụ, nếu phạm vi số là từ 1 đến 100, chương trình sẽ tìm và in ra tất cả số chính phương trong phạm vi này.
- Gợi ý: bạn có thể sử dụng vòng lặp để kiểm tra từng số trong phạm vi, và sử dụng hàm `is_perfect_square()` để kiểm tra xem số đó có phải là số chính phương hay không.