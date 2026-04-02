<div align="center">
  <img src="image/zunny.png" alt="Zunny" width="160" style="border-radius: 50%; box-shadow: 0 12px 30px rgba(0,0,0,0.25);">

  # ☁️ ZunSchool – Học lập trình cùng Zunny

  **Lộ trình học lập trình miễn phí · Từ zero đến hero · Dự án mã nguồn mở của Zun Technologies**

  ![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![HTML](https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS](https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
  ![C++](https://img.shields.io/badge/C++-17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)
  ![Status](https://img.shields.io/badge/Trạng%20thái-Đang%20phát%20triển-orange?style=for-the-badge)

</div>

---

## 📖 Giới thiệu

**ZunSchool** là nền tảng học lập trình miễn phí, mã nguồn mở, được xây dựng bởi **Zun Technologies** và dẫn dắt bởi **Zunny** – chú cáo công nghệ bé nhỏ nhưng đầy nhiệt huyết! 🦊

Dù bạn là người **chưa biết gì** về lập trình hay đã có kiến thức nền tảng muốn **đi sâu hơn**, ZunSchool có lộ trình phù hợp cho bạn – với 4 khoá học được thiết kế bài bản, ví dụ thực tế và dự án cuối khoá.

> *"Lập trình không khó, chỉ cần bạn bắt đầu đúng chỗ – và Zunny luôn ở đây!"* 🦊☁️

---

## 🎓 Các khoá học

| Khoá | Ngôn ngữ | Cấp độ | Số bài | Trạng thái |
|------|----------|--------|--------|------------|
| 🐍 | Python | Cơ bản → Nâng cao | 22 bài | ✅ Hoàn thành |
| 🌐 | HTML | Cơ bản → Trung cấp | 18 bài | ✅ Hoàn thành |
| 🎨 | CSS | Cơ bản → Nâng cao | 20 bài | 🔄 Đang cập nhật |
| ⚙️ | C++ | Cơ bản → Trung cấp | 20 bài | 🔄 Đang cập nhật |

---

## 🐍 Khoá Python

> Ngôn ngữ đa năng – từ automation, web, AI đến data science.

### Bạn sẽ học được gì?

- ✅ Cú pháp Python từ cơ bản đến nâng cao
- ✅ Cấu trúc dữ liệu: list, tuple, dict, set
- ✅ Lập trình hướng đối tượng (OOP)
- ✅ Xử lý file & ngoại lệ
- ✅ Làm việc với API và JSON
- ✅ Tự động hóa tác vụ
- ✅ Xây dựng ứng dụng CLI, web scraper đơn giản

### 📚 Nội dung bài học

| Bài | Chủ đề | Code mẫu |
|-----|--------|----------|
| 00 | Hello World & cài đặt | `print("Hello Zunny!")` |
| 01 | Biến, kiểu dữ liệu | `name = "Zunny"; age = 3` |
| 02 | Nhập/xuất dữ liệu | `input("Tên bạn: ")` |
| 03 | Câu lệnh rẽ nhánh | `if, elif, else` |
| 04 | Vòng lặp | `for, while` |
| 05 | Hàm cơ bản | `def chao():` |
| 06 | List, Tuple | `my_list = [1,2,3]` |
| 07 | Dict, Set | `{"key": "value"}` |
| 08 | Xử lý chuỗi nâng cao | `split(), join(), strip()` |
| 09 | Đọc/ghi file | `open(), read(), write()` |
| 10 | Xử lý ngoại lệ | `try/except/finally` |
| 11 | Module và Package | `import math` |
| 12 | OOP – Class & Object | `class Zunny:` |
| 13 | Kế thừa, đa hình | `class ConCa(Zunny):` |
| 14 | Decorator | `@staticmethod` |
| 15 | Generator | `yield` |
| 16 | Làm việc với JSON | `json.loads()` |
| 17 | Gọi API bằng requests | `requests.get()` |
| 18 | Web scraping cơ bản | `BeautifulSoup` |
| 19 | Tự động hóa file/thư mục | `os, shutil` |
| 20 | Dự án 1: Todo CLI | `todo.py` |
| 21 | Dự án 2: Quản lý sinh viên | `student_manager.py` |
| 22 | Dự án 3: Lấy tỷ giá USD | `exchange_rate.py` |

### 💻 Code mẫu nổi bật

**Đọc file & xử lý ngoại lệ:**
```python
try:
    with open('data.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Không tìm thấy file!")
except Exception as e:
    print(f"Lỗi: {e}")
```

**Lớp Zunny đơn giản (OOP):**
```python
class Zunny:
    def __init__(self, name):
        self.name = name

    def teach(self, lesson):
        print(f"🦊 {self.name} đang dạy: {lesson}")

    def say_hello(self):
        return f"Xin chào, mình là {self.name}!"

z = Zunny("Zunny")
print(z.say_hello())
z.teach("Python OOP")
```

**Gọi API:**
```python
import requests

response = requests.get('https://api.github.com/repos/ZunFox20/ZunSchool')
if response.status_code == 200:
    data = response.json()
    print(f"Stars: {data['stargazers_count']}")
else:
    print("Gọi API thất bại")
```

---

## 🌐 Khoá HTML

> Nền tảng của mọi trang web – học đúng từ đầu để không phải học lại.

### Bạn sẽ học được gì?

- ✅ Cấu trúc tài liệu HTML5 chuẩn
- ✅ Các thẻ văn bản, tiêu đề, danh sách
- ✅ Link, ảnh, video, audio
- ✅ Bảng (table) và biểu mẫu (form)
- ✅ Semantic HTML: `<header>`, `<main>`, `<section>`, `<footer>`
- ✅ Accessibility cơ bản (alt, label, aria)
- ✅ Dự án: Trang cá nhân đơn giản

### 📚 Nội dung bài học

| Bài | Chủ đề | Ví dụ |
|-----|--------|-------|
| 00 | Cấu trúc HTML5 cơ bản | `<!DOCTYPE html>` |
| 01 | Tiêu đề, đoạn văn | `<h1>`, `<p>` |
| 02 | Định dạng văn bản | `<b>`, `<i>`, `<u>`, `<mark>` |
| 03 | Danh sách | `<ul>`, `<ol>`, `<li>` |
| 04 | Liên kết & điều hướng | `<a href="">` |
| 05 | Hình ảnh | `<img src="" alt="">` |
| 06 | Video & Audio | `<video>`, `<audio>` |
| 07 | Bảng dữ liệu | `<table>`, `<tr>`, `<td>` |
| 08 | Biểu mẫu cơ bản | `<form>`, `<input>` |
| 09 | Các loại input | `text, email, password, radio` |
| 10 | Select, Textarea | `<select>`, `<option>` |
| 11 | Semantic HTML5 | `<header>`, `<nav>`, `<main>` |
| 12 | `<div>` và `<span>` | Layout cơ bản |
| 13 | Meta tags & SEO cơ bản | `<meta name="description">` |
| 14 | Favicon & Open Graph | `<link rel="icon">` |
| 15 | Nhúng bản đồ / YouTube | `<iframe>` |
| 16 | Accessibility cơ bản | `alt`, `label`, `aria-*` |
| 17 | Dự án 1: Trang cá nhân | `profile.html` |
| 18 | Dự án 2: Trang sản phẩm | `product.html` |

### 💻 Code mẫu nổi bật

**Cấu trúc trang chuẩn:**
```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Trang của Zunny</title>
</head>
<body>
  <header>
    <h1>☁️ Xin chào từ ZunSchool!</h1>
    <nav>
      <a href="#about">Giới thiệu</a> |
      <a href="#contact">Liên hệ</a>
    </nav>
  </header>
  <main>
    <p>Học HTML cùng Zunny – dễ hơn bạn nghĩ! 🦊</p>
  </main>
  <footer>
    <p>© 2026 Zun Technologies</p>
  </footer>
</body>
</html>
```

---

## 🎨 Khoá CSS

> Biến trang HTML trần trụi thành giao diện đẹp mắt, chuyên nghiệp.

### Bạn sẽ học được gì?

- ✅ Selectors, specificity, cascade
- ✅ Box model: margin, padding, border
- ✅ Typography: font, size, weight, spacing
- ✅ Màu sắc, gradient, background
- ✅ Flexbox layout
- ✅ CSS Grid layout
- ✅ Responsive design & media queries
- ✅ Animations & transitions
- ✅ CSS variables & custom properties
- ✅ Dự án: Landing page responsive

### 📚 Nội dung bài học

| Bài | Chủ đề | Ví dụ |
|-----|--------|-------|
| 00 | Cú pháp CSS, cách nhúng | `<link rel="stylesheet">` |
| 01 | Selectors cơ bản | `*`, `.class`, `#id`, `element` |
| 02 | Màu sắc & Background | `color`, `background-color` |
| 03 | Text & Typography | `font-size`, `font-family` |
| 04 | Box Model | `margin`, `padding`, `border` |
| 05 | Display & Visibility | `block`, `inline`, `none` |
| 06 | Position | `static`, `relative`, `absolute`, `fixed` |
| 07 | Flexbox cơ bản | `display: flex` |
| 08 | Flexbox nâng cao | `align-items`, `justify-content` |
| 09 | CSS Grid cơ bản | `display: grid` |
| 10 | CSS Grid nâng cao | `grid-template-columns` |
| 11 | Responsive & Media Queries | `@media (max-width: 768px)` |
| 12 | Pseudo-class & Pseudo-element | `:hover`, `::before` |
| 13 | Transition | `transition: all 0.3s ease` |
| 14 | Animation | `@keyframes`, `animation` |
| 15 | CSS Variables | `--primary-color: #6c63ff` |
| 16 | Dark Mode | `@media (prefers-color-scheme: dark)` |
| 17 | Glassmorphism & modern effects | `backdrop-filter: blur()` |
| 18 | Dự án 1: Card component | `card.css` |
| 19 | Dự án 2: Navbar responsive | `navbar.css` |
| 20 | Dự án 3: Landing page | `landing.css` |

### 💻 Code mẫu nổi bật

**CSS Variables + Flexbox:**
```css
:root {
  --primary: #6c63ff;
  --bg: #0d0d0d;
  --text: #f0f0f0;
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Segoe UI', sans-serif;
}

.card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  border-radius: 12px;
  background: rgba(255,255,255,0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.1);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
}
```

---

## ⚙️ Khoá C++

> Ngôn ngữ nền tảng – hiểu C++ là hiểu máy tính thực sự hoạt động như thế nào.

### Bạn sẽ học được gì?

- ✅ Cú pháp C++ và cấu trúc chương trình
- ✅ Kiểu dữ liệu, biến, hằng số
- ✅ Toán tử, điều kiện, vòng lặp
- ✅ Hàm, đệ quy
- ✅ Mảng, chuỗi, con trỏ
- ✅ Lập trình hướng đối tượng (OOP)
- ✅ STL: vector, map, set
- ✅ Dự án: Quản lý danh sách sinh viên

### 📚 Nội dung bài học

| Bài | Chủ đề | Ví dụ |
|-----|--------|-------|
| 00 | Hello World & cài đặt | `cout << "Hello Zunny!";` |
| 01 | Biến và kiểu dữ liệu | `int, float, char, bool` |
| 02 | Nhập/xuất dữ liệu | `cin`, `cout` |
| 03 | Toán tử | `+, -, *, /, %, ++` |
| 04 | Câu lệnh điều kiện | `if, else if, switch` |
| 05 | Vòng lặp | `for, while, do-while` |
| 06 | Hàm cơ bản | `int add(int a, int b)` |
| 07 | Đệ quy | `factorial(n)` |
| 08 | Mảng 1 chiều | `int arr[5] = {1,2,3,4,5}` |
| 09 | Mảng 2 chiều | `int matrix[3][3]` |
| 10 | Chuỗi (string) | `#include <string>` |
| 11 | Con trỏ cơ bản | `int* p = &x` |
| 12 | Tham chiếu (reference) | `int& ref = x` |
| 13 | OOP – Class & Object | `class Zunny {}` |
| 14 | Constructor & Destructor | `Zunny() {}` |
| 15 | Kế thừa (Inheritance) | `class Fox : public Animal` |
| 16 | Đa hình (Polymorphism) | `virtual void speak()` |
| 17 | STL – Vector | `vector<int> v` |
| 18 | STL – Map & Set | `map<string, int>` |
| 19 | Dự án 1: Máy tính đơn giản | `calculator.cpp` |
| 20 | Dự án 2: Quản lý sinh viên | `student_manager.cpp` |

### 💻 Code mẫu nổi bật

**Class và OOP:**
```cpp
#include <iostream>
#include <string>
using namespace std;

class Zunny {
private:
    string name;
    int level;

public:
    Zunny(string n, int l) : name(n), level(l) {}

    void introduce() {
        cout << "🦊 Tôi là " << name
             << ", cấp độ " << level << endl;
    }

    void teach(string topic) {
        cout << name << " đang dạy: " << topic << endl;
    }
};

int main() {
    Zunny z("Zunny", 99);
    z.introduce();
    z.teach("C++ OOP");
    return 0;
}
```

**STL Vector:**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> scores = {85, 92, 78, 95, 88};

    sort(scores.begin(), scores.end(), greater<int>());

    cout << "Điểm cao nhất: " << scores[0] << endl;
    cout << "Tổng số học sinh: " << scores.size() << endl;

    for (int s : scores)
        cout << s << " ";

    return 0;
}
```

---

## 🚀 Bắt đầu nhanh

```bash
# Clone repository
git clone https://github.com/ZunFox20/ZunSchool.git
cd ZunSchool

# --- Python ---
python courses/python/lessons/00_hello_world.py

# --- C++ (cần g++ hoặc MinGW) ---
g++ courses/cpp/lessons/00_hello_world.cpp -o hello
./hello

# --- HTML & CSS ---
# Mở trực tiếp bằng trình duyệt
open courses/html/lessons/00_structure.html
```

> **Yêu cầu:**
> - Python: 3.8+ – tải tại [python.org](https://python.org)
> - C++: g++ (Linux/macOS) hoặc MinGW (Windows)
> - HTML/CSS: Trình duyệt bất kỳ + VS Code (khuyến nghị)

---

## 📂 Cấu trúc thư mục

```
ZunSchool/
├── courses/
│   ├── python/
│   │   ├── lessons/        # 00 → 22
│   │   ├── projects/       # Todo CLI, Student Manager...
│   │   └── solutions/      # Đáp án bài tập
│   ├── html/
│   │   ├── lessons/        # 00 → 18
│   │   └── projects/       # Profile page, Product page
│   ├── css/
│   │   ├── lessons/        # 00 → 20
│   │   └── projects/       # Card, Navbar, Landing page
│   └── cpp/
│       ├── lessons/        # 00 → 20
│       └── projects/       # Calculator, Student Manager
├── image/
│   └── zunny.png
└── README.md
```

---

## 🛠️ Cách học hiệu quả

1. **Chọn khoá học** phù hợp với mục tiêu của bạn.
2. **Clone repo** về máy và mở bằng VS Code.
3. **Chạy từng file** theo thứ tự từ bài `00`.
4. **Đọc comment trong code** – Zunny giải thích rất chi tiết.
5. **Sửa code, thử nghiệm** – cách nhanh nhất để nhớ.
6. **Làm bài tập** (đáp án có trong thư mục `solutions/`).
7. **Hỏi Zunny** qua Telegram bot hoặc mở Issues nếu gặp khó khăn.

---

## 🤝 Đóng góp

Dự án được xây dựng bởi cộng đồng, cho cộng đồng. Bạn có thể:

- 🐛 Báo lỗi hoặc đề xuất bài học mới qua **Issues**
- 📝 Gửi **Pull Request** cải thiện nội dung
- 🌍 Dịch nội dung sang ngôn ngữ khác
- ⭐ **Star repo** để ủng hộ dự án
- 📢 Chia sẻ với bạn bè!

---

## 📫 Liên hệ & Hỗ trợ

| Kênh | Thông tin |
|------|-----------|
| 🤖 Telegram Bot | [@Zunnycloud_bot](https://t.me/Zunnycloud_bot) – hỗ trợ tự động 24/7 |
| 📧 Email | zunny932@gmail.com |
| 🐛 GitHub Issues | [Tạo issue mới](https://github.com/ZunFox20/ZunSchool/issues) |

---

## 📜 Giấy phép

**MIT © 2026 Zun Technologies** – Mã nguồn mở, tự do sử dụng và phát triển.

---

<div align="center">
  <sub>Made with ☁️ and 💙 by <strong>Zun Technologies</strong> – where Zunny lives. 🦊</sub>
</div>
