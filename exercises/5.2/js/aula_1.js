// Exercise 1 - Acesse o elemento elementoOndeVoceEsta.
let acces = document.getElementById('elementoOndeVoceEsta');
console.log(acces);

// Exercise 2 - Acesse pai a partir de elementoOndeVoceEsta e adicione uma color a ele.
let acces2 = document.getElementById('elementoOndeVoceEsta').parentNode;
acces2.style.background = 'Cyan';

// Exercise 3 - Acesse o primeiroFilhoDoFilho e adicione um texto a ele. Você se lembra dos vídeos da aula anterior, como fazer isso?
let firstSonOfSon = document.getElementById('primeiroFilhoDoFilho');
firstSonOfSon.innerHTML = 'Div primeiroFilhoDoFilho';

// Exercise 4 - Acesse o primeiroFilho a partir de pai.
let firstSonOfSonByFather = document.querySelector('#pai').firstElementChild;
console.log(firstSonOfSonByFather);

