# Unit-3D Task-4: Simple interest with a default argument (rate = 5)

def simple_interest(principal, time, rate=5):
    return (principal * time * rate) / 100


print("SI (default rate):", simple_interest(1000, 2))
print("SI (rate=8):", simple_interest(1000, 2, 8))
