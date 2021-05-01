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
