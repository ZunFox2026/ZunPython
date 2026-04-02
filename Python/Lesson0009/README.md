# README – Bài 9 (Cấp Cơ bản)

## Giới thiệu
Bài 9 là bài tập thực hành phần **Cơ bản** của khóa học Python. Mục tiêu của bài là giúp sinh viên nắm vững các khái niệm về **xử lý chuỗi và vòng lặp**, đồng thời biết cách áp dụng chúng vào các bài toán thực tế như kiểm tra palindrome, đếm ký tự đặc biệt, và chuyển đổi định dạng dữ liệu. Sau khi hoàn thành bài này, bạn sẽ có thể:

- Viết hàm xử lý chuỗi đơn giản và linh hoạt.
- Sử dụng các phương pháp tích hợp của Python (`str` methods) để tối ưu mã.
- Thiết kế các bài tập nhỏ để củng cố kiến thức luồng điều kiện và vòng lặp.

## Lý thuyết
### 1. Chuỗi trong Python
- Chuỗi (`str`) là một dãy không thể thay đổi của ký tự Unicode.
- Các thao tác phổ biến: indexing (`s[i]`), slicing (`s[start:stop:step]`), concatenation (`+`), và replication (`*`).  
- Một số phương thức hữu ích:
  - `s.lower()`, `s.upper()`, `s.title()` – đổi hoa/thường.
  - `s.strip()`, `s.lstrip()`, `s.rstrip()` – loại bỏ khoảng trắng.
  - `s.split(sep=None)` – tách chuỗi thành danh sách.
  - `s.join(iterable)` – ghép danh sách thành chuỗi.
  - `s.find(sub)`, `s.count(sub)` – tìm kiếm và đếm.
  - `s.isdigit()`, `s.isalpha()`, `s.isalnum()` – kiểm tra loại ký tự.

### 2. Vòng lặp và điều kiện
- `for` duyệt qua từng phần tử của một iterable (chuỗi, list, range…).
- `while` lặp finché điều kiện còn đúng.
- Cấu trúc `if‑elif‑else` để ra quyết định dựa trên kết quả kiểm tra.

### 3. Kết hợp chuỗi và vòng lặp
Thường ta sẽ duyệt qua mỗi ký tự của chuỗi để:
- Đếm số lần xuất hiện của một ký tự hoặc nhóm ký tự.
- Kiểm tra tính đối xứng (palindrome).
- Thay đổi hoặc lọc ký tự theo điều kiện nhất định.

## Ví dụ
Dưới đây là hàm kiểm tra xem một chuỗi có phải là **palindrome** (đọc ngược vẫn như cũ) sau khi bỏ qua khoảng trắng và không phân biệt hoa/thường.

```python
def is_palindrome(s: str) -> bool:
    """
    Trả về True nếu s là palindrome, ngược lại False.
    Bỏ qua khoảng trắng và không phân biệt hoa/thường.
    """
    # Chuẩn hoá: bỏ khoảng trắng và chuyển thành chữ thường
    cleaned = ''.join(ch.lower() for ch in s if not ch.isspace())
    # So sánh chuỗi với chuỗi ngược lại
    return cleaned == cleaned[::-1]


# Minh họa
if __name__ == "__main__":
    test_cases = [
        "A man a plan a canal Panama",
        "Hello world",
        "Was it a car or a cat I saw",
        "",
        "12321"
    ]
    for case in test_cases:
        print(f'"{case}" -> {is_palindrome(case)}')
```

**Giải thích**
- List comprehension `''.join(ch.lower() for ch in s if not ch.isspace())` tạo ra chuỗi đã được chuẩn hoá.
- `cleaned[::-1]` là cách nhanh để đảo ngược chuỗi bằng slicing.
- Hàm trả về giá trị Boolean, dễ dàng dùng trong các điều kiện `if`.

## Bài tập
1. **Đếm tần suất ký tự**