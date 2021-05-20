// Exercício 1 - Crie um irmão para elementoOndeVoceEsta .
let father = document.querySelector("#pai");

let creatingElement = document.createElement('div');
creatingElement.innerHTML = '<p>Criando irmão de elementoOndeVoceEsta</p>';
creatingElement.className = "adiciona-irmao";

father.appendChild(creatingElement);

// Exercício 2 - Crie um filho para elementoOndeVoceEsta.
let elementoOndeVoceEsta = document.getElementById("elementoOndeVoceEsta");

let creatingElement2 = document.createElement('div');
creatingElement2.innerHTML = '<p>Criando filho de elementoOndeVoceEsta</p>';
creatingElement2.className = 'adiciona-filho';

elementoOndeVoceEsta.appendChild(creatingElement2);

// Exercício 3 - Crie um filho para primeiroFilhoDoFilho.
let filhoDoFilho = document.getElementById('elementoOndeVoceEsta').firstElementChild;

let creatingElement3 = document.createElement('div');
creatingElement3.innerHTML = '<p>Criando filho do filho de elementoOndeVoceEsta';
creatingElement3.className = 'adiciona-filho-do-filho';

filhoDoFilho.appendChild(creatingElement3);

// Exercício 4 - A partir desse filho criado, acesse terceiroFilho.
console.log(document.querySelector('.adiciona-filho-do-filho').parentElement.parentElement.nextElementSibling);
