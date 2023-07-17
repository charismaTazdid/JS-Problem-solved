// Problem: https://www.hackerrank.com/challenges/missing-numbers/


function missingNumbers(arr, brr) {

    for (let i = 0; i < arr.length; i++) {
        const INDEX = brr.indexOf(arr[i]);

        if (INDEX !== -1) {
            brr.splice(INDEX, 1);
        }
    }

    const RESULT = [...new Set(brr.sort((a, b) => a - b))];
    return RESULT;
}