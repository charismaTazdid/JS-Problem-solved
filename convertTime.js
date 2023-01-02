//task: convert 12 hrs format time to 24 hrs format time.
//given input: '1:20 PM' expected output: 13:20 PM
//given input: '12:30 AM' expected output: 00:30 AM

const convert12To24hoursFormat = (time12h) => {
    const [time, modifier] = time12h.split(" ");
    let [hours, minutes] = time.split(":");

    if (hours === "12") {
        hours = hours = "00"
    }
    if (modifier === "PM") {
        hours = parseInt(hours) + 12;
    }
    return `${hours}:${minutes}`
}
console.log(convert12To24hoursFormat('1:20 PM')) //expected output: 13:20 PM
console.log(convert12To24hoursFormat('2:50 PM')) //expected output: 14:50 PM
console.log(convert12To24hoursFormat('4:10 PM'))  //expected output: 16:10 PM
console.log(convert12To24hoursFormat('12:10 PM')) //expected output: 12:10 PM
console.log(convert12To24hoursFormat('12:30 AM')) //expected output: 00:30 AM
console.log(convert12To24hoursFormat('2:33 AM'))  //expected output: 2:33 AM
console.log(convert12To24hoursFormat('9:11 PM'))  //expected output: 00:30 PM



// Method 2

const convert12To24hours = (time12h) => {
    const time = time12h.split(" ")
    const modifier = time[1];
    let [hours, minutes] = time[0].split(":")

    if (hours === "12" && modifier === "AM") {
        hours = hours = "00"
    }
    if (hours !== "12" && modifier === "PM") {
        hours = parseInt(hours) + 12;
    }
    return `${hours}:${minutes} ${modifier}`
}

