temp = 20
is_sunny = True

if temp >=30 and is_sunny:
    print("Hot")
    print("Sunny")
elif temp <=0 and is_sunny:
    print("Cold")
    print("Sunny")
elif 28 > temp > 0 and is_sunny:
    print("Warm")
    print("Sunny")

elif temp >=30 and not is_sunny:
    print("Hot")
    print("Cloudy")
elif temp <=0 and not is_sunny:
    print("Cold")
    print("Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("Warm")
    print("Cloudy")