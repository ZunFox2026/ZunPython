# Bài 20: Làm quen với thư viện Tkinter

# Import thư viện Tkinter
import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Làm quen với Tkinter")

# Tạo label
label = tk.Label(window, text="Xin chào, tôi là Tkinter!", font=("Arial", 20))
label.pack(pady=20)  # Thêm padding trên và dưới

# Tạo button
def click_button():
    print("Bạn đã nhấn nút!")
button = tk.Button(window, text="Nhấn tôi!", command=click_button)
button.pack(pady=10)  # Thêm padding trên và dưới

# Tạo entry
entry = tk.Entry(window, font=("Arial", 16), width=30)
entry.pack(pady=10)  # Thêm padding trên và dưới

# Tạo text box
text_box = tk.Text(window, font=("Arial", 16), width=40, height=5)
text_box.pack(pady=10)  # Thêm padding trên và dưới

# Tạo checkbox
def check_checkbox():
    if checkbox_var.get():
        print("Bạn đã chọn checkbox!")
    else:
        print("Bạn đã bỏ chọn checkbox!")
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Checkbox", variable=checkbox_var, command=check_checkbox)
checkbox.pack(pady=10)  # Thêm padding trên và dưới

# Tạo radio button
def select_radio():
    print("Bạn đã chọn:", radio_var.get())
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(window, text="Radio 1", variable=radio_var, value="Radio 1", command=select_radio)
radio2 = tk.Radiobutton(window, text="Radio 2", variable=radio_var, value="Radio 2", command=select_radio)
radio1.pack(pady=5)  # Thêm padding trên và dưới
radio2.pack(pady=5)  # Thêm padding trên và dưới

# Chạy ứng dụng
window.mainloop()