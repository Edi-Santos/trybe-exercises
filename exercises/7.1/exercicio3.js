/* 
  Exercício 3 - Crie uma página que contenha:
    · Um botão ao qual será associado um event listener ;
    · Uma variável clickCount no arquivo JavaScript que acumule o número de clicks no botão;
    · Um campo no HTML que vá atualizando a quantidade de clicks no botão conforme a variável clickCount é atualizada.
*/

const pegaSpan = document.querySelector('span');
const pegaBtn = document.querySelector('button');

let vez = 0;
pegaBtn.addEventListener('click', () => {
  pegaSpan.innerHTML = vez += 1;
});
