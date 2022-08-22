
src="https://www.gstatic.com/charts/loader.js">

google.charts.load('current',{packages:['corechart']});
google.charts.setOnLoadCallback(convertTable);

function addFields(){
    // Generate a dynamic number of inputs
    var number = document.getElementById("numberofexercise").value;
    // Get the element where the inputs will be added to
    var container = document.getElementById("container");
    // Remove every children it had before
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
    for (i=0;i<number;i++){
        // Append a node with a random text
        container.appendChild(document.createTextNode("Exercise " + (i+1)));
        // Create an <input> element, set its type and name attributes
        var input = document.createElement("input");
        input.type = "text";
        input.name = "Exercise" + i;
        input.id = "Exercise" + i;
        container.appendChild(input);

        // Append a line break 
        container.appendChild(document.createElement("br"));
    }
}

function DoSubmit(){
    
    var workoutID = document.getElementById('workouts');
    //print(workoutID + "hello");
    alert("help");
    
}

function notEmpty(){

    var e = document.getElementById("field_6");
    var strUser = e.options[e.selectedIndex].label;
    document.getElementById('aggregator_name').innerHTML = strUser;
    
    }
notEmpty()
        
    document.getElementById("field_6").onchange = notEmpty;


    
function convertTable(){
    const table = document.querySelector('table')
    const arr = [...table.rows].map(r => [...r.querySelectorAll('td, th')].map(td => td.textContent))
    console.log(arr)
    var weightbydate = [];
    for (let i = 0; i<arr.length; i++){

        weightbydate.push([ arr[i][1], new Date(arr[i][3]) ]) // first index is row, second is column
        
    }
    
    document.getElementById("demo").innerHTML = weightbydate[0];

    var data = google.visualization.arrayToDataTable(weightbydate)
    
    // Set Options
    var options = {
        title: 'Weight Over Time',
        hAxis: {title: 'Date'},
        vAxis: {title: 'Weight'},
        legend: 'none'
    };
    // Draw Chart
    var chart = new google.visualization.LineChart(document.getElementById('myChart'));
    chart.draw(data, options);

}

