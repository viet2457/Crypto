import numpy as np

# Dữ liệu cơ bản
total_resources = np.array([12, 10, 7])  # Tổng tài nguyên [CPU, RAM, Storage]
allocation = np.array([
    [4, 1, 2],  # P0
    [2, 0, 0],  # P1
    [3, 0, 2],  # P2
    [2, 1, 1],  # P3
    [0, 0, 2]   # P4
])
max_demand = np.array([
    [7, 5, 3],  # P0
    [3, 2, 2],  # P1
    [9, 0, 2],  # P2
    [2, 2, 2],  # P3
    [4, 3, 3]   # P4
])
need = max_demand - allocation

# Hàm kiểm tra trạng thái an toàn
def is_safe(available, allocation, need):
    work = available.copy()
    finish = [False] * len(allocation)
    safe_sequence = []

    while len(safe_sequence) < len(allocation):
        progress = False
        for i in range(len(allocation)):
            if not finish[i] and all(need[i] <= work):
                work += allocation[i]
                finish[i] = True
                safe_sequence.append(i)
                progress = True
                break
        if not progress:
            return False, []
    return True, safe_sequence

# Hàm yêu cầu tài nguyên
def request_resources():
    try:
        process_id = int(input("Nhập ID tiến trình (0-4): "))
        request = list(map(int, input("Nhập yêu cầu tài nguyên (CPU RAM Storage): ").split()))

        if process_id < 0 or process_id >= len(allocation):
            raise ValueError("ID tiến trình không hợp lệ.")

        # Tính toán tài nguyên còn lại
        available = total_resources - allocation.sum(axis=0)

        # Kiểm tra yêu cầu tài nguyên hợp lệ
        if all(request[i] <= need[process_id][i] for i in range(len(request))) and all(request[i] <= available[i] for i in range(len(request))):
            if any(request[i] > available[i] for i in range(len(request))):
                print("Yêu cầu tài nguyên vượt quá tài nguyên còn lại.")
                return

            # Cấp phát tài nguyên tạm thời
            available -= request
            allocation[process_id] += request
            need[process_id] -= request

            # Kiểm tra trạng thái an toàn
            safe, sequence = is_safe(available, allocation, need)
            if safe:
                print(f"Yêu cầu tài nguyên đã được chấp nhận.\nChuỗi an toàn: {sequence}")
            else:
                available += request
                allocation[process_id] -= request
                need[process_id] += request
                print("Yêu cầu bị từ chối. Trạng thái không an toàn.")
        else:
            print("Yêu cầu không hợp lệ hoặc không đủ tài nguyên.")
    except ValueError as e:
        print(str(e))

# Chạy hàm yêu cầu tài nguyên
if __name__ == "__main__":
    print(f"Tổng tài nguyên (CPU, RAM, Storage): {total_resources}")
    print(f"Tài nguyên đã cấp phát:\n{allocation}")
    print(f"Nhu cầu tối đa:\n{max_demand}")
    print(f"Tài nguyên còn lại: {total_resources - allocation.sum(axis=0)}")

    request_resources()
