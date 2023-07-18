document.querySelector(".add_option").addEventListener("click", () => {
    if(document.querySelector(".add_window").getAttribute("style")=="display: none;"){
        document.querySelector(".add_window").style.display = "grid"
    } else {
        document.querySelector(".add_window").style.display = "none"
    }
})