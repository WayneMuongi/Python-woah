import time


def calculate_sum(n):
    sum=0
    for num in range(1,n+1):
        print(f"sum={sum},num={num}")
        sum=sum+num
    print(f"for {n}")
    return sum 





start_time=time.time()
calculate_sum(50000)
end_time=time.time()
diff=end_time-start_time
print(f"Speed {diff}")
