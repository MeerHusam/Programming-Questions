while True:
    n = int(input())
    if n == -1:
        break
    speed, prevTime = 0, 0
    distance = 0
    for a in range(n):
        str = input()
        speed, time = str.split(" ")
        speed = int(speed)
        time = int(time)
        distance += speed * (time - prevTime)
        prevTime = time
    print(distance, "miles")