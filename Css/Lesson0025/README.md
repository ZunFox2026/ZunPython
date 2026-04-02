# Tìm hiểu về thuộc tính Z-index
## Giới thiệu
Thuộc tính Z-index là một thuộc tính quan trọng trong CSS, giúp các nhà thiết kế web kiểm soát thứ tự chồng xếp của các phần tử trên trang web. Khi các phần tử có vị trí trùng nhau, thuộc tính Z-index sẽ quyết định phần tử nào sẽ được hiển thị trên cùng. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thuộc tính Z-index và các ứng dụng của nó trong thiết kế web.

## Lý thuyết
Thuộc tính Z-index là một giá trị số nguyên, có thể là dương, âm hoặc zero. Giá trị Z-index càng cao, phần tử sẽ được hiển thị càng trên cùng. Nếu hai phần tử có cùng giá trị Z-index, thứ tự chồng xếp sẽ được quyết định bởi thứ tự xuất hiện trong mã HTML. Để sử dụng thuộc tính Z-index, bạn cần đặt phần tử vào vị trí tuyệt đối (absolute) hoặc tương đối (relative) bằng cách thêm thuộc tính position vào phần tử.

Ví dụ:
```css
.div1 {
  position: absolute;
  z-index: 1;
  background-color: red;
  width: 100px;
  height: 100px;
}

.div2 {
  position: absolute;
  z-index: 2;
  background-color: blue;
  width: 100px;
  height: 100px;
  top: 50px;
  left: 50px;
}
```
Trong ví dụ trên, phần tử div2 sẽ được hiển thị trên cùng vì nó có giá trị Z-index cao hơn div1.

## Ví dụ
Giả sử chúng ta có hai phần tử div, div1 và div2, có cùng kích thước và vị trí trùng nhau. Nếu chúng ta muốn div2 được hiển thị trên cùng, chúng ta có thể thêm thuộc tính Z-index vào div2 như sau:
```css
.div1 {
  position: absolute;
  z-index: 1;
  background-color: red;
  width: 100px;
  height: 100px;
}

.div2 {
  position: absolute;
  z-index: 2;
  background-color: blue;
  width: 100px;
  height: 100px;
}
```
Kết quả sẽ là div2 được hiển thị trên cùng, che khuất div1.

## Bài tập
Bài tập 1: Tạo hai phần tử div, div1 và div2, có cùng kích thước và vị trí trùng nhau. Thêm thuộc tính Z-index vào div2 để nó được hiển thị trên cùng.

Bài tập 2: Tạo một phần tử div có vị trí tuyệt đối và thêm thuộc tính Z-index vào nó. Thử thay đổi giá trị Z-index và quan sát kết quả.

Bài tập 3: Tạo một trang web có nhiều phần tử chồng xếp nhau. Sử dụng thuộc tính Z-index để kiểm soát thứ tự chồng xếp của các phần tử.