# Bài tập 2 – Cấp Cơ bản  
**Chủ đề:** Xử lý danh sách và từ điển trong Python  

---

## Giới thiệu  

Bài tập này hướng dẫn sinh viên làm quen với hai cấu trúc dữ liệu cơ bản nhất trong Python – **list (danh sách)** và **dict (từ điển)**. Khi học xong, bạn sẽ biết cách:  

* Tạo, truy cập và thay đổi các phần tử trong list và dict.  
* Duyệt qua các cấu trúc này bằng vòng lặp `for`.  
* Áp dụng các hàm nội建 (built‑in) như `len()`, `append()`, `pop()`, `keys()`, `values()`, `items()`.  
* Giải quyết các bài toán thực tế như thống kê tần suất từ, sắp xếp danh sách học sinh theo điểm, hoặc xây dựng một “phone‑book” đơn giản.  

Kiến thức này là nền tảng để tiếp cận các chủ đề nâng cao như xử lý file, làm việc với JSON, hoặc viết các thuật toán sắp xếp và tìm kiếm.

---

## Lý thuyết  

### 1. List (danh sách)  
* **Khái niệm:** Tập hợp có thứ tự các đối tượng, cho phép trùng lặp.  
* **Cú pháp:** `my_list = [1, "apple", 3.14]`  
* **Thao tác phổ biến:**  
  * Truy cập: `my_list[0]` → phần tử đầu tiên.  
  * Thêm: `my_list.append(42)` (cuối) hoặc `my_list.insert(1, "banana")` (vị trí chỉ định).  
  * Xóa: `my_list.pop()` (cuối) hoặc `my_list.remove("apple")` (theo giá trị).  
  * Độ dài: `len(my_list)`.  
  * Duyệt: `for item in my_list:`.

### 2. Dict (từ điển)  
* **Khái niệm:** Tập hợp các cặp *key‑value* (khóa‑giá trị), khóa phải là immutable (int, str, tuple …).  
* **Cú pháp:** `my_dict = {"name": "An", "age": 20}`  
* **Thao tác phổ biến:**  
  * Truy cập: `my_dict["name"]` → `"An"`.  
  * Thêm/sửa: `my_dict["city"] = "Hà Nội"` (thêm mới nếu khóa chưa tồn tại).  
  * Xóa: `del my_dict["age"]` hoặc `my_dict.pop("age")`.  
  * Lấy danh sách khóa/giá trị: `my_dict.keys()`, `my_dict.values()`, `my_dict.items()`.  
  * Duyệt: `for k, v in my_dict.items():`.

### 3. Lưu ý khi sử dụng  
* List giữ thứ tự insertion; dict từ Python 3.7 cũng giữ thứ tự insertion (được chuẩn hoá).  
* Khi cần tra cứu nhanh theo khóa, dict là lựa chọn tối ưu (O(1) trung bình).  
* Khi cần lưu danh sách có thể trùng lặp và cần truy cập theo vị trí, dùng list.

---

## Ví dụ  

```python
# Ví dụ 1: Thống kê tần suất từ trong một câu
sentence = "python là ngôn ngữ lập trình python rất mạnh mẽ và python dễ học"
words = sentence.lower().split()          # Tách từ, chuyển về chữ thường
freq = {}                                 # Từ điển lưu tần suất

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print("Tần suất từ:")
for word, count in freq.items():
    print(f"{word}: {count}")

# Ví dụ 2: Sắp xếp danh sách học sinh theo điểm giảm dần
students = [
    {"name": "An",   "score": 85},
    {"name": "Bình", "score": 92},
    {"name": "Cường","score": 78},
]

# Sắp xếp bằng lambda lấy trường key