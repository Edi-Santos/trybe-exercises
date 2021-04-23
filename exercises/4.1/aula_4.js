let nota = 75;
let result;

if (nota >= 80 && nota <= 100) {
    result = "aprovado";
}else if (nota >= 60 && nota < 80) {
    result = "lista";
}else if (nota < 60) {
    result = "reprovado";
}

switch (result) {
    case "aprovado":
        console.log("Parabéns, você foi aprovado!");
        break;

    case "lista":
        console.log("Você está na lista de espera.");
        break;

    case "reprovado":
        console.log("Você foi reprovado.");
        break;

    default:
        console.log("Valor inválido.");
}