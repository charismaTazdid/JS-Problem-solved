const piChart = document.querySelector(".pichart");

document.querySelector('#inputHandler').addEventListener("input", (e) => {
    piChart.style = `--parcentage:${e.target.value}%`
})