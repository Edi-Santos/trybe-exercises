// Exercício 1 - Crie um irmão para elementoOndeVoceEsta .
let father = document.querySelector("#pai");

let creatingElement = document.createElement('div');
creatingElement.innerHTML = '<p>Criando irmão de elementoOndeVoceEsta</p>';
creatingElement.id = "adiciona-irmao";

father.appendChild(creatingElement);