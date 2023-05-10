#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

n = 600851475143
p_factor = []

c = 2
while(n > 1):
    if(n % c  == 0):
        p_factor.append(c)
        n = n / c
    else:
        c += 1

p_factor.sort(reverse=True)
print(p_factor.pop(0))

#Answer = 6857