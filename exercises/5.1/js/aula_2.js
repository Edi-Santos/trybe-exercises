// Adicione uma classe igual para os dois parágrafos.

// Exercício 1 - Recupere os seus parágrafos via código JavaScript, usando a função getElementsByClassName;
let prg = document.getElementsByClassName("paragraph");
console.log(prg)

// Exercício 2 - Altere algum estilo do primeiro deles.
prg[0].style.fontFamily = 'monospace';

// Exercício 3 - Recupere o subtítulo e altere a cor dele usando a função getElementsByTagName .
document.getElementsByTagName('h4')[0].style.color = 'purple';
