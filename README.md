# Binary Grey Wolf Optimization (BGWO) - Group 13

> **Project Demo: Thuật toán Tối ưu hóa Sói Xám phiên bản Rời rạc (Binary GWO)** > **Đề tài:** Tìm hiểu và cài đặt thuật toán GWO cùng các biến thể.

## 1. Giới thiệu (Introduction)

Dự án này là phần demo mã nguồn thuộc báo cáo bài tập lớn của **Nhóm 13**. Chúng tôi cài đặt thuật toán **Binary Grey Wolf Optimization (BGWO)** để giải quyết các bài toán tối ưu hóa trong không gian rời rạc (0 và 1).

Khác với GWO gốc hoạt động trên không gian liên tục, phiên bản này sử dụng **Hàm chuyển đổi (Transfer Function)** để biến đổi các giá trị thực thành xác suất, từ đó cập nhật vị trí của sói thành 0 hoặc 1.

### Thông tin nhóm thực hiện (Team Members)
| STT | Họ và tên | MSSV | Vai trò |
|:---:|:---|:---:|:---|
| 1 | **Nguyễn Việt Anh** | 20235651 | Nghiên cứu lý thuyết & Code |
| 2 | **Hoàng Văn Bình** | 20235664 | Nghiên cứu biến thể & Báo cáo |

---

## 2. Chi tiết thuật toán (Algorithm Implementation)

Mã nguồn được cài đặt dựa trên các lý thuyết đã trình bày trong báo cáo:

* **Thuật toán:** Binary Grey Wolf Optimization (BGWO).
* **Hàm chuyển đổi (Transfer Function):** Sử dụng hàm **Sigmoid (S-shaped)**.
    * Công thức: $T(x) = \frac{1}{1+e^{-10(x-0.5)}}$.
    * Cơ chế: Hàm này buộc các giá trị di chuyển về cực (0 hoặc 1) một cách mềm mại.
* **Quy tắc cập nhật vị trí:**
    * Nếu $rand < T(x^d)$ $\rightarrow$ Vị trí mới = 1.
    * Ngược lại $\rightarrow$ Vị trí mới = 0.
* **Bài toán Demo:** OneMax Problem (Tìm chuỗi nhị phân có tổng giá trị lớn nhất). Đây là bài toán cơ sở đại diện cho các bài toán phức tạp hơn như *Feature Selection*.

---

## 3. Cài đặt và Sử dụng (Installation & Usage)

Để chạy được mã nguồn này, máy tính cần cài đặt Python và thư viện NumPy.

### Bước 1: Clone dự án
```bash
git clone https://github.com/hvb1412/Binary-GWO-Python-Group13.git
cd Ten-Repo-Cua-Ban
```
### Bước 2: Cài đặt thư viện
```bash
pip install numpy
```
### Bước 3: Chạy chương trình
```bash
python BGWO_Demo.py
```