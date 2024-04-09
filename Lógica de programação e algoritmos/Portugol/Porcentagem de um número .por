programa
{
	
	funcao inicio()
	{
		real valor, resultado, porcentagem
		caracter letra = 's' 
		enquanto (letra == 's'){
		escreva("digite o numero: ") 
		leia(valor)

		escreva("Digite a porcentagem: ") 
		leia(porcentagem) 

		resultado = valor * (porcentagem / 100) 

		escreva("\nO resultado de sua porcenatgem é: ", resultado) 

		escreva("\n Deseja continuar? [s/n] ")
		leia(letra) 
		limpa()
		
		
		
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 412; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */