function createDaysOfTheWeek() {
  const weekDays = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
  const weekDaysList = document.querySelector('.week-days');

  for (let index = 0; index < weekDays.length; index += 1) {
    const days = weekDays[index];
    const dayListItem = document.createElement('li');
    dayListItem.innerHTML = days;

    weekDaysList.appendChild(dayListItem);
  };
};

createDaysOfTheWeek();

// Escreva seu código abaixo.
// Exercício 1 - Preencher o calendário com os dias do mês de forma dinâmica e adicionar classes para dias específicos.
function createDays() {
  let days = [];
  let takeDays = document.getElementById('days');

  for (let pushDay = 29; pushDay < 31; pushDay += 1) {
    days.push(pushDay);
  };

  for (let pushDay = 1; pushDay <= 31; pushDay += 1) {
    days.push(pushDay);
  };

  for (let index = 0; index < days.length; index += 1) {
    let createDayList = document.createElement('li');
    let monthDay = days[index];
    createDayList.innerHTML = monthDay;
    createDayList.className = 'day';
    
    if (monthDay === 24 || monthDay === 31) {
      createDayList.className = 'day holiday';
    } else if (monthDay === 4 || monthDay === 11 || monthDay === 18) {
      createDayList.className = 'day friday';
    } else if (monthDay === 25) {
      createDayList.className = 'day friday holiday';
    };

    takeDays.appendChild(createDayList);
  };
};
createDays();

// Exercício 2 - Implemente uma função que receba como parâmetro a string "Feriados" e crie dinamicamente um botão com o nome "Feriados".

// · Adicione a este botão a ID "btn-holiday" .
// · Adicione este botão como filho/filha da tag <div> com classe "buttons-container"
function createButton (string) {
  let takeBtnCont = document.querySelector('.buttons-container');
  let holidayButton = document.createElement('button');
  holidayButton.innerText = string;

  takeBtnCont.appendChild(holidayButton);
};
createButton('Feriados');

// Exercício 3 - Implemente uma função que adicione ao botão "Feriados" um evento de "click" que muda a cor de fundo dos dias que possuem a classe "holiday".

// · É interessante que este botão possua também a lógica inversa. Ao ser clicado novamente ele retorna à configuração inicial com a cor "rgb(238,238,238)".
let takeBtnFer = document.querySelector('.buttons-container button');

takeBtnFer.addEventListener('click', function() {
  let takeHoliday = document.getElementsByClassName('holiday');

  for (let index = 0; index < takeHoliday.length; index += 1) {

    if (takeHoliday[index].style.background != 'rgb(157, 223, 240)') {
      takeHoliday[index].style.background = 'rgb(157, 223, 240)';
    } else {
      takeHoliday[index].style.background = 'rgb(238,238,238)';
    };

  };
});

// Exercícios 4 - Implemente uma função que receba como parâmetro a string "Sexta-feira" e crie dinamicamente um botão com o nome "Sexta-feira".

// · Adicione a este botão o ID "btn-friday" .
// · Adicione este botão como filho/filha da tag <div> com classe "buttons-container".
function createBtnFriday(string) {
  let takeBtnCont = document.querySelector('.buttons-container');
  let createBtn = document.createElement('button');
  createBtn.innerHTML = string;
  
  createBtn.id = 'btn-friday';

  takeBtnCont.appendChild(createBtn);
}
createBtnFriday('Sexta-feira');
