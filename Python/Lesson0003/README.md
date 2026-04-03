# Bài 1: Làm Quen Với Python - In Dữ Liệu Và Biến Đơn Giản

## Giới thiệu

Trong bài học đầu tiên này, bạn sẽ được làm quen với ngôn ngữ lập trình Python — một ngôn ngữ phổ biến, dễ học và mạnh mẽ. Bạn sẽ bắt đầu với việc in dữ liệu ra màn hình và sử dụng biến đơn giản để lưu trữ thông tin. Đây là nền tảng quan trọng giúp bạn tiếp tục học các khái niệm phức tạp hơn trong lập trình.

## Lý thuyết

Trong Python, để in dữ liệu ra màn hình, ta sử dụng lệnh `print()`. Bên trong dấu ngoặc, bạn có thể đặt chuỗi ký tự (được bao bởi dấu nháy kép `"` hoặc nháy đơn `'`), số, hoặc biến.

Biến là một tên gọi dùng để lưu trữ giá trị. Trong Python, bạn không cần khai báo kiểu dữ liệu cho biến — Python tự động nhận diện kiểu dựa trên giá trị gán. Cú pháp gán giá trị cho biến là: `tên_biến = giá_trị`.

Ví dụ:
```python
ten = "An"
tuoi = 12
```

## Ví dụ

Dưới đây là một chương trình Python đơn giản in lời chào và thông tin cá nhân:

```python
# In dữ liệu ra màn hình
print("Xin chào các bạn!")
print("Mình tên là Python.")

# Sử dụng biến
ten = "Lan"
tuoi = 10
print("Tên tôi là", ten)
print("Tôi", tuoi, "tuổi.")
```

Kết quả khi chạy chương trình:
```
Xin chào các bạn!
Mình tên là Python.
Tên tôi là Lan
Tôi 10 tuổi.
```

## Bài tập

1. Viết chương trình in ra dòng: `Chào mừng bạn đến với thế giới lập trình!`
2. Tạo hai biến: `ho_ten` (họ tên của bạn) và `lop` (lớp bạn đang học), sau đó in ra thông tin theo mẫu:
   ```
   Tôi tên là [ho_ten], hiện đang học lớp [lop].
   ```
3. Thử in ra kết quả của phép tính `5 + 3` bằng cách sử dụng `print(5 + 3)`.

> Gợi ý: Nhớ dùng dấu phẩy hoặc nối chuỗi với `+` (nếu là chuỗi) để kết hợp văn bản và biến khi in.