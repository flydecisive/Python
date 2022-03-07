zum_speed = int(input())
flash_speed = int(input())

if zum_speed > flash_speed:
    result = 'NO'
elif zum_speed < flash_speed:
    result = 'YES'
else:
    result = "Don't know"

print(result)