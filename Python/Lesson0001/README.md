# Bài 1: Làm Quen Với Python - In Dữ Liệu và Biến Đơn Giản

## Giới thiệu

Chào mừng bạn đến với bài học đầu tiên trong hành trình học lập trình Python! Python là một ngôn ngữ lập trình dễ học, dễ đọc và được sử dụng rộng rãi trong nhiều lĩnh vực như phát triển web, khoa học dữ liệu, trí tuệ nhân tạo,... Bài học này sẽ giúp bạn làm quen với cách in dữ liệu ra màn hình và sử dụng biến đơn giản – những nền tảng cơ bản nhất khi bắt đầu lập trình.

## Lý thuyết

Trong Python, để hiển thị dữ liệu ra màn hình, ta dùng hàm `print()`. Cú pháp rất đơn giản:

```python
print("Nội dung cần in")
```

Bạn có thể in chuỗi, số, hoặc giá trị của biến.  
Biến là nơi lưu trữ dữ liệu. Trong Python, bạn không cần khai báo kiểu dữ liệu, chỉ cần gán giá trị:

```python
ten_bien = giá_trị
```

Ví dụ:  
```python
ten = "An"
tuoi = 15
```

## Ví dụ

Dưới đây là một chương trình đơn giản minh họa việc in thông tin cá nhân:

```python
# Gán giá trị cho các biến
ho_ten = "Nguyễn Văn Bình"
lop = "8A"
diem_toan = 9.5

# In thông tin ra màn hình
print("Họ và tên:", ho_ten)
print("Lớp:", lop)
print("Điểm Toán:", diem_toan)
```

Kết quả khi chạy chương trình:
```
Họ và tên: Nguyễn Văn Bình
Lớp: 8A
Điểm Toán: 9.5
```

## Bài tập

1. Viết chương trình in ra tên, tuổi và sở thích của bạn.
2. Tạo hai biến `a = 10` và `b = 20`, sau đó in tổng của hai số này ra màn hình (sử dụng `print(a + b)`).
3. Thử thay đổi giá trị của một biến rồi in lại – quan sát kết quả.

> 💡 Gợi ý: Hãy thực hành trên trình soạn thảo Python (như IDLE, Thonny, hoặc Google Colab) để làm quen với cú pháp và môi trường lập trình.