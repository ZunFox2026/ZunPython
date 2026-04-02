# Tìm Số Nguyên Tố
## Giới thiệu
Số nguyên tố là một số tự nhiên lớn hơn 1, chỉ có hai ước là 1 và chính nó. Bài viết này sẽ giúp bạn hiểu rõ hơn về số nguyên tố và cách tìm số nguyên tố bằng ngôn ngữ lập trình Python.

## Lý thuyết
Một số được gọi là số nguyên tố nếu nó đáp ứng hai điều kiện sau:
- Là số tự nhiên lớn hơn 1.
- Chỉ có hai ước là 1 và chính nó.
Để kiểm tra một số có phải là số nguyên tố hay không, chúng ta có thể sử dụng thuật toán kiểm tra số nguyên tố. Thuật toán này sẽ kiểm tra tất cả các số từ 2 đến căn bậc hai của số cần kiểm tra, nếu số cần kiểm tra chia hết cho bất kỳ số nào trong khoảng này, thì nó không phải là số nguyên tố.

## Ví dụ
Ví dụ, chúng ta muốn kiểm tra số 25 có phải là số nguyên tố hay không. Chúng ta sẽ kiểm tra tất cả các số từ 2 đến căn bậc hai của 25 (khoảng 5). Kết quả là 25 chia hết cho 5, nên 25 không phải là số nguyên tố.

Mặt khác, nếu chúng ta kiểm tra số 23, chúng ta sẽ thấy rằng 23 không chia hết cho bất kỳ số nào từ 2 đến căn bậc hai của 23 (khoảng 4,8), nên 23 là số nguyên tố.

## Bài tập
Bài tập này yêu cầu bạn viết một chương trình Python để kiểm tra một số có phải là số nguyên tố hay không. Chương trình sẽ nhận vào một số tự nhiên lớn hơn 1 và trả về True nếu số đó là số nguyên tố, False nếu không.

Ví dụ, nếu người dùng nhập số 25, chương trình sẽ trả về False, vì 25 không phải là số nguyên tố. Nếu người dùng nhập số 23, chương trình sẽ trả về True, vì 23 là số nguyên tố.

Chương trình sẽ sử dụng thuật toán kiểm tra số nguyên tố đã được mô tả ở trên. Bạn có thể sử dụng vòng lặp để kiểm tra tất cả các số từ 2 đến căn bậc hai của số cần kiểm tra.