# Bài 29: Làm quen với máy học

# Import các thư viện cần thiết
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# Tải dữ liệu mẫu về hoa iris
iris = datasets.load_iris()

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Tạo một mô hình máy học (Support Vector Machine)
model = svm.SVC()

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Sử dụng mô hình để dự đoán
y_pred = model.predict(X_test)

# Đánh giá hiệu suất của mô hình
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Độ chính xác của mô hình:", accuracy)

# In ra các lớp dự đoán
print("Các lớp dự đoán:", y_pred)

# In ra các lớp thực tế
print("Các lớp thực tế:", y_test)