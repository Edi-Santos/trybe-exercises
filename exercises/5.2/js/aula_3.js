// Exercício 1 - Remova todos os elementos filhos de paiDoPai exceto pai, elementoOndeVoceEsta e primeiroFilhoDoFilho.

let removeFirst = document.getElementById('primeiroFilho');
removeFirst.remove();

let removeSonOfSon = document.getElementById('elementoOndeVoceEsta').lastElementChild;
removeSonOfSon.remove();

let removeThird = document.querySelector('#pai').firstElementChild.nextElementSibling;
removeThird.remove();

let removeFourth = document.getElementById('pai').lastElementChild;
removeFourth.remove();