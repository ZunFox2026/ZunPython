import inspect
import functools

# Bài tập 1: Viết hàm kiểm tra tham số bắt buộc
# Viết hàm `get_required_params(func)` nhận vào một hàm
# và trả về danh sách tên các tham số bắt buộc (không có giá trị mặc định)
def get_required_params(func):
    # TODO: Hoàn thành hàm
    pass

# Bài tập 2: Viết decorator kiểm tra kiểu tham số
# Viết decorator `type_check` kiểm tra kiểu tham số theo annotation
# Nếu tham số không đúng kiểu, ném lỗi TypeError
def type_check(func):
    # TODO: Hoàn thành decorator
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pass
    return wrapper

# Bài tập 3: In tên hàm gọi nó
# Viết hàm `who_called_me()` in ra tên hàm đã gọi nó
# Sử dụng inspect.stack()
def who_called_me():
    # TODO: Hoàn thành hàm
    pass

# Hàm để kiểm thử - không chỉnh sửa
def test_function_a():
    test_function_b()

def test_function_b():
    who_called_me()  # Dự kiến in ra: Hàm test_function_b đã gọi tôi