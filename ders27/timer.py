import time

orgiginalTime = int(input("Enter duration for count down timer: "))
print("\nCount Down Starting...")

for duration in range(orgiginalTime,0,-1):
    mins, seconds = (duration//60) , (duration%60)
    print(f"\r{mins:02d}:{seconds:02d}", end='',flush=True)
    time.sleep(1)

print("\rTime is over.      ")  # overwrites the timer display
