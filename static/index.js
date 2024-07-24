function fact() {
    let xhr = new XMLHttpRequest();

    xhr.open("GET", `/factorial/${$("#num").val()}`)

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            $("#result").html(xhr.response);
        }
    }

    xhr.send();
}

function average() {
    let xhr = new XMLHttpRequest();

    let params = `?x=${$("#num1").val()}&y=${$("#num2").val()}`

    xhr.open("GET", `/avg${params}`)

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            $("#result2").html(xhr.response);
        }
    }

    xhr.send();
}

function validation() {
    let username = document.getElementById("username")
    let submitButton = document.getElementById("submitButton")
    let username_error = document.getElementById("error_username")
    let password = document.getElementById('password')
    if (username.value == "") {
        username.style.border = "1px solid red"
        username.style.color = "red"
        username_error.textContent = "Username is Required";
        username_error.style.color = "red"
        submitButton.style.display = "none"
    }  else {
        if (username.value.length < 5) {
            username_error.innerHTML = "Username is too short"
            username_error.style.color = "#FF0000"
        } else if (username.value == password.value){
            username_error.textContent = "Username and password cannot match"
            username_error.style.color = "red"
            
        } else {
            submitButton.style.display = "block"
            username.style.border = "1px solid black"
            username.style.color = "black"
            username_error.textContent = ""
        }
    } 
}

function removeEntry(){
    console.log(document.getElementById("removeButton").getAttribute("data-id"));
}



function addNewFriends(){
    let content = document.getElementById("friendInput").value 
    fetch("/api/people", {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(content)
    })
}