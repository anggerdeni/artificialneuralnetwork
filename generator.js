var dataSet = []


function toggleData(id){
    var btn = document.getElementById(id);
    if(btn.style["background-color"] == "white"){
        btn.style["background-color"] = "black";
    } else {
        btn.style["background-color"] = "white";
    }
}

function generateData(){
    var btn;
    var symbol = document.getElementById("symbol").value;
    var arr = symbol;
    for( i=0; i<81; i++){
        btn = document.getElementById(i);
        arr += (btn.style["background-color"] == "black") ? '1': '0';
    }
    dataSet.push(arr);
    console.log(dataSet);
}

function clearBtn(){
    var btn;
    for( i=0; i<81; i++){
        btn = document.getElementById(i);
        btn.style["background-color"] = "white";
    }
}