import numpy
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

T = 10
a = 0.05
b = 0.25
h = 0.5
ξ0 = 1000
n = 20
N = int(T/h)

W = [[0.0]*(N+1)]*n

for i in range(n):
    ε = numpy.random.normal(0, numpy.sqrt(h), N+1)
    W_current = [0.0]*(N+1)

    for j in range(1, N+1):
        W_current[j] = W_current[j-1] + ε[j-1]

    W[i] = W_current

toPrint = pd.DataFrame(W)
display(toPrint)

t = list(range(0, N+1, 1))
plt.plot(t, W[1])


ξ = [[0.0]*(N+1)]*n

for i in range(n):
    ξ_current = [0.0]*(N+1)
    ξ_current[0] = ξ0

    for j in range(1, N+1):
        ξ_current[j] = ξ0*numpy.exp((a - (b**2)/2)*j*h + b*W[i][j])

    ξ[i] = ξ_current

toPrint = pd.DataFrame(ξ)
display(toPrint)

plt.plot(t, ξ[1])



X = [[0.0]*(N+1)]*n

for i in range(n):
    X_current = [0.0]*(N+1)
    X_current[0] = ξ0

    for j in range(N):
        X_current[j+1] = X_current[j] + a*X_current[j]*h + b*X_current[j]*(W[i][j+1] - W[i][j])

    X[i] = X_current

toPrint = pd.DataFrame(X)
display(toPrint)

plt.plot(t, X[1])


plt.plot(t, ξ[1])
plt.plot(t, X[1], linestyle = 'dashed')



ME = 0
for i in range(n):
    ME += numpy.abs(ξ[i][N] - X[i][N])

ME /= n

print('Mean Error is', ME)


b = 0.5
W = [[0.0]*(N+1)]*n

for i in range(n):
    ε = numpy.random.normal(0, numpy.sqrt(h), N+1)
    W_current = [0.0]*(N+1)

    for j in range(1, N+1):
        W_current[j] = W_current[j-1] + ε[j-1]

    W[i] = W_current


ξ = [[0.0]*(N+1)]*n

for i in range(n):
    ξ_current = [0.0]*(N+1)
    ξ_current[0] = ξ0

    for j in range(1, N+1):
        ξ_current[j] = ξ0*numpy.exp((a - (b**2)/2)*j*h + b*W[i][j])

    ξ[i] = ξ_current

X = [[0.0]*(N+1)]*n

for i in range(n):
    X_current = [0.0]*(N+1)
    X_current[0] = ξ0

    for j in range(N):
        X_current[j+1] = X_current[j] + a*X_current[j]*h + b*X_current[j]*(W[i][j+1] - W[i][j])

    X[i] = X_current

X = [[0.0]*(N+1)]*n

for i in range(n):
    X_current = [0.0]*(N+1)
    X_current[0] = ξ0

    for j in range(N):
        X_current[j+1] = X_current[j] + a*X_current[j]*h + b*X_current[j]*(W[i][j+1] - W[i][j])

    X[i] = X_current


W = [[0.0]*(N+1)]*n

for i in range(n):
    ε = numpy.random.normal(0, numpy.sqrt(h), N+1)
    W_current = [0.0]*(N+1)

    for j in range(1, N+1):
        W_current[j] = W_current[j-1] + ε[j-1]

    W[i] = W_current

ξ = [[0.0]*(N+1)]*n

for i in range(n):
    ξ_current = [0.0]*(N+1)
    ξ_current[0] = ξ0

    for j in range(1, N+1):
        ξ_current[j] = ξ0*numpy.exp((a - (b**2)/2)*j*h + b*W[i][j])

    ξ[i] = ξ_current


X = [[0.0]*(N+1)]*n

for i in range(n):
    X_current = [0.0]*(N+1)
    X_current[0] = ξ0

    for j in range(N):
        X_current[j+1] = X_current[j] + a*X_current[j]*h + b*X_current[j]*(W[i][j+1] - W[i][j])

    X[i] = X_current


ME = 0
for i in range(n):
    ME += numpy.abs(ξ[i][N] - X[i][N])

ME /= n

print('Mean Error is', ME)


ME = 0
for i in range(n):
    ME += numpy.abs(ξ[i][N] - X[i][N])

ME /= n

print('Mean Error is', ME)

b = 0.25


def getMeanError(step):
    N_tmp = int(T / step)

    W = [[0.0] * (N_tmp + 1)] * n
    for i in range(n):
        ε = numpy.random.normal(0, numpy.sqrt(step), N_tmp + 1)
        W_current = [0.0] * (N_tmp + 1)

        for j in range(1, N_tmp + 1):
            W_current[j] = W_current[j - 1] + ε[j - 1]

        W[i] = W_current

    ξ = [[0.0] * (N_tmp + 1)] * n

    for i in range(n):
        ξ_current = [0.0] * (N_tmp + 1)
        ξ_current[0] = ξ0

        for j in range(1, N_tmp + 1):
            ξ_current[j] = ξ0 * numpy.exp((a - (b ** 2) / 2) * j * step + b * W[i][j])

        ξ[i] = ξ_current

    X = [[0.0] * (N_tmp + 1)] * n

    for i in range(n):
        X_current = [0.0] * (N_tmp + 1)
        X_current[0] = ξ0

        for j in range(N_tmp):
            X_current[j + 1] = X_current[j] + a * X_current[j] * step + b * X_current[j] * (W[i][j + 1] - W[i][j])

        X[i] = X_current

    ME = 0
    for i in range(n):
        ME += numpy.abs(ξ[i][N_tmp] - X[i][N_tmp])

    return ME / n



h_exp = [0.002, 0.01, 0.02, 0.025, 0.05, 0.1, 0.25, 0.4, 0.5]

ME_exp = []
for i in h_exp:
    ME_exp.append(getMeanError(i))

toPrint = pd.DataFrame(zip(h_exp, ME_exp), columns = ['h', 'ε(h)'])
display(toPrint)


X = numpy.ones((len(h_exp), 2))
for i in range(len(h_exp)):
    X[i][1] = numpy.log(h_exp[i])

y = numpy.zeros(len(h_exp))
for i in range(len(h_exp)):
    y[i] = numpy.log(ME_exp[i])

matrixToPrint = pd.DataFrame(X, columns = ['1', 'ln(h)'])
display(matrixToPrint)

vectorToPrint = pd.DataFrame(y, columns = ['ln(ε)'])
display(vectorToPrint)

X_transp = X.transpose()
α = numpy.linalg.inv(X_transp.dot(X)).dot(X_transp).dot(y)

toPrint = pd.DataFrame(α, columns = ['α'])
display(toPrint)

# plt.scatter (numpy.log(h_exp), numpy.log(ME_exp))
# z = numpy.polyfit (numpy.log(h_exp), numpy.log(ME_exp), 1 )
# p = numpy.poly1d (z)
# plt.plot (numpy.log(h_exp), p(numpy.log(h_exp)))
# plt.xlabel('ln(h)')
# plt.ylabel('ln(ε)')
# print(numpy.poly1d (z))


