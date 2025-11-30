import numpy as np
import random

# --- CẤU HÌNH THUẬT TOÁN ---
POPULATION_SIZE = 10   # Số lượng sói
MAX_ITERATIONS = 100    # Số vòng lặp tối đa
DIMENSION = 50         # Số chiều của bài toán (ví dụ: số lượng đặc trưng/feature)

# --- 1. ĐỊNH NGHĨA BÀI TOÁN ---
def fitness_function(position):
    """
    Hàm mục tiêu demo: OneMax Problem.
    Mục tiêu: Tối đa hóa số lượng bit 1 trong chuỗi.
    Input: position (mảng gồm các số 0 và 1)
    Output: Giá trị fitness (càng cao càng tốt)
    """
    return np.sum(position)

# --- 2. HÀM CHUYỂN ĐỔI (TRANSFER FUNCTION) ---
def sigmoid_transfer(x):
    """
    Hàm Sigmoid chuyển đổi giá trị thực sang xác suất.
    Công thức: T(x) = 1 / (1 + e^(-10 * (x - 0.5)))
    """
    return 1 / (1 + np.exp(-10 * (x - 0.5)))

# --- 3. THUẬT TOÁN BGWO ---
class BinaryGWO:
    def __init__(self, pop_size, max_iter, dim):
        self.pop_size = pop_size
        self.max_iter = max_iter
        self.dim = dim
        
        # Khởi tạo quần thể sói (vị trí ngẫu nhiên 0 hoặc 1)
        self.positions = np.random.randint(2, size=(pop_size, dim))
        # Khởi tạo "vị trí liên tục" để cập nhật (giá trị thực)
        self.continuous_positions = np.random.rand(pop_size, dim)
        
        self.fitness = np.zeros(pop_size)
        
        # Khởi tạo Alpha, Beta, Delta
        self.alpha_pos = np.zeros(dim)
        self.alpha_score = -float("inf") 
        
        self.beta_pos = np.zeros(dim)
        self.beta_score = -float("inf")
        
        self.delta_pos = np.zeros(dim)
        self.delta_score = -float("inf")

    def optimize(self):
        print(f"Bắt đầu tối ưu hóa với {self.pop_size} cá thể trong {self.max_iter} vòng lặp...")
        
        for t in range(self.max_iter):
            # 1. Tính toán độ thích nghi (Fitness) cho từng con sói
            for i in range(self.pop_size):
                self.fitness[i] = fitness_function(self.positions[i])
                
                # Cập nhật Alpha, Beta, Delta
                if self.fitness[i] > self.alpha_score:
                    self.delta_score = self.beta_score
                    self.delta_pos = self.beta_pos.copy()
                    self.beta_score = self.alpha_score
                    self.beta_pos = self.alpha_pos.copy()
                    self.alpha_score = self.fitness[i]
                    self.alpha_pos = self.positions[i].copy()
                elif self.fitness[i] > self.beta_score:
                    self.delta_score = self.beta_score
                    self.delta_pos = self.beta_pos.copy()
                    self.beta_score = self.fitness[i]
                    self.beta_pos = self.positions[i].copy()
                elif self.fitness[i] > self.delta_score:
                    self.delta_score = self.fitness[i]
                    self.delta_pos = self.positions[i].copy()

            # Hệ số a giảm tuyến tính từ 2 xuống 0
            a = 2 - t * (2 / self.max_iter)

            # 2. Cập nhật vị trí cho từng con sói Omega
            for i in range(self.pop_size):
                for d in range(self.dim):
                    # --- Tính toán theo công thức GWO gốc cho không gian liên tục ---
                    # Sói Alpha
                    r1, r2 = np.random.rand(), np.random.rand()
                    A1 = 2 * a * r1 - a
                    C1 = 2 * r2
                    D_alpha = abs(C1 * self.alpha_pos[d] - self.continuous_positions[i, d])
                    X1 = self.alpha_pos[d] - A1 * D_alpha
                    
                    # Sói Beta
                    r1, r2 = np.random.rand(), np.random.rand()
                    A2 = 2 * a * r1 - a
                    C2 = 2 * r2
                    D_beta = abs(C2 * self.beta_pos[d] - self.continuous_positions[i, d])
                    X2 = self.beta_pos[d] - A2 * D_beta
                    
                    # Sói Delta
                    r1, r2 = np.random.rand(), np.random.rand()
                    A3 = 2 * a * r1 - a
                    C3 = 2 * r2
                    D_delta = abs(C3 * self.delta_pos[d] - self.continuous_positions[i, d])
                    X3 = self.delta_pos[d] - A3 * D_delta
                    
                    # Vị trí liên tục trung bình
                    X_cont_new = (X1 + X2 + X3) / 3
                    
                    # Lưu lại giá trị liên tục để dùng cho vòng sau
                    self.continuous_positions[i, d] = X_cont_new
                    
                    # --- Chuyển đổi sang Nhị phân (Binary) --- [cite: 72, 73]
                    # Tính xác suất bằng hàm Sigmoid
                    proba = sigmoid_transfer(X_cont_new)
                    
                    # Cập nhật vị trí nhị phân (0 hoặc 1)
                    if np.random.rand() < proba:
                        self.positions[i, d] = 1
                    else:
                        self.positions[i, d] = 0
            
            # In kết quả từng vòng lặp
            print(f"Iter {t+1} | Best Fitness: {self.alpha_score}")

        return self.alpha_pos, self.alpha_score

# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    # Khởi tạo mô hình
    bgwo = BinaryGWO(pop_size=POPULATION_SIZE, max_iter=MAX_ITERATIONS, dim=DIMENSION)
    
    # Chạy tối ưu hóa
    best_solution, best_fitness = bgwo.optimize()
    
    print("\n--- KẾT QUẢ CUỐI CÙNG ---")
    print(f"Lời giải tốt nhất (Alpha): {best_solution}")
    print(f"Giá trị Fitness tốt nhất: {best_fitness}")