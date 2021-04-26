// Exercício 1 - Faça cinco programas, um para cada operação aritmética básica. Seu programa deve ter duas variáveis, a e b , definidas no começo com os valores que serão operados. Faça programas para:
console.log('Exercício 1:');
let a = 5;
let b = 8;

let soma = a + b;
let subtr = a - b;
let mult = a * b;
let divide = a / b;
let mod = a % b;

console.log("adição = " + soma);
console.log("subtração = " + subtr);
console.log("multiplicação = " + mult);
console.log("divisão = " + divide);
console.log("modulação = " + mod);

console.log('\n');

// Exercício 2 - Faça um programa que retorne o maior de dois números. Defina no começo do programa duas variáveis com os valores que serão comparados.
console.log('Exercício 2:');
if(a > b) {
    console.log("a é maior que b");
}else {
    console.log("b é maior que a");
}

console.log('\n');

// Exercício 3 - Faça um programa que retorne o maior de três números. Defina no começo do programa três variáveis com os valores que serão comparados.
console.log('Exercício 3:');
let a3 = 15;
let b3 = 3;
let c3 = 16;

if(a3 > b3 && a > c3) {
    console.log("a3 é o maior número");
}else if(b3 > a3 && b3 > c3) {
    console.log("b3 é o maior número");
}else if(c3 > a3 && c3 > b3) {
    console.log("c3 é o maior número");
}else {
    console.log('Error!');
}

console.log('\n');

// Exercício 4 - Faça um programa que, dado um valor definido numa variável, retorne "positive" se esse valor for positivo, "negative" se for negativo e "zero" caso contrário.
console.log('Exercício 4:');
let a4 = -3;

if(a4 > 0) {
    console.log("positive");
}else if(a4 < 0) {
    console.log("negative");
}else {
    console.log("zero");
}

console.log('\n');
// Exercício 5 - Faça um programa que defina três variáveis com os valores dos três ângulos internos de um triângulo. Retorne true se os ângulos representarem os ângulos de um triângulo e false , caso contrário. Se algum ângulo for inválido o programa deve retornar uma mensagem de erro.
console.log('Exercício 5:');
let angulo1 = 60;
let angulo2 = -61;
let angulo3 = 60;
let triangulo;

if(angulo1 < 0 || angulo2 < 0 || angulo3 < 0) {
    triangulo = "erro";
}else if(angulo1 + angulo2 + angulo3 == 180){
    triangulo = "true";
}else if(angulo1 + angulo2 + angulo3 != 180) {
    triangulo = "false";
}

switch(triangulo) {
    case "true":
        console.log("true");
        break;
    case "false":
        console.log("false");
        break;
    default:
        console.log("error");
}

console.log('\n');

// Exercício 6 - Escreva um programa que receba o nome de uma peça de xadrez e retorne os movimentos que ela faz.
console.log('Exercício 6:');
let pecaXadrez = 'Rei';

switch(pecaXadrez.toLowerCase()) {
    case 'rei':
        console.log(`${pecaXadrez} - Uma casa para qualquer lado.`);
        break;
    case 'rainha':
        console.log(`${pecaXadrez} - Todo o tabuleiro para qualquer lado.`);
        break;
    case 'bispo':
        console.log(`${pecaXadrez} - Todo o tabuleiro em diagonal.`);
        break;
    case 'cavalo':
        console.log(`${pecaXadrez} - Formato de "L".`);
        break;
    case 'torre':
        console.log(`${pecaXadrez} - Todo o tabuleiro em vertical e horizontal.`);
        break;
    case 'peão':
        console.log(`${pecaXadrez} - Para frente. Primeiro movimento - Pode andar duas casas | A partir do segundo movimento - Pode andar uma casa.`);
        break;
    default:
        console.log('Valor inválido.');
}

console.log('\n');

// Exercício 7 - Escreva um programa que converte uma nota dada em porcentagem (de 0 a 100) em conceitos de A a F. Siga essas regras:
console.log('Exercício 7:');
let porcentagem = 70;

if(porcentagem >= 90 && porcentagem <= 100) {
    console.log('nota - A');
}else if(porcentagem < 90 && porcentagem >= 80) {
    console.log('nota - B');
}else if(porcentagem < 80 && porcentagem >= 70) {
    console.log('nota - C');
}else if(porcentagem < 70 && porcentagem >= 60) {
    console.log('nota - D');
}else if(porcentagem < 60 && porcentagem >= 50) {
    console.log('nota - E');
}else if(porcentagem < 50 && porcentagem >= 0) {
    console.log('nota - F');
}else {
    console.log('error');
}

console.log('\n');

// Exercício 8 - Escreva um programa que defina três números em variáveis e retorne true se pelo menos uma das três for par. Caso contrário, ele retorna false .
// Bonus: use somente um if.
console.log('Exercício 8')
let n1 = 7;
let n2 = 10;
let n3 = 1;

if(n1 % 2 == 0 || n2 % 2 == 0 || n3 % 2 == 0) {
    console.log('true');
}else {
    console.log('false');
}