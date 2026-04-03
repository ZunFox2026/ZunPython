import time
import functools

# Ví dụ 1: Đo thời gian thực thi
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Hàm '{func.__name__}' thực thi trong {end - start:.4f} giây")
        return result
    return wrapper

@timer
def calculate_sum(n):
    """Tính tổng từ 1 đến n"""
    return sum(range(1, n + 1))

# Ví dụ 2: Kiểm tra quyền truy cập
def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if permission not in user.get('permissions', []):
                print(f"Người dùng {user['name']} không có quyền {permission}")
                return None
            print(f"Người dùng {user['name']} có quyền {permission}, thực hiện hàm...")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@requires_permission('edit')
def edit_document(user, doc_name):
    print(f"{user['name']} đang chỉnh sửa tài liệu '{doc_name}'")

# Ví dụ 3: Ghi log hoạt động
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Đang gọi hàm: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Hàm {func.__name__} đã thực thi xong")
        return result
    return wrapper

@logger
def greet(name):
    print(f"Xin chào, {name}!")

# Chạy các ví dụ
def main():
    print("=== Ví dụ 1: Đo thời gian ===")
    result = calculate_sum(100000)
    print(f"Kết quả: {result}\n")
    
    print("=== Ví dụ 2: Kiểm tra quyền ===")
    user1 = {'name': 'An', 'permissions': ['view', 'edit']}
    user2 = {'name': 'Bình', 'permissions': ['view']}
    
    edit_document(user1, "Báo cáo Q3")
    edit_document(user2, "Báo cáo Q4")
    print()
    
    print("=== Ví dụ 3: Ghi log ===")
    greet("Minh")

if __name__ == "__main__":
    main()