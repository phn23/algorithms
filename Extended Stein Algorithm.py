# This program follows the flowchart of Jossy Sayir's 4F5: Extended Stein Algorithm (with some small modifications)
########################################################
# technically should add some checks
# assumptions as follows:
# n1 >= 0, n2 >=0, both not 0 at the same time
n1 = 90
n2 = 810

########################################################
c, flag = 0, 0

while n1 % 2  == 0 and n2 % 2 == 0:
  n1 /= 2
  n2 /= 2
  c += 1

if n2 % 2 == 0:
  n1, n2 = n2, n1
  flag = 1

N1, N2 = n1, n2
a1, b1 = 1, 0
a2, b2 = 0, 1

while n1 != 0:
  while n1 % 2 == 0:
    if a1 % 2 == 1:
      a1 -= N2
      b1 += N1

    n1 /= 2
    a1 /= 2
    b1 /= 2

  diff = n1 - n2
  if diff < 0:
    n2 = n1
    a1, a2 = a2, a1
    b1, b2 = b2, b1
    diff *= -1

  n1 = diff
  a1 -= a2
  b1 -= b2

if flag == 1:
  a2, b2 = b2, a2

g = int(2**c * n2)
a = int(a2)
b = int(b2)

print(g, a, b)

