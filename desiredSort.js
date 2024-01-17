
const arr3 = [
    { name: "International", id: 30 },
    { name: "National", id: 34 },
    { name: "Sports", id: 3 },
    { name: "Entertainment", id: 55 },
    { name: "Politics", id: 38 },
    { name: "Education", id: 67 },
    { name: "Technology", id: 10 },
];

const customOrder = [67, 3, 55, 30, 34, 10, 38];

arr3.sort((a, b) => customOrder.indexOf(a.id) - customOrder.indexOf(b.id));

console.log(arr3);
