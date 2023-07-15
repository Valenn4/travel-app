'use strict';
/* WINDOW ADD IMAGE */

document.querySelector(".file").addEventListener("change", event => {
	document.querySelector(".name_image").innerHTML = event.target.files[0].name
})