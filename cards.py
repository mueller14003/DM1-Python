works = []
nope = []
sd_month_days = [0,31,28,31,30,31,30,31,31,30,31]
for i in range(100,999):
    if i//100 == 1 and (0 < (i%100) < 10):
        works.append(i)
    elif i//100 < 10 and (i//10)%10 != 0 and i%100 <= sd_month_days[i//100]:
        works.append(i)
    else:
        nope.append(i)

print("Works:", len(works), "\nNope:", len(nope))
print("Probability:",len(works)/899)