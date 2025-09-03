logs = [
    "2025-08-25 12:15:33 Иван /catalog",
    "2025-08-25 12:16:10 Мария /product/123",
    "2025-08-25 12:17:05 Иван /product/555",
    "2025-08-25 12:18:22 Мария /catalog",
    "2025-08-25 12:20:00 Иван /cart",
    "2025-08-25 12:21:15 Анна /catalog",
    "2025-08-25 12:25:30 Иван /product/777",
]
# - 1)
def most_active_user(logs):
    data_l = []
    data_d = {}
    for i_log in logs:
        data_l.append(i_log.split()[2])
    for user in data_l:
        data_d[user] = data_d.get(user, 0) + 1
    return max(data_d.items(), key=lambda x: x[1])
    
most_active_user = most_active_user(logs)
print(most_active_user)

# -2)
def most_active_user(logs):
    data_d = {}
    for i_log in logs:
        user = i_log.split()[2] 
        data_d[user] = data_d.get(user, 0) + 1
    return max(data_d.items(), key=lambda x: x[1])

# -> ("Иван", 4)
