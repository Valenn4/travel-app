document.querySelectorAll(".publication").forEach(p => {
    p.addEventListener("click", (e) => {
        const body = new URLSearchParams()
        body.append("likes", Number(document.querySelector(".id_user").innerHTML))
        csrftoken = document.cookie.substring(10)

        if(e.target.getAttribute("id") != 'favorite'){
            location.href = `../../publication/${p.id}`
        } else {
            if(document.querySelector("#DEBUG").value=='True'){
                url = `http://127.0.0.1:8000/api/v1/publication/${p.id}`
            } else {
                url = `https://valenn2.pythonanywhere.com/api/v1/publication/${p.id}`
            }
            fetch(url, {
            method: 'PUT',
            body: body,
            headers:{
                "X-Csrftoken": csrftoken
            }
            })
            .then(response => response.json())
            .then(json => {
                console.log(json)
            })
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