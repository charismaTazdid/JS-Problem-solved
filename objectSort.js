//let's sorted an array of object with Ascending Order Descending Order


const products = [
    {
        name: 'Coffe',
        price: 180,
        id: 3,
    },
    {
        name: 'Tea',
        price: 80,
        id: 5,
    },
    {
        name: 'Cold Coffe',
        price: 220,
        id: 2,
    },
    {
        name: 'Chicken With Bred',
        price: 300,
        id: 12,
    },
    {
        name: 'Pepsi',
        price: 70,
        id: 43,
    }
]

const defaultSort = products.sort();

console.log('Default sorted', defaultSort) //nothing is change

const ascendingWithPrice = (a, b) => a.price - b.price;
const descendingWithPrice = (a, b) => b.price - a.price;

const ascendingValue = products.sort(ascendingWithPrice)
console.log("Ascending By Price", ascendingValue)

const descendigValue = products.sort(descendingWithPrice)
console.log("Descending By Price", descendigValue)


// Ascending and Descending By Id
const ascendingWithId = (a, b) => a.id - b.id;
const descendingWithId = (a, b) => b.id - a.id;

const ascendingValueById = products.sort(ascendingWithId);
console.log("Ascending By ID", ascendingValueById)

const descendingValueById = products.sort(descendingWithId);
console.log("Descending By ID", descendingValueById)