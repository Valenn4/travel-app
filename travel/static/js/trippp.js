document.querySelector("#id_image").setAttribute("multiple", true)


/* WINDOW ADD IMAGE */
document.querySelector("#id_image").addEventListener("change", event => {
	document.querySelector(".name_image").innerHTML = event.target.files[0].name
})
/* CLICK BUTTON CONTINUE, IMAGES DUPLICATE */
document.querySelector(".button_continue").addEventListener("click", () => {
	document.querySelector(".result_form").style.display='none'
})