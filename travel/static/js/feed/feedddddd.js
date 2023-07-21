document.querySelector(".publications").style.display = 'none'
window.addEventListener("load", e => {
    document.querySelector(".publications").style.display = 'flex'
    document.querySelector(".load").style.display = 'none'
})

/* NEW MESSAGE */
document.querySelector("#id_message").setAttribute("rows", 0)
document.querySelector("#id_message").setAttribute("placeholder", "Escriba un mensaje")
