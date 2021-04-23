// Exercício 1
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

// Exercício 2
if(a > b) {
    console.log("\n a é maior que b");
}else {
    console.log("\n b é maior que a");
}

// Exercício 3
let a3 = 15;
let b3 = 3;
let c3 = 16;

if(a3 > b3 && a > c3) {
    console.log("\n a3 é o maior número \n");
}else if(b3 > a3 && b3 > c3) {
    console.log("\n b3 é o maior número \n");
}else if(c3 > a3 && c3 > b3) {
    console.log("\n c3 é o maior número \n");
}else {
    console.log('\n Error!');
}

// Exercício 4
let a4 = -3;

if(a4 > 0) {
    console.log("positive \n");
}else if(a4 < 0) {
    console.log("negative \n");
}else {
    console.log("zero \n");
}