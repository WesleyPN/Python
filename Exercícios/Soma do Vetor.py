"""
Soma do Vetor

Modifique o código abaixo, adicionando o código da função soma_vetor, 
que recebe como parâmetros um inteiro n e um ponteiro para um vetor de inteiros v 
e deve retornar um int: a soma dos nn elementos do vetor v. 
Vale ressaltar que você pode trabalhar com o ponteiro para o vetor 
exatamente da mesma maneira que faria se trabalhasse diretamente com o vetor.

#include <iostream>

using namespace std;

int soma_vetor(int n, int v[]){
	// Seu código aqui.
}

int main(){
	
	int n, v[100100];
	cin >> n;
	
	for(int i=0;i<n;i++)
		cin >> v[i];

	cout << soma_vetor(n,v) << "\n";
}

Entrada

A entrada do seu programa terá duas linhas: a primeira delas terá um único inteiro n, 
e a segunda terá os n elementos v[i] do vetor v.
Saída

Seu programa deve imprimir na saída padrão uma única linha contendo a soma dos elementos do vetor.
Restrições

    1<=n<=10^5
    -10^4<=v[i]<=10^4
"""
#----------------------------------------------------------------------------------------------
def soma_vetor(n=0, v=list()):
    soma = 0
    for i in range(0, n):
        soma += int(v[i])
    return str(soma)
	

n = 0
v = list()
n = int(input("Digite a quantidade de elementos do vetor: "))

for i in range(0, n):
    v.append(int(input(f"Digite o elemento no indice {i} do vetor: ")))

print(soma_vetor(n,v)+"\n")
#----------------------------------------------------------------------------------------------
