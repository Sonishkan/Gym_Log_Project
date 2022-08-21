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
        