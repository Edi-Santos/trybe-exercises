// Pegue cada um dos exercícios da primeira parte das nossas aulas de JavaScript e faça com que todos eles sejam funções de um mesmo arquivo. As variáveis que você define no começo de cada arquivo devem ser removidas e transformadas em parâmetros das funções. Por exemplo:

// Adição
// let a = 5;
// let b = 2;

// a + b;

// ... se transforma em:

// function sum(a, b) {
//     return a + b;
// }

// Adição
console.log('soma:');
function soma(a, b) {
    console.log(a + b);
};
soma(2, 8);
console.log('\n');


// Subtração
console.log('subtração:');
function subtr(a, b) {
    console.log(a - b);
};
subtr(6, 7);
console.log('\n');


// Multiplicação
console.log('multiplicação:');
function mult(a, b) {
    console.log(a * b);
};
mult(3, 8);
console.log('\n');


