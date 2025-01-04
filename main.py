# This is a sample Python script.

def seir(y, t, n, beta, gamma, delta):
    s, e, i, r = y
    dsdt = -beta * s * i / n
    dedt = beta * s * i / n - delta * e
    didt = delta * e - gamma * i
    drdt = gamma * i
    return dsdt, dedt, didt, drdt

def SEIRD(y, t, N, beta, gamma, delta, alpha, rho):
    S, E, I, R, D = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - delta * E
    dIdt = delta * E - (1 - alpha) * gamma * I - alpha * rho * I
    dRdt = (1 - alpha) * gamma * I
    dDdt = alpha * rho * I
    return dSdt, dEdt, dIdt, dRdt, dDdt

def SEIRD2(y, t, N, beta, gamma, delta, alpha, rho):
    S, E, I, R, D = y
    dSdt = -beta(t) * S * I / N
    dEdt = beta(t) * S * I / N - delta * E
    dIdt = delta * E - (1 - alpha) * gamma * I - alpha * rho * I
    dRdt = (1 - alpha) * gamma * I
    dDdt = alpha * rho * I
    return dSdt, dEdt, dIdt, dRdt, dDdt

def R_0(t):
    return 5.0 if t < TL else 0.8
def beta(t):
    return R_0(t) * gamma

def deriv(y, t, N, beta, gamma, delta, alpha_opt, rho):
    S, E, I, R, D = y
    def alpha(t):
        return s * I/N + alpha_opt

    dSdt = -beta(t) * S * I / N
    dEdt = beta(t) * S * I / N - delta * E
    dIdt = delta * E - (1 - alpha(t)) * gamma * I - alpha(t) * rho * I
    dRdt = (1 - alpha(t)) * gamma * I
    dDdt = alpha(t) * rho * I
    return dSdt, dEdt, dIdt, dRdt, dDdt

def logistic_R_0(t):
    return (R_ini-R_end) / (1 + np.exp(-k*(-t+xm))) + R_end

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from scipy.integrate import odeint
    import numpy as np
    import matplotlib.pyplot as plt

 #1) seir Model
    n = 1000000
    d = 4.0  # número de dias que uma pessoa propaga a doença
    gamma = 1.0 / d
    delta = 1.0 / 5.0  # (periodo de incubação 5 dias)
    r_0 = 5.0  # também definido como beta/gama, é o valor total de pessoas infectadas
            # por uma unica pessoa.

    beta = r_0 * gamma
    s0, e0, i0, r0 = n - 1, 1, 0, 0
    t = np.linspace(0, 99, 100)
    y0 = s0, e0, i0, r0

    out = odeint(seir, y0, t, args=(n, beta, gamma, delta))
    s, e, i, r = out.T

    plt.plot(t, s, label='S')
    plt.plot(t, e, label='E')
    plt.plot(t, i, label='I')
    plt.plot(t, r, label='R')
    plt.legend()
    plt.show()

