# coding: utf-8
import matplotlib.pyplot as plt
X = [135, 145, 155, 165, 175, 185, 195]
freq = [0, 8, 9, 20, 1, 2, 0]
plt.plot(X, freq, color='maroon')
plt.savefig("grafico_01.png")
plt.show()


#Comentário
plt.grid(color='maroon', linestyle=':', axis='y')
plt.plot(X, freq, color='maroon')
plt.savefig("grafico_02.png)
plt.savefig("grafico_02.png")
plt.show()


#Comentário
plt.plot(X, freq, color='maroon', marker='V')
plt.plot(X, freq, color='maroon', marker='^')
plt.savefig("grafico_03.png")
plt.show()


#Comentário
eixos = plt.gca()
eixos.spines['top'].set_color('pink')
plt.grid(color='maroon', linestyle=':', axis='y')
plt.plot(X, freq, color='maroon', marker='^')
plt.show()
get_ipython().magic('save Aula02.py 1-27')
