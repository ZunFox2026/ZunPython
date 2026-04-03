# Python 53: Xử Lý Danh Sách và Vòng Lặp Cơ Bản

## Giới thiệu

Trong lập trình Python, danh sách (list) và vòng lặp là hai khái niệm cơ bản nhưng cực kỳ quan trọng. Danh sách giúp lưu trữ nhiều giá trị trong một biến duy nhất, còn vòng lặp cho phép thực hiện lặp lại một khối lệnh nhiều lần. Bài học này sẽ giúp bạn làm quen với cách tạo danh sách, truy cập phần tử và sử dụng vòng lặp `for` để xử lý dữ liệu một cách hiệu quả.

## Lý thuyết

- **Danh sách (List)**: Là cấu trúc dữ liệu dùng để lưu trữ một dãy các phần tử, có thể thay đổi (mutable). Danh sách được khai báo bằng dấu ngoặc vuông `[]`, các phần tử cách nhau bằng dấu phẩy.
  
- **Vòng lặp `for`**: Dùng để duyệt qua các phần tử trong danh sách (hoặc các đối tượng có thể lặp được). Cú pháp:
  ```python
  for biến in danh_sách:
      # thực hiện lệnh
  ```

- Truy cập phần tử bằng chỉ số: Phần tử đầu tiên có chỉ số 0, phần tử cuối có chỉ số -1.

## Ví dụ

Dưới đây là ví dụ minh họa cách tạo danh sách và sử dụng vòng lặp `for` để in từng phần tử:

```python
# Tạo danh sách các tên học sinh
hoc_sinh = ["An", "Bình", "Chi", "Dũng"]

# Duyệt danh sách và in từng tên
print("Danh sách học sinh:")
for ten in hoc_sinh:
    print(ten)

# Truy cập phần tử theo chỉ số
print("\nHọc sinh đầu tiên:", hoc_sinh[0])
print("Học sinh cuối cùng:", hoc_sinh[-1])
```

**Kết quả:**
```
Danh sách học sinh:
An
Bình
Chi
Dũng

Học sinh đầu tiên: An
Học sinh cuối cùng: Dũng
```

## Bài tập

1. Tạo một danh sách chứa 5 số nguyên bất kỳ.
2. Sử dụng vòng lặp `for` để in ra từng số trong danh sách.
3. Tính và in tổng các số trong danh sách.
4. *(Nâng cao)*: In ra các số chẵn trong danh sách.

> Gợi ý: Dùng `sum()` để tính tổng, và toán tử `%` để kiểm tra số chẵn (ví dụ: `so % 2 == 0`).