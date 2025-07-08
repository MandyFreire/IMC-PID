import numpy as np
import matplotlib.pyplot as plt
from model import process_model
from controller import pid_control, imc_pid_control

# Parâmetros do sistema
Kp_process = 2.5
tau_process = 50.0
theta_process = 10.0
lambda_imc = 10.0

# Tempo de simulação
t = np.linspace(0, 200, 1000)

# Simulação
y_pid_simulation = pid_control(3.0, 40.0, 8.0, 1.0, 0.0, t)
y_imc_pid_simulation = imc_pid_control(Kp_process, tau_process, theta_process, lambda_imc, 1.0, 0.0, t)

# Plotar resultados
plt.figure(figsize=(12, 6))
plt.plot(t, y_pid_simulation, label='PID Clássico', color='blue')
plt.plot(t, y_imc_pid_simulation, label='IMC-PID', color='green')
plt.xlabel('Tempo')
plt.ylabel('Resposta do Sistema')
plt.title('Comparação: PID Clássico vs IMC-PID')
plt.legend()
plt.grid(True)
plt.show()
