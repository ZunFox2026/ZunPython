# Tạo Form Đăng Nhập
## Giới thiệu
Trong phần trước, chúng ta đã tìm hiểu về các thẻ cơ bản trong HTML. Tiếp theo, chúng ta sẽ tìm hiểu về cách tạo một form đăng nhập đơn giản bằng HTML và CSS. Form đăng nhập là một phần không thể thiếu trong bất kỳ trang web nào, và việc tạo ra một form đăng nhập đẹp và chức năng là một kỹ năng quan trọng cho bất kỳ nhà phát triển web nào.

Để tạo một form đăng nhập, chúng ta sẽ sử dụng các thẻ HTML như `form`, `input`, `label`, và `button`. Chúng ta cũng sẽ sử dụng CSS để tạo kiểu và thiết kế cho form đăng nhập của mình.

## Lý thuyết
Trước khi bắt đầu tạo form đăng nhập, chúng ta cần hiểu về các thẻ HTML sẽ được sử dụng. Dưới đây là một số thẻ HTML quan trọng:

* `form`: Thẻ này dùng để tạo một form trong HTML.
* `input`: Thẻ này dùng để tạo một trường nhập liệu trong form.
* `label`: Thẻ này dùng để tạo một nhãn cho trường nhập liệu.
* `button`: Thẻ này dùng để tạo một nút trong form.

Chúng ta cũng cần hiểu về các thuộc tính của các thẻ này, như `type` cho thẻ `input`, `for` cho thẻ `label`, và `name` cho thẻ `input` và `button`.

Ví dụ về HTML cho một form đăng nhập đơn giản:
```html
<form>
  <label for="username">Tên đăng nhập:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="password">Mật khẩu:</label>
  <input type="password" id="password" name="password"><br><br>
  <button type="submit">Đăng nhập</button>
</form>
```
Và ví dụ về CSS cho form đăng nhập này:
```css
form {
  width: 300px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"], input[type="password"] {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button[type="submit"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}
```
## Ví dụ
Dưới đây là ví dụ hoàn chỉnh về HTML và CSS cho một form đăng nhập đơn giản:
```html
<form>
  <label for="username">Tên đăng nhập:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="password">Mật khẩu:</label>
  <input type="password" id="password" name="password"><br><br>
  <button type="submit">Đăng nhập</button>
</form>
```
```css
form {
  width: 300px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"], input[type="password"] {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button[type="submit"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}
```
## Bài tập
Bài tập cho bạn là tạo một form đăng nhập với các trường nhập liệu cho tên đăng nhập, mật khẩu, và một nút đăng nhập. Hãy sử dụng