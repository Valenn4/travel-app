window.addEventListener("load", e => {
    document.querySelector(".section_center").style.display = 'grid'
    document.querySelector(".load").style.display = 'none'
})

/* NEW MESSAGE */
document.querySelector("#id_message").setAttribute("rows", 0)
document.querySelector("#id_message").setAttribute("placeholder", "Escriba un mensaje")
