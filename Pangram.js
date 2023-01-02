//write a pangram string checker

const checkPangram = (str) => {

    if (str.length < 26) return false;

    const charArray = new Array(26).fill(false);

    let index;
    for (let i = 0; i < str.length; i++) {

        if (str[i] >= "A" && str[i] <= "Z") {
            index = str[i].charCodeAt() - "A".charCodeAt()
        }
        else if (str[i] >= "a" && str[i] <= "z") {
            index = str[i].charCodeAt() - "a".charCodeAt()
            console.log(index)
        }
        else {
            continue
        }
        charArray[index] = true;

    }

    for (let i = 0; i < charArray.length; i++) {
        if (charArray[i] === false) {
            return false
        }
    }
    return true;

    // Time complexity: O(n)
    // Space complexity: O(1)
}

const result = checkPangram(' A quick brown fox jumps over the lazy dog')
const result2 = checkPangram(' A quick brown jumps over the lazy dog')
console.log(result); //output: true
console.log(result2); //output: false

