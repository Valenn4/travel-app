/* click trip */
document.querySelectorAll(".trip").forEach(el => {
    el.addEventListener("click", () => {
        window.location.href = `../trip/${el.id}`
    })
})
/* open and close window photo */
document.querySelector(".photo_profile").addEventListener("click", () => {
    document.querySelector(".window_photo").style.display = "flex"
    document.querySelector("body").style.overflow = "hidden"
})
document.querySelector(".close").addEventListener("click", () => {
    document.querySelector(".window_photo").style.display = "none"
    document.querySelector("body").style.overflow = "auto"
})

/* options click */
if(document.querySelector(".my_trips_section").getAttribute("style")=="display:flex;"){
    document.querySelector(".my_trips").style.borderBottom = "2px solid black"
} else {
    document.querySelector(".my_messages").style.borderBottom = "2px solid black"
}
document.querySelectorAll(".options p").forEach(el => {
    el.addEventListener("click", () => {
        document.querySelectorAll(".options p").forEach(x => {
            if(el != x){
                x.style.borderBottom = "none"
            } else {
                el.style.borderBottom = "2px solid black"
            }
        })
        document.querySelectorAll(".section").forEach(section => {
            if(el.getAttribute("class") == section.id){
                section.style.display="flex"
            } else {
                section.style.display="none"
            }
        })
    })
})


/* NEW MESSAGE */
document.querySelector("#id_message").setAttribute("rows", 0)
document.querySelector("#id_message").setAttribute("placeholder", "Escriba un mensaje...")