import inspect

################################################################################
# Bài tập 1: In thông tin lớp
################################################################################

def print_class_info(cls):
    """In ra tất cả phương thức và thuộc tính của một lớp"""
    print(f"\\n--- Thông tin về lớp {cls.__name__} ---")
    
    # Lấy tất cả thành viên của lớp
    members = inspect.getmembers(cls)
    
    methods = []
    attributes = []
    
    for name, obj in members:
        if inspect.isfunction(obj) or inspect.ismethod(obj):
            methods.append(name)
        elif not name.startswith("__"):  # Bỏ qua các thuộc tính nội bộ
            attributes.append(name)
    
    print(f"Phương thức: {methods}")
    print(f"Thuộc tính: {attributes}")


################################################################################
# Bài tập 2: Viết decorator debug_call
################################################################################

def debug_call(func):
    """Decorator ghi log tên hàm, tham số và kết quả"""
    def wrapper(*args, **kwargs):
        # Lấy thông tin về tham số
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        arg_str = ", ".join(f"{k}={v}" for k, v in bound_args.arguments.items())
        
        print(f"[DEBUG] Gọi: {func.__name__}({arg_str})")
        
        result = func(*args, **kwargs)
        
        print(f"[DEBUG] Trả về: {result}")
        return result
    
    return wrapper


################################################################################
# Bài tập 3: Tìm hàm theo tên trong module
################################################################################

def find_functions_by_name(module, name):
    """Tìm tất cả các hàm trong module có tên chứa chuỗi `name`"""
    found = []
    for member_name, obj in inspect.getmembers(module, inspect.isfunction):
        if name.lower() in member_name.lower():
            found.append(member_name)
    return found


################################################################################
# Bài tập 4: Lấy thông tin người gọi
################################################################################

def get_caller_info():
    """Trả về tên hàm và số dòng của hàm gọi nó"""
    frame = inspect.currentframe().f_back  # Frame của hàm gọi
    if frame:
        return {
            "function": frame.f_code.co_name,
            "line": frame.f_lineno
        }
    return None


################################################################################
# Bài tập 5: Hiển thị mã nguồn nếu có
################################################################################

def show_source_if_available(obj):
    """In mã nguồn của đối tượng nếu có, nếu không thì in thông báo"""
    try:
        source = inspect.getsource(obj)
        print(f"Mã nguồn của {obj.__name__}:")
        print(source)
    except TypeError:
        print(f"Không thể lấy mã nguồn của {obj.__name__}. Đối tượng không phải là hàm hoặc lớp trong file.")
    except OSError:
        print(f"Không tìm thấy mã nguồn cho {obj.__name__}.")