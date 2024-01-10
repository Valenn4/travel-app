var paginaAnterior = document.referrer;
if(document.querySelector("#DEBUG").value=='False'){
	var ultimaParte = paginaAnterior.substring(paginaAnterior.indexOf(".com")+4);
} else {
	var ultimaParte = paginaAnterior.substring(paginaAnterior.indexOf("8000")+4);
}
document.querySelector(".back").addEventListener("click", () => {
	if(paginaAnterior == ''){
		location.href = `../feed`
	} else {
		location.href = `../..${ultimaParte}`
	}
})
document.querySelectorAll(".img_album").forEach(e => {
	e.addEventListener("click", i => {
		document.querySelector(".input_name").setAttribute("value", e.id)
		document.querySelector(".div_photo_window").innerHTML = ''
		document.querySelector(".div_photo_window").insertAdjacentHTML('beforeend', `
			<img src='../..${e.getAttribute("src")}' id="${e.id}"></img>
		`)
		document.querySelector(".window_photo").style.display = 'block'
		document.querySelector("body").style.overflow = "hidden"

	})
})

function closeImage(){
	document.querySelector(".window_photo").style.display = "none"
    document.querySelector("body").style.overflow = "auto"
}
document.querySelector("#id_image").setAttribute("multiple", true)

/* WINDOW ADD IMAGE */
document.querySelector("#id_image").addEventListener("change", event => {
	document.querySelector(".name_image").innerHTML = event.target.files[0].name
})
/* CLICK BUTTON CONTINUE, IMAGES DUPLICATE */
document.querySelector(".button_continue").addEventListener("click", () => {
	document.querySelector(".result_form").style.display='none'
})