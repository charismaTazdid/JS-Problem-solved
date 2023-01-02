// this keyword output 


const student = {
    name: 'Raihan Tazdid',

    welcome() {
        return `Hello ${this.name}`
    },
    goodBy: () => {
        return `Good By ${this.name}` //here name will be undefined, goodBy consider as property, not a method.
    }
}

console.log(student.welcome()) //output: Hello Raihan Tazdid
console.log(student.goodBy()) //output: Good By undefined

