function openAdd(){
    document.querySelector(".add_window").style.display = "grid"
    document.querySelector(".add_option").setAttribute("onclick", "closeAdd()")
}
function closeAdd(){
    document.querySelector(".add_window").style.display = "none"
    document.querySelector(".add_option").setAttribute("onclick", "openAdd()")
}