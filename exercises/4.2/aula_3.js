// Laço for/of permite percorrer objetos iteráveis como arrays e Strings
// Laço for/of em array
let numeros = [1, 2, 3, 4, 5];
for(let numero of numeros) {
    console.log(numero);
}

console.log('\n');

// Laço for/of em string
let word = "Hello";
for(let letter of word) {
    console.log(letter);
}

console.log('\n');

// Laço for/of para somar um valar em cada elemento
let arrOfNumbers = [10, 20, 30];
for(let sum of arrOfNumbers) {
    sum += 1;
    console.log(sum);
}