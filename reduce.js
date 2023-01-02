// array sum by using reduce()

const arraySum = (arr) => {
    const result = arr.reduce((a, b) => a + b);
    return result;
};

const array1 = [5, 7, 8, 40];
console.log(arraySum(array1))


// reverse string by using reduce()

const reverseStr = (str) => {
    const result = [...str].reduce((a, b) => {
        return b + a
    })
    return result;
};

const string = "hello";
console.log(reverseStr(string))




