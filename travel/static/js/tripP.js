document.querySelector("#id_image").setAttribute("multiple", true)

document.querySelectorAll(".img_album").forEach(e => {
	e.addEventListener("click", i => {
		document.querySelector(".div_photo_window").innerHTML = ''
		document.querySelector(".div_photo_window").insertAdjacentHTML('beforeend', `
			<img src="../..${e.getAttribute("src")}"></img>
		`)
		document.querySelector(".window_photo").style.display = 'block'

	})
})

document.querySelector(".close_image").addEventListener("click", () => {
    document.querySelector(".window_photo").style.display = "none"
    document.querySelector("body").style.overflow = "auto"
})
/* WINDOW ADD IMAGE */
document.querySelector("#id_image").addEventListener("change", event => {
	document.querySelector(".name_image").innerHTML = event.target.files[0].name
})
/* CLICK BUTTON CONTINUE, IMAGES DUPLICATE */
document.querySelector(".button_continue").addEventListener("click", () => {
	document.querySelector(".result_form").style.display='none'
})