//Remove spaces from a given string and add "-" insted of empty space
// given input:  Hello World What's going on?
// expected output:  Hello-World-What's-going-on?

const parameterizeString = (str) => {
    let result = "";
    for (let i = 0; i < str.length; i++) {
        if (str[i] === " ") {
            result = result + "-"
        }
        else
            result = result + str[i]

    }
    return result
}

console.log(parameterizeString("Hello World What's going on?"))