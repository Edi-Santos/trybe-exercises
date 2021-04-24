// Exercícios do bloco 4.2
let numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27];

// Exercícios 1 - Nesse primeiro exercício, percorra o array imprimindo todos os valores nele contidos com a função console.log() 
console.log('Exercício 1:');
for(index = 0; index < numbers.length; index += 1) {
    console.log(numbers[index]);
}

console.log('\n');

// Exercício 2 - Para o segundo exercício, some todos os valores contidos no array e imprima o resultado
console.log('Exercício 2:');
for(let sum of numbers) {
    sum += 1;
    console.log(sum);
}