function ehPar(value) {
    return value % 2 == 0;
}
  
function ehImpar(value) {
    return value % 2 !== 0;
}
 
function ehPositivo(value) {
    return value > 0;
}
  
function ehNegativo(value) {
    return value < 0;
}
  
numero = Array(5);

numero[0] = gets();
numero[1] = gets();
numero[2] = gets();
numero[3] = gets();
numero[4] = gets();

var pares = numero.filter(ehPar);
var impares = numero.filter(ehImpar);

var positivos = numero.filter(ehPositivo);
var negativos = numero.filter(ehNegativo);

print(pares.length + " valor(es) par(es)");
print(impares.length + " valor(es) impar(es)");
print(positivos.length + " valor(es) positivo(s)");
print(negativos.length + " valor(es) negativo(s)");