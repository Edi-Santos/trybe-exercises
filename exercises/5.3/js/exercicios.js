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