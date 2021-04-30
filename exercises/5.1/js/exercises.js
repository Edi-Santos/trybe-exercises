// Header
let header = document.querySelector('header');
header.style.backgroundColor = 'rgb(79, 199, 95)';

let headerH1 = document.querySelector('header h1');
headerH1.style.background = 'rgb(79, 199, 95)'

// Section .emergency-tasks
let sectionET = document.querySelector('.emergency-tasks');
sectionET.style.background = 'rgb(248, 150, 150)';

let sectionETDiv = document.querySelectorAll('.emergency-tasks div');
for (let i = 0; i < sectionETDiv.length; i ++) {
    sectionETDiv[i].style.background = 'rgb(248, 150, 150)';
}

let sectionETH3 = document.querySelectorAll('.emergency-tasks h3');
for (let i = 0; i < sectionETH3.length; i++) {
    sectionETH3[i].style.background = 'rgb(165, 83, 147)';
}

// Section .no-emergency-tasks
let sectionNTE = document.getElementsByClassName('no-emergency-tasks');
sectionNTE[0].style.background = 'yellow';

let sectionNTEDiv = document.querySelectorAll('.no-emergency-tasks div');
for (let i = 0; i < sectionNTEDiv.length; i++) {
    sectionNTEDiv[i].style.background = 'yellow';
}

let sectionNTEH3 = document.querySelectorAll('.no-emergency-tasks h3');
for (let i = 0; i < sectionNTEH3.length; i++) {
    sectionNTEH3[i].style.background = 'black';
}
