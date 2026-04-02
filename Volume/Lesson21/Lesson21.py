# Bài 21: Làm quen với thư viện Tkinter

# Thư viện Tkinter là một thư viện tạo giao diện đồ họa người dùng (GUI) trong Python
import tkinter as tk

# Tạo một cửa sổ chính (root window)
root = tk.Tk()
# Đặt tiêu đề cho cửa sổ
root.title("Làm quen với Tkinter")

# Tạo một nhãn (label) hiển thị văn bản
label = tk.Label(root, text="Xin chào, tôi là Tkinter!")
# Thêm nhãn vào cửa sổ
label.pack()

# Tạo một nút (button) để người dùng tương tác
button = tk.Button(root, text="Nhấn vào đây", command=lambda: print("Bạn đã nhấn nút!"))
# Thêm nút vào cửa sổ
button.pack()

# Tạo một trường nhập văn bản (entry) để người dùng nhập dữ liệu
entry = tk.Entry(root)
# Thêm trường nhập vào cửa sổ
entry.pack()

# Tạo một nút để lấy dữ liệu từ trường nhập
get_button = tk.Button(root, text="Lấy dữ liệu", command=lambda: print("Dữ liệu nhập:", entry.get()))
# Thêm nút vào cửa sổ
get_button.pack()

# Tạo một Text Box để nhập nhiều dòng văn bản
text_box = tk.Text(root, height=5, width=30)
# Thêm Text Box vào cửa sổ
text_box.pack()

# Tạo một nút để lấy dữ liệu từ Text Box
get_text_button = tk.Button(root, text="Lấy dữ liệu từ Text Box", command=lambda: print("Dữ liệu nhập:\n", text_box.get("1.0", tk.END)))
# Thêm nút vào cửa sơ
get_text_button.pack()

# Chạy chương trình
root.mainloop()