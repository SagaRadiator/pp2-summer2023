n = int(input())

sagat = n//60
if sagat >= 24:
    sagat = sagat % 24

minut = n%60

print(sagat, minut)