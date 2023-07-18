// Problem: https://www.hackerrank.com/challenges/organizing-containers-of-balls


function organizingContainers(container) {
    // Write your code here
    let obj1 = {};
    let obj2 = {};
    for (let i = 0; i < container.length; i++) {
        obj1[i] = container[i].reduce((a, b) => a + b);
        obj2[i] = 0;
        for (let j = 0; j < container.length; j++) {
            obj2[i] += container[j][i];
        }
    }

    let x = Object.values(obj1).sort((a, b) => a - b);
    let y = Object.values(obj2).sort((a, b) => a - b);
    if (JSON.stringify(x) === JSON.stringify(y)) {
        return "Possible"
    } else {
        return "Impossible"
    }

}