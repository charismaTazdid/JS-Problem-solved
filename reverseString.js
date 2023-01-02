// write a function to reverse a string
// 10 different way to reverse a string


//Reverse a String Using for Loop
function reverseStr(str) {
    let reversed = "";
    for (let i = 0; i < str.length; i++) {
        reversed = str[i] + reversed;
    }
    return reversed;
};
//or
function reverseStr2(str) {
    let result = "";
    for (let i = str.length - 1; i >= 0; i--) {
        result += str[i]
    }
    return result;
};


//Reverse a String With Built-In Functions
function reverseStr3(str) {
    return str.split("").reverse().join("");
};
//or
function reverseStr4(str) {
    return [...str].reverse().join("");
};


// Reverse a String using reduce()

function reverseStr5(str) {
    return [...str].reduce((a, b) => b + a);
};
//or
function reverseStr6(str) {
    return str.split("").reduce((acc, curr) => curr + acc);
};
//or
function reverseStr7(str) {
    return [...str].reduceRight((acc, curr) => acc + curr)
};


// Reverse a String using recursion

function reverseByRecursion(str) {
    let [result, ...rest] = str;
    if (rest.length) {
        return reverseByRecursion(rest) + result;
    };
    return result;
    
};

// OR
const reverseStrByRecursion = (str) => {
    const [first, ...rest] = str;
    let result = first
    if (rest.length) {
        let tempResult = reverseStr(rest)
        result = tempResult + result
    }
    return result;
};
// recursion works like LIFO structure 



let string = "hello"
console.log(reverseStr(string));
console.log(reverseStr2(string));
console.log(reverseStr3(string));
console.log(reverseStr4(string));
console.log(reverseStr5(string));
console.log(reverseStr6(string));
console.log(reverseStr7(string));
console.log(reverseByRecursion(string));
console.log(reverseStrByRecursion(string));
