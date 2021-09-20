// Adicionando novas chaves e valores num objeto.

const customer1 = {
  firstName: 'Roberto',
  age: 22,
  job: 'Teacher',
};

console.log('Primeiro console:');
console.log(customer1);

customer1.lastName = 'Faria';
console.log('Segundo console:');
console.log(customer1);

const customer2 = {
  firstName: 'Maria',
  age: 23,
  job: 'Medic',
};

console.log('Terceiro console:');
console.log(customer2);
customer2['lastName'] = 'Silva';
console.log('Quarto console:');
console.log(customer2);

// Agora, para praticar, crie uma função que receba três parâmetros, sendo eles: um objeto, o nome de uma chave e o seu valor. O retorno dessa função deve ser o objeto já com a nova chave adicionada nele.

console.log('\n----------------------------------------------------------------\n');
console.log('Exercise:');

let object = {};

const addToObj = (obj, key, value) => {
  obj[key] = value;
  return object;
};

console.log(addToObj(object, 'name', 'Ed'));
