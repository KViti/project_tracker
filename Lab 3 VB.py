from numpy import random
import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd

a = -0.3
σ = 1
μ = 1
Dε = 0.7
D𝜈 = 1.5
N = 100
ξ = [0.0] * (N + 1)

γ = random.normal(μ, σ, 1)[0]
ξ[0] = γ

for i in range(1, N + 1):
    ε = random.normal(0, Dε**0.5, 1)[0]
    ξ[i] = a*ξ[i-1] + ε

toPrint = pd.DataFrame(ξ, columns = ['ξ'])
display(toPrint)

η = [0.0]*(N + 1)

for i in range(N + 1):
    𝜈 = random.normal(0, D𝜈**0.5, 1)[0]
    η[i] = ξ[i] + 𝜈

toPrint = pd.DataFrame(η, columns = ['η'])
display(toPrint)


plt.figure(figsize=(8, 5))

plt.plot(range(N + 1), ξ, color = 'red', linewidth = 0.8)
plt.plot(range(N + 1), η, color = 'green', linewidth = 0.8)

plt.xlabel('t')
plt.ylabel('ξ(t), η(t)')




MSE = 0
for i in range (N + 1):
    MSE += (ξ[i] - η[i])**2

MSE /= N + 1

print('Mean Squared Error is', MSE)


K = [0.0]*(N + 1)
K[0] = (σ**2) / D𝜈

ρ = Dε / D𝜈
for i in range(1, N + 1):
    K[i] = ((a**2) * K[i-1] + ρ) / ((a**2) * K[i-1] + ρ + 1)

ξ_filtered = [0.0]*(N + 1)
ξ_filtered[0] = μ

for i in range(1, N + 1):
    ξ_filtered[i] = a * ξ_filtered[i-1] + K[i] * (η[i] - a * ξ_filtered[i-1])

toPrint = pd.DataFrame(ξ_filtered, columns = ['ξ_filtered'])
display(toPrint)


plt.figure(figsize=(8, 5))

plt.plot(range(N + 1), ξ, color = 'red', linewidth = 0.8)
plt.plot(range(N + 1), ξ_filtered, color = 'green', linewidth = 0.8)

plt.xlabel('t')
plt.ylabel('ξ(t), ξ_filtered(t)')


MSE = 0
for i in range (N + 1):
    MSE += (ξ[i] - ξ_filtered[i])**2

MSE /= N + 1

print('Mean Squared Error is', MSE)


P = [0.0]*(N + 1)
P[0] = σ**2

for i in range(1, N + 1):
    P[i] = K[i]*D𝜈

toPrint = pd.DataFrame(P, columns = ['P'])
display(toPrint)

sum = 0
for i in range(1, N + 1):
    sum += P[i]

print(sum / (N + 1))


ξ = [0.0]*(N + 1)

γ = random.normal(μ, σ, 1)[0]
ξ[0] = γ

for i in range(1, N + 1):
    ε = random.uniform(-(3**0.5)*(Dε**0.5), (3**0.5)*(Dε**0.5), 1)[0]
    ξ[i] = a*ξ[i-1] + ε

toPrint = pd.DataFrame(ξ, columns = ['ξ'])
display(toPrint)


η = [0.0]*(N + 1)

for i in range(N + 1):
    𝜈 = random.uniform(-(3**0.5)*(D𝜈**0.5), (3**0.5)*(D𝜈**0.5), 1)[0]
    η[i] = ξ[i] + 𝜈

toPrint = pd.DataFrame(η, columns = ['η'])
display(toPrint)


plt.figure(figsize=(8, 5))

plt.plot(range(N + 1), ξ, color = 'red', linewidth = 0.8)
plt.plot(range(N + 1), η, color = 'green', linewidth = 0.8)

plt.xlabel('t')
plt.ylabel('ξ(t), η(t)')


K = [0.0]*(N + 1)
K[0] = (σ**2) / D𝜈

ρ = Dε / D𝜈
for i in range(1, N + 1):
    K[i] = ((a**2) * K[i-1] + ρ) / ((a**2) * K[i-1] + ρ + 1)

ξ_filtered = [0.0]*(N + 1)
ξ_filtered[0] = μ

for i in range(1, N + 1):
    ξ_filtered[i] = a * ξ_filtered[i-1] + K[i] * (η[i] - a * ξ_filtered[i-1])

toPrint = pd.DataFrame(ξ_filtered, columns = ['ξ_filtered'])
display(toPrint)

plt.figure(figsize=(8, 5))

plt.plot(range(N + 1), ξ, color = 'red', linewidth = 0.8)
plt.plot(range(N + 1), ξ_filtered, color = 'green', linewidth = 0.8)

plt.xlabel('t')
plt.ylabel('ξ(t), ξ_filtered(t)')

MSE = 0
for i in range (N + 1):
    MSE += (ξ[i] - ξ_filtered[i])**2

MSE /= N+1

print('Mean Squared Error is', MSE)

P = [0.0]*(N + 1)
P[0] = σ**2

for i in range(1, N + 1):
    P[i] = K[i]*D𝜈

toPrint = pd.DataFrame(P, columns = ['P'])
display(toPrint)

sum = 0
for i in range(1, N + 1):
    sum += P[i]

print(sum / (N + 1))