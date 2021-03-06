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

/* 
	Exercício 4 - Crie um código JavaScript com a seguinte especificação:
Não se esqueça de usar template literals
		· Função 1 : Escreva uma função que vai receber uma string como parâmetro. Sua função deverá procurar pela letra x em uma string qualquer que você determinar e substituir pela string que você passou como parâmetro. Sua função deve retornar essa nova string .
		Exemplo:
		· String determinada: "Tryber x aqui!"
		· Parâmetro: "Bebeto"
		· Retorno: "Tryber Bebeto aqui!"
		
	· Um array com escopo global, que é o escopo do arquivo JS , nesse caso, contendo cinco strings com suas principais skills .
	· Função 2 : Escreva uma função que vai receber a string retornada da Função 1 como parâmetro. Essa função deve concatenar as skills do array global à string que foi passada para a Função 2 via parâmetro. Você deve ordenar os skills em ordem alfabética. Sua função deve retornar essa nova string .
	Exemplo: "Tryber x aqui! Minhas cinco principais habilidades são:
		· JavaScript;
		· HTML; ... #goTrybe".
*/

const trocaPalavra = palavra => {
	let chamada = 'Tryber x aqui';

	for (let index = 0; index < chamada.length; index += 1) {
		if (chamada[index] === 'x') {
			chamada = `Tryber ${palavra} aqui!`;	
		};
	};

	return chamada;
};

console.log(trocaPalavra('Ed'));

let array = ['HTML5', 'CSS3', 'JavaScript', 'Bootstrap', 'Git'];

array.sort();

const sobreMim = (nome, callback) => {
	return `\n${callback(nome)} Minhas cinco principais habilidades são:
${array}
#goTrybe`;
};

console.log(sobreMim('Ed', trocaPalavra));
