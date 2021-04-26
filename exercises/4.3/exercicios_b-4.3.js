// Exercício 1 - Para o primeiro exercício de hoje, faça um programa que, dado um valor n qualquer, seja n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo:
/* 
n = 5

*****
*****
*****
*****
*****
*/
let n = 5;
let ast = '*';
let linha = '';

for(let i = 0; i < n; i += 1){
    linha = linha + ast;
    for(let ii = 0; ii < n; ii +=1) {
        console.log(linha);
    };
};

// Exercício 2 - Para o segundo exercício, faça o mesmo que antes, mas que imprima um triângulo retângulo com 5 asteriscos de base. Por exemplo:
/*
n = 5

*
**
***
****
*****
*/
let n2 = 5;
let ast2 = '*';
let linha2 = '';

for(let i = 0; i < n2; i += 1) {
    linha2 += ast2;
    console.log(linha2);
};