###############
# Bài tập 1 #
###############
def safe_getattr(obj, attr, default=None, allow_private=False):
    """
    Viết hàm an toàn để lấy thuộc tính từ đối tượng.
    - Nếu thuộc tính không tồn tại, trả về default.
    - Nếu allow_private=False, không cho phép truy cập thuộc tính bắt đầu bằng _.
    """
    pass

###############
# Bài tập 2 #
###############
def list_methods(obj):
    """
    Trả về danh sách tên các phương thức công khai (không bắt đầu bằng _) của đối tượng.
    """
    pass

###############
# Bài tập 3 #
###############
class PluginManager:
    """
    Quản lý các plugin (lớp xử lý) được đăng ký theo tên.
    Yêu cầu:
    - register_plugin(name, plugin_class): đăng ký lớp plugin
    - create_and_run(name, *args, **kwargs): tạo đối tượng và gọi run()
    """
    def __init__(self):
        self.plugins = {}
    
    def register_plugin(self, name, plugin_class):
        pass
    
    def create_and_run(self, name, *args, **kwargs):
        pass

###############
# Bài tập 4 #
###############
def is_subclass(obj, base_class):
    """
    Kiểm tra xem obj (có thể là lớp hoặc đối tượng) có kế thừa từ base_class không.
    """
    pass

###############
# Bài tập 5 #
###############
def dump_object_info(obj):
    """
    In ra thông tin chi tiết về một đối tượng:
    - Loại
    - Các thuộc tính (không phải hàm, không private)
    - Các phương thức công khai
    """
    pass