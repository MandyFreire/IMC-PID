import numpy as np

def pid_control(Kc, Ti, Td, setpoint, initial_value, t):
    """
    Implementação do controlador PID clássico.
    """
    y_pid = np.zeros(len(t))
    e_previous = 0
    integral = 0

    for i in range(1, len(t)):
        e = setpoint - initial_value
        integral += e * (t[i] - t[i-1])
        derivative = (e - e_previous) / (t[i] - t[i-1])
        y_pid[i] = Kc * (e + (1.0/Ti) * integral + Td * derivative)
        e_previous = e

    return y_pid

def imc_pid_control(Kp, tau, theta, lambda_imc, setpoint, initial_value, t):
    """
    Implementação do controlador IMC-PID.
    """
    Kc_imc = tau / (Kp * (lambda_imc + theta))
    Ti_imc = tau
    Td_imc = (theta * tau) / (2 * lambda_imc + theta)

    return pid_control(Kc_imc, Ti_imc, Td_imc, setpoint, initial_value, t)
