// Criando e verificando o tamanho do array
console.log("Criando e verificando o tamanho do array");

let tasksList = ['Tomar café', 'Reunião', 'Brincar com o cachorro'];

console.log(tasksList.length + "\n");


// Acessando arrays pelo seu índice
console.log("Acessando arrays pelo seu índice");

let searchForFirstTask = tasksList[0];
console.log(searchForFirstTask);

let searchForLastTask = tasksList[tasksList.length - 1];
console.log(searchForLastTask + "\n");


// Adicionando um elemento ao final da array
console.log("Adicionando um elemento ao final da array");

tasksList.push("Fazer exercícios da Trybe");
console.log(tasksList + "\n");


// Adicionando um elemento no início da array
console.log("Adicionando um elemento no início da array");

tasksList.unshift("Acordar cedo");
console.log(tasksList + '\n');


// Remover o último elemento
console.log('Remove o último elemento');

tasksList.pop();
console.log(tasksList + '\n');

// Remover o primeiro elemento
console.log('Remove o primeiro');

tasksList.shift();
console.log(tasksList + '\n');

// Acessa o índice do elemento pelo próprio elemento
console.log('Acessa o índice pelo elemento');

let indexOfTask = tasksList.indexOf('Reunião');
console.log(indexOfTask);
console.log('-----------------------------' + '\n');


// Exercícios
// Exercício 1 - Obtenha o valor "Serviços" do array menu 
console.log('Exercícios')
let menu = ['Home', 'Serviços', 'Portfólio', 'Links'];
let menuServices = menu[1];

console.log(menuServices);

// Exercício 2 - Procure o índice do valor "Portfólio" do array menu
let indexOfMenu = menu.indexOf('Portfólio');

console.log(indexOfMenu);