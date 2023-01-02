
function reverseString(str) {
    const [first, ...rest] = str;
    let result = first;
    if (rest.length) {
       let tempFirst =  reverseString(rest);
       result = tempFirst + result;
    }
    return result;
};

console.log(reverseString("hello"))