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

// Exercise 5 - Agora acesse o primeiroFilho a partir de elementoOndeVoceEsta.
let firstSonByElem = document.getElementById('elementoOndeVoceEsta').previousElementSibling;
console.log(firstSonByElem);

// Exercise 6 - Agora acesse o texto Atenção! a partir de elementoOndeVoceEsta.
let textByElem = document.getElementById('elementoOndeVoceEsta').nextSibling;
console.log(textByElem);

// Exercise 7 - Agora acesse o terceiroFilho a partir de elementoOndeVoceEsta.
let thirdSonByElem = document.getElementById('elementoOndeVoceEsta').nextElementSibling;
console.log(thirdSonByElem);