
const numbers = [34, 4, 32, 22, 7, 1, 345, 12, 7, 89, 900];

const defaultSort = numbers.sort();

console.log(defaultSort);
//Default sorted output: [1, 12, 22, 32, 34, 345, 4, 7, 7, 89, 900]
//here all number(element) consider as string and sorted as string

const ascendingOrder = (a, b) => a - b;
const descendingOrder = (a, b) => b - a;

const ascendingValue = numbers.sort(ascendingOrder);
console.log(ascendingValue);  //ascendig output: [1, 4, 7, 7, 12, 22, 32, 34, 89, 345, 900]

const descendigValue = numbers.sort(descendingOrder);
console.log(descendigValue); //descendig output: [900, 345, 89, 34, 32, 22, 12, 7, 7, 4, 1]

