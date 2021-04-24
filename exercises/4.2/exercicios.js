// Exercícios do bloco 4.2
let numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27];

// Exercícios 1 - Nesse primeiro exercício, percorra o array imprimindo todos os valores nele contidos com a função console.log();
console.log('Exercício 1:');
for(index = 0; index < numbers.length; index += 1) {
    console.log(numbers[index]);
}

console.log('\n');

// Exercício 2 - Para o segundo exercício, some todos os valores contidos no array e imprima o resultado;
console.log('Exercício 2:');
for(let sum of numbers) {
    sum += 1;
    console.log(sum);
}

console.log('\n');

// Exercício 3 - Para o terceiro exercício, calcule e imprima a média aritmética dos valores contidos no array;
console.log('Exercício 3:');
let somatorio = 0;
for(index = 0; index < numbers.length; index += 1) {
    somatorio = somatorio + numbers[index];
}
let media = somatorio / numbers.length;
console.log(`média = ${media}`);

console.log('\n');

// Exercício 4 - Com o mesmo código do exercício anterior, caso o valor final seja maior que 20, imprima a mensagem: "valor maior que 20". Caso não seja, imprima a mensagem: "valor menor ou igual a 20";
console.log('Exercício 4:');
if(media > 20) {
    console.log('valor maior que 20');
}else {
    console.log('valor menor ou igual a 20');
}

console.log('\n');

// Exercício 5 - Utilizando for , descubra qual o maior valor contido no array e imprima-o;
console.log('Exercício 5:');
let maiorNumero = 0;
for(index = 0; index < numbers.length; index += 1) {
    if(numbers[index] > maiorNumero) {
        maiorNumero = numbers[index];
    }
}
console.log(maiorNumero);

console.log('\n');

// Exercício 6 - Descubra quantos valores ímpares existem no array e imprima o resultado. Caso não exista nenhum, imprima a mensagem: "nenhum valor ímpar encontrado";
console.log('Exercício 6:');
let impar = 0;
for(index = 0; index < numbers.length; index += 1) {
    if(numbers[index] % 2 != 0) {
        impar += 1;
    }
}
console.log(impar);

console.log('\n');

// Exercício 7 - Utilizando for , descubra qual o menor valor contido no array e imprima-o;
console.log('Exercício 7:');
let menorNumero = maiorNumero;
for(index = 0; index < numbers.length; index += 1) {
    if(numbers[index] < menorNumero) {
        menorNumero = numbers[index];
    }
}
console.log(menorNumero);

console.log('\n');
// Exercício 8 - Utilizando for , crie um array que vá de 1 até 25 e imprima o resultado;
console.log('Exercício 8:');
let sequenciaNum = [];
for(index = 1; index <= 25; index += 1) {
    sequenciaNum.push(index);
}
console.log(sequenciaNum);