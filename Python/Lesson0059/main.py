import inspect

def calculate_discount(price, discount=0.1, tax=0.05, **kwargs):
    """
    Tính giá sau giảm giá và thuế.
    """
    final_price = price * (1 - discount)
    final_price *= (1 + tax)
    return final_price

class ShoppingCart:
    """
    Lớp mô phỏng giỏ hàng.
    """
    def __init__(self, items=None):
        self.items = items or []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def get_total(self, discount=0, tax=0.1):
        total = sum(item['price'] for item in self.items)
        total *= (1 - discount)
        total *= (1 + tax)
        return total

# Ví dụ 1: In thông tin chi tiết về hàm
def example_1():
    print("=== Ví dụ 1: Thông tin về hàm calculate_discount ===")
    sig = inspect.signature(calculate_discount)
    print(f"Chữ ký hàm: {sig}")

    for name, param in sig.parameters.items():
        print(f"  - {name}: loại={param.kind}, mặc định={param.default if param.default != param.empty else 'Không'}")

# Ví dụ 2: Decorator ghi log tự động
def log_calls(func):
    def wrapper(*args, **kwargs):
        # Lấy thông tin về hàm
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        
        print(f"[LOG] Gọi hàm '{func.__name__}' với tham số: {dict(bound.arguments)}")
        
        result = func(*args, **kwargs)
        print(f"[LOG] Hàm '{func.__name__}' trả về: {result}")
        return result
    return wrapper

@log_calls
def multiply(a, b):
    return a * b

def example_2():
    print("\n=== Ví dụ 2: Sử dụng decorator log_calls ===")
    multiply(3, 4)

# Ví dụ 3: Phân tích lớp và phương thức
def example_3():
    print("\n=== Ví dụ 3: Phân tích lớp ShoppingCart ===")
    methods = inspect.getmembers(ShoppingCart, predicate=inspect.isfunction)
    
    for name, method in methods:
        print(f"Phương thức: {name}")
        try:
            sig = inspect.signature(method)
            print(f"  Tham số: {sig}")
            # In mã nguồn nếu có
            source = inspect.getsource(method)
            print(f"  Mã nguồn:\n{source.strip()}")
        except OSError:
            print("  Không thể lấy mã nguồn.")
        print("---")

if __name__ == "__main__":
    example_1()
    example_2()
    example_3()