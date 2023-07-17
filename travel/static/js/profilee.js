document.querySelector(".section").style.display = 'none'
window.addEventListener("load", e => {
    document.querySelector(".section").style.display = 'flex'
    document.querySelector(".load").style.display = 'none'
})

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