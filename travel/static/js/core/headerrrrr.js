/* ADD WINDOW */
function openAdd(){
    document.querySelector(".add_window").style.display = "grid"
    document.querySelector(".add_option").setAttribute("onclick", "closeAdd()")
}
function closeAdd(){
    document.querySelector(".add_window").style.display = "none"
    document.querySelector(".add_option").setAttribute("onclick", "openAdd()")
}

/* SEARCH WINDOW */
document.querySelector(".search").addEventListener("click", () => {
    document.querySelector(".input_result").value=''
    document.querySelector(".not_results").innerHTML = ''
    document.querySelector(".search_window").style.display = 'block'
})
document.querySelector(".close").addEventListener("click", () => {
    document.querySelector(".search_window").style.display = 'none'
})

document.querySelector(".form_search").addEventListener("submit", (e)=>{
    document.querySelector(".list_users").innerHTML = ''
    document.querySelector(".not_results").innerHTML = ''
    e.preventDefault()

    /*fetch(`http://127.0.0.1:8000/api/v1/users/${e.target.result.value}`)*/
    fetch(`http://valenn2.pythonanywhere.com/api/v1/users/${e.target.result.value}`)
    .then(response => response.json())
    .then(json =>{
        if(json.length == 0){
            document.querySelector(".not_results").innerHTML = 'No hubo coincidencias'
        } else {
            json.forEach(el => {
                document.querySelector(".not_results").innerHTML = ''
                node_li = document.createElement("li")
                node_li.setAttribute("class", "option")

                node_a = document.createElement("a")
                const textnode_a = document.createTextNode(el.username)
                node_a.appendChild(textnode_a)
                node_a.setAttribute("href", `../profile/${el.username}`)
                node_li.appendChild(node_a)

                document.querySelector(".list_users").appendChild(node_li)
            })
        }
    })
    .catch(err => console.log('Solicitud fallida', err));
})
