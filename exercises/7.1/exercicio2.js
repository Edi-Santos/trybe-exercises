/* 
Abaixo, você verá algumas especificações de algoritmos para desenvolver. É fundamental que você utilize o que aprendeu sobre let, const, arrow functions, template literals e ternary operator.
	Exercício 1 - Crie uma função que receba um número e retorne seu fatorial.
		· Na matemática, o fatorial de um número não negativo N, com a notação N!, é o produto de todos os inteiros menores ou iguais a N. Exemplo: 4! = 4 * 3 * 2 * 1 = 24.
		· Bônus (opcional): tente fazer o mesmo exercício de forma recursiva. Spoiler: É possível resolver com uma linha usando ternary operator.
*/

const fatorial = (numero) => {
	let numAtual = 0;
	let result = 1;
	
	for (let i = 1; i <= numero; i += 1) {
		numAtual = i;
		result *= numAtual;
	};
	
	return result;
}

console.log(fatorial(10));

/* 
	Exercício 2 - Crie uma função que receba uma frase e retorne qual a maior palavra.
		· Exemplo:
			» longestWord("Antônio foi no banheiro e não sabemos o que aconteceu") // retorna 'aconteceu'
 */

const longestWord = _ => {
	let separando = _.split(' ');
	let maiorPalavra = '';

	for (let index = 0; index < separando.length; index += 1) {
		if (maiorPalavra.length < separando[index].length) {
			maiorPalavra = separando[index];
		}
	}

	return maiorPalavra;
};

console.log(`A maior palavra da frase é: ${longestWord('Antônio foi no banheiro e não sabemos o que aconteceu')}`);
