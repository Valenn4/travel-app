window.addEventListener("load", e => {
    document.querySelector(".section").style.display = 'flex'
    document.querySelector(".load").style.display = 'none'
})

/* NEW MESSAGE */
document.querySelector("#id_message").setAttribute("rows", 0)
document.querySelector("#id_message").setAttribute("placeholder", "Escriba un mensaje")

document.querySelectorAll(".publication").forEach(p => {
    p.addEventListener("click", (e) => {
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