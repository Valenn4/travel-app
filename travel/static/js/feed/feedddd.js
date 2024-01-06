 
window.addEventListener("load", e => {
    document.querySelector(".section").style.display = 'flex'
    document.querySelector(".load").style.display = 'none'
})

/* NEW MESSAGE */
document.querySelector("#id_message").setAttribute("rows", 0)
document.querySelector("#id_message").setAttribute("placeholder", "Escriba un mensaje")

function like_publication(){
    
}
document.querySelectorAll(".publication").forEach(p => {
    p.addEventListener("click", (e) => {
        const body = new URLSearchParams()
        body.append("likes", Number(document.querySelector(".id_user").innerHTML))
        csrftoken = document.cookie.substring(10)

        fetch(`http://127.0.0.1:8000/api/v1/publication/${p.id}`, {
            method: 'PUT',
            body: body,
            headers:{"X-Csrftoken": csrftoken}
        })
        .then(response => response.json())
        .then(json => {
            console.log(json)
        })
        if(e.target.getAttribute("id") != 'favorite'){
            location.href = `../publication/${p.id}`
        } else {
            let likes = p.childNodes[7].childNodes[3].textContent
            if(e.target.style.color=="red"){
                e.target.style.color = "white"
                p.childNodes[7].childNodes[3].textContent = Number(likes)-1
            } else {
                e.target.style.color = "red"
                p.childNodes[7].childNodes[3].textContent = Number(likes)+1
            }
        }
    })
})