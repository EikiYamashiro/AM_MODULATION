# AM_MODULATION
Nesse projeto você irá construir uma aplicação que executa as seguintes tarefas, sequencialmente: 

1. Faça a leitura de um arquivo de áudio de poucos segundos previamente gravado com uma taxa de amostragem de 44100Hz. 

2. Normalize esse sinal (multiplicar o sinal por uma constante, de modo que as amplitudes fiquem dentro do intervalo [-1,1]). 

3. Reproduza o sinal e verifique que continua audível. 

4. Filtre as altas frequências desse sinal (frequências acima de 4000 Hz). 

5. Reproduza o sinal e verifique que continua audível (porém agora, sem as frequências altas, o som está mais “opaco”).

6. Module esse sinal de áudio em AM com portadora de 14000 Hz. 

7. Execute o sinal e perceba que não é mais audível. 

8. Construa o gráfico nos domínios do tempo e da frequência (Fourier) para os seguintes sinais: 

a. Sinal de áudio original. 
b. Sinal de áudio normalizado. 
c. Sinal de áudio filtrado. 
d. Sinal de áudio modulado. Verifique que o sinal modulado não ocupa frequências muito distantes de 14000Hz, ou seja, está dentro da uma suposta banda permitida. Nomeie os gráficos de maneira a ser possível saber o que se trada, por exemplo “Fourier do sinal modulado” .

9. Demodule o sinal usando a mesma portadora. 10. Execute o áudio do sinal demodulado e verifique que novamente é audível. 11. Mostre o gráfico no domínio do tempo e da frequência (Fourier) do sinal demodulado. Verifique que as frequências voltaram a ser baixas (região audível).
