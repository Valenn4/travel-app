let websocket = new WebSocket(`ws://${window.location.host}/ws/${window.location.pathname.split("/")[2]}/`)

websocket.onmessage = function(e){
    let data = JSON.parse(e.data)
    let list_messages = document.querySelector(".list_message")
    list_messages.insertAdjacentHTML("afterbegin", `<p>${e.target.user_connected.value}: ${JSON.parse(data.message)["message"]}</p>`)    
}

websocket.onopen = function(e){
    console.log("onOpen")
}
websocket.onclose = function(e){
    console.log("onClose")
}

let form = document.querySelector(".form")


form.addEventListener("submit", (e) => {
    

    const body = new FormData()
    body.append("message", e.target.message.value)
    body.append("created_by", e.target.user_connected.value)

    e.preventDefault()
    websocket.send(JSON.stringify({
        'message':e.target.message.value,
    })) 

    
    fetch(`../../new_message/${window.location.pathname.split("/")[2]}`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.cookie.substring(10)
        },
        body: body
    })
    .then(response => response.json())
    .then(json => json)
    form.reset()
})