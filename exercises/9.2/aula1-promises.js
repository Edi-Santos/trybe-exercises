// Criando uma Promise e usando os parâmetros resolve e reject.

const promise = new Promise((resolve, reject) => {
  const number = Math.floor(Math.random() * 11);

  if (number <= 5) {
    return reject(console.log(`Que fracasso =( Nosso número foi ${number})`));
  }
  resolve(console.log(`Que sucesso =) Nosso número foi ${number}`));
});

