import inspect

def example_1_basic_reflection():
    """Ví dụ 1: Sử dụng các hàm phản xạ cơ bản"""
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Xin chào, tôi là {self.name}"

    p = Person("An", 25)

    # Kiểm tra kiểu
    print("Kiểu của p:", type(p))

    # Liệt kê tất cả thuộc tính và phương thức
    print("\nCác thành viên của p:", dir(p))

    # Kiểm tra và lấy thuộc tính
    if hasattr(p, 'name'):
        print("Tên:", getattr(p, 'name'))

    # Kiểm tra xem có phải callable
    if callable(p.greet):
        print("Gọi greet():", p.greet())


def example_2_inspect_functions():
    """Ví dụ 2: Sử dụng inspect để phân tích hàm"""
    
    def calculate_area(length, width=10, unit='m'):
        """Tính diện tích hình chữ nhật"""
        return length * width

    # Lấy chữ ký hàm
    sig = inspect.signature(calculate_area)
    print("Chữ ký hàm calculate_area:", sig)

    # Duyệt qua các tham số
    print("\nChi tiết các tham số:")
    for name, param in sig.parameters.items():
        default = param.default if param.default != inspect.Parameter.empty else "<không có>"
        print(f"- {name}: mặc định = {default}, kiểu = {param.kind}")

    # Lấy docstring
    print("\nDocstring:", calculate_area.__doc__)

    # Lấy mã nguồn (nếu có)
    try:
        source = inspect.getsource(calculate_area)
        print("\nMã nguồn:\n", source)
    except OSError:
        print("Không thể lấy mã nguồn (hàm built-in hoặc không truy cập được)")


def example_3_automatic_plugin_discovery():
    """Ví dụ 3: Tự động phát hiện các lớp con (ứng dụng plugin)"""
    
    class PaymentProcessor:
        def process(self, amount):
            raise NotImplementedError()

    class CreditCardProcessor(PaymentProcessor):
        def process(self, amount):
            return f"Xử lý {amount} bằng thẻ tín dụng"

    class PayPalProcessor(PaymentProcessor):
        def process(self, amount):
            return f"Xử lý {amount} bằng PayPal"

    # Tự động tìm tất cả các lớp con của PaymentProcessor
    def get_all_processors():
        subclasses = PaymentProcessor.__subclasses__()
        return {cls.__name__: cls for cls in subclasses}

    processors = get_all_processors()
    print("Các bộ xử lý thanh toán tìm thấy:", list(processors.keys()))

    # Tạo instance và xử lý
    for name, cls in processors.items():
        instance = cls()
        result = instance.process(100)
        print(f"{name}: {result}")

    # Dùng inspect để kiểm tra thêm
    for cls in processors.values():
        print(f"\nThông tin về {cls.__name__}:")
        print("- Là lớp?", inspect.isclass(cls))
        print("- Có phương thức process?", hasattr(cls, 'process'))
        if hasattr(cls, 'process'):
            method = getattr(cls, 'process')
            sig = inspect.signature(method)
            print("- Chữ ký phương thức process:", sig)

if __name__ == "__main__":
    print("=== Ví dụ 1: Phản xạ cơ bản ===")
    example_1_basic_reflection()

    print("\n=== Ví dụ 2: Phân tích hàm với inspect ===")
    example_2_inspect_functions()

    print("\n=== Ví dụ 3: Phát hiện plugin tự động ===")
    example_3_automatic_plugin_discovery()
