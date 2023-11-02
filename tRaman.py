# Determinação da temperatura por Espectroscopia Raman.
# Autor: Pojucan M.M.S.
# Data: 2019/11/03

# Vilarejo # Conservatória

# biblioteca para calculo:
import math

# Dados de entrada
ins = float(input('\nDigite o valor da intensidade Stokes do pico: '))
inas = float(input('\nDigite o valor da intensidade anti-Stokes do pico: '))

# condições de contorno:
h = 6.62607015e-34      # J.s
# Is=45.0523            Intensidade stokes do pico
# Ias=17.8961           Intensidade anti-stokes do pico 
kb = 1.38065e-23          #J/K
llnm = 633                #comprimento de onda do laser (nm) 
k = 218                   #número de onda (cm-1) 
c = 299792458           #velocidade da luz (m/s)

# Calculos parciais:
pi = math.asin(1.0)*2.0 # valor de pi em radianos        
llm = llnm*10**-9         # conversao do comprimento de onda (nm) para (1/metros)
km = k*(1/(10**-2))       # conversao do numero de onda em (1/metros)
lvm = 1/km                # calculo do comprimento de onda de vibração em (1/metros)
r = ins/inas

# Calculos dos Logaritmos neperianos dos termos:
lnsas = math.log(r)
lnl = math.log((((1/llm)-(1/lvm))**4)/(((1/llm)+(1/lvm))**4))
T = h*c*km/(kb*(lnsas-lnl))

# Saída do programa:
print ('\nPrograma tRaman - Cálculo da temperatura da amostra')
print ('Autor: Pojucan M.M.S.')
print ('Data: 2019/11/03')
print ('\nDados de entrada:')
print ('Constante de planck',h)
print ('Intensidade stokes',ins)
print ('Intensidade anti-stokes',inas)
print ('Constante de Boltzman',kb)
print ('Comprimento de onda do laser:',llnm,('(nm)'))
print ('Número de onda:',k,('(1/cm)'))
print ('Velocidade da luz no vácuo:',c,('(m/s)'))
print ('\nCálculos auxiliares:')
print ('Valor de pi:',pi,('radianos'))
print ('Comprimento de onda do laser:',llm,('(metros)'))
print ('Valor do número de onda:', km,('(metros)'))
print ('Comprimento de onda vibracional:',lvm,('(metros)'))
print ('Razão entre a Intensidade Stokes / Intensidade anti-Stokes:',r)
print ('Logaritmo da Intensidade Stokes / Intensidade anti-Stokes',lnsas)
print ('Logaritmo do termo com as frequencias laser & vibracional',lnl)
print ('\nResultado do cálculo principal:')
print ('A temperatura da amostra é:',T,('(Kelvin)'))
