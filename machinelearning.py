a = 0.05
W1 = -0.11
W2 = 0.24
W3 = -0.15
W4 = 0.03
W5 = -0.14
W6 = 0.11
i1 = 2
i2 = 3
H1 = 0.5
H2 = -0.21
count = 0
iterations = 10

while count < iterations:
    Delta = abs(H1) * W5 + abs(H2) * W6 -1

    W1 = W1 - a * (i1 * W5 * Delta)
    W2 = W2 - a * (i2 * W5 * Delta)
    W3 = W3 - a * (i1 * W6 * Delta)
    W4 = W4 - a * (i2 * W6 * Delta)
    W5 = W5 - a * (H1 * Delta)
    W6 = W6 - a * (H2 * Delta)

    print (round (W1,3), round (W2,3), round (W3,3), round (W4,3), round (W5,3), round (W6,3) )
    count = count +1