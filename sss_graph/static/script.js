let chart;

async function generateGraph() {
    const inputs = {
    family: {
        adults: parseInt(document.getElementById('adults').value),
        infants: parseInt(document.getElementById('infants').value),
        preschoolers: parseInt(document.getElementById('preschoolers').value),
        schoolagers: parseInt(document.getElementById('schoolagers').value),
        teenagers: parseInt(document.getElementById('teenagers').value),
    },
    housing: document.getElementById('housing').value,
    food_plan: document.getElementById('food_plan').value
    };

    const response = await fetch('/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(inputs)
    });

    const data = await response.json();

    let table = {
    labels: data.map(row => row.output),
    datasets: [{
        label: 'Monthly Costs ($)',
        data: data.map(row => row.values)}]
    } 

    //   const labels = data.map(row => row.output),
    //   const values = data.map(row => row.values);

    const ctx = document.getElementById('myChart').getContext('2d');
    if (chart) chart.destroy();

    chart = new Chart(ctx, {
    type: 'bar',
    data: table,
    // options: {
    //   scales: {y: {beginAtZero: true}}
    // }
});
}
