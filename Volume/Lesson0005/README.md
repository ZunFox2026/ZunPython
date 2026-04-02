# Xử lý chuỗi
## Giới thiệu
Xử lý chuỗi là một phần quan trọng trong lập trình Python. Chuỗi là một loại dữ liệu cơ bản trong Python, được sử dụng để lưu trữ và thao tác với văn bản. Trong bài này, chúng ta sẽ tìm hiểu về các phương thức và kỹ thuật xử lý chuỗi trong Python.

## Lý thuyết
Chuỗi trong Python được định nghĩa bằng cách đặt văn bản bên trong dấu ngoặc kép hoặc dấu ngoặc đơn. Ví dụ: "Xin chào" hoặc 'Xin chào'. Python cung cấp nhiều phương thức để xử lý chuỗi, bao gồm:
- `upper()`: Chuyển chuỗi sang chữ hoa
- `lower()`: Chuyển chuỗi sang chữ thường
- `strip()`: Loại bỏ khoảng trắng ở đầu và cuối chuỗi
- `split()`: Chia chuỗi thành danh sách các từ
- `join()`: Nối các từ trong danh sách thành một chuỗi

## Ví dụ
Ví dụ về xử lý chuỗi trong Python:
- Chuyển chuỗi sang chữ hoa: `"Xin chào".upper()` sẽ trả về `"XIN CHÀO"`
- Chuyển chuỗi sang chữ thường: `"XIN CHÀO".lower()` sẽ trả về `"xin chào"`
- Loại bỏ khoảng trắng: `"   Xin chào   ".strip()` sẽ trả về `"Xin chào"`
- Chia chuỗi thành danh sách các từ: `"Xin chào thế giới".split()` sẽ trả về `["Xin", "chào", "thế", "giới"]`
- Nối các từ trong danh sách thành một chuỗi: `"-".join(["Xin", "chào", "thế", "giới"])` sẽ trả về `"Xin-chào-thế-giới"`

## Bài tập
Bài tập về xử lý chuỗi:
- Viết một chương trình Python để chuyển đổi một chuỗi nhập vào từ người dùng sang chữ hoa và chữ thường.
- Viết một chương trình Python để loại bỏ khoảng trắng ở đầu và cuối một chuỗi nhập vào từ người dùng.
- Viết một chương trình Python để chia một chuỗi nhập vào từ người dùng thành danh sách các từ và in ra danh sách này.
- Viết một chương trình Python để nối các từ trong một danh sách nhập vào từ người dùng thành một chuỗi, với các từ được ngăn cách bởi dấu gạch chéo (`/`).