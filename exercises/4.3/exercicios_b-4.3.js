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
let a = '*';
let linha = '';

for(let i = 0; i < n; i += 1){
    linha = linha + a;
    for(let ii = 0; ii < n; ii +=1) {
        console.log(linha);
    };
};
