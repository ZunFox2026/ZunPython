# Python 56: Lập Trình Cơ Bản Từ Con Số 0

## Giới thiệu

Chào mừng bạn đến với bài học thứ 56 trong chuỗi "Lập Trình Cơ Bản Từ Con Số 0" – một hành trình giúp người mới bắt đầu làm quen với ngôn ngữ Python một cách dễ hiểu và hiệu quả. Ở bài học này, chúng ta sẽ củng cố các kiến thức lập trình cơ bản như biến, kiểu dữ liệu, cấu trúc điều kiện và vòng lặp – những nền tảng quan trọng để bạn tự tin bước vào thế giới lập trình.

Dù bạn chưa từng viết một dòng code nào, hay chỉ mới biết chút ít về Python, bài học này sẽ giúp bạn hệ thống lại kiến thức và thực hành qua các ví dụ minh họa trực quan. Mục tiêu là giúp bạn hiểu được cách máy tính "suy nghĩ" và xử lý thông tin thông qua code.

## Lý thuyết

Trong Python, bạn bắt đầu bằng việc khai báo **biến** để lưu trữ dữ liệu. Các kiểu dữ liệu cơ bản gồm: `int` (số nguyên), `float` (số thực), `str` (chuỗi), và `bool` (đúng/sai).  

Cấu trúc điều kiện `if-elif-else` cho phép chương trình đưa ra quyết định dựa trên điều kiện. Ví dụ: kiểm tra một số là dương, âm hay bằng 0.

Vòng lặp `for` và `while` giúp lặp lại một đoạn code nhiều lần. Đây là công cụ mạnh để xử lý danh sách hoặc thực hiện các tác vụ lặp đi lặp lại.

## Ví dụ

Dưới đây là một chương trình nhỏ kiểm tra số chẵn/lẻ và in ra các số từ 1 đến 5:

```python
# Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))

# Kiểm tra chẵn lẻ
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")

# In các số từ 1 đến 5
print("Các số từ 1 đến 5:")
for i in range(1, 6):
    print(i)
```

## Bài tập

1. Viết chương trình nhập vào một số và in ra bình phương của số đó.  
2. Dùng vòng lặp `while`, in các số từ 10 về 1.  
3. Kiểm tra một số có chia hết cho cả 3 và 5 không, nếu có thì in "Chia hết cho 15".

Hãy thử tự viết code trước khi xem đáp án. Lập trình là kỹ năng – luyện tập chính là chìa khóa thành công!