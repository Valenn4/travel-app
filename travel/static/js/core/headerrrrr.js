/* ADD */
function openAdd(){
    document.querySelector(".add_trip").style.display = "block"
    document.querySelector(".add_message").style.display = "block"
    document.querySelector(".add").setAttribute("onclick", "closeAdd()")
    document.querySelector(".add").setAttribute("class","fa-solid fa-xmark add")
}
function closeAdd(){
    document.querySelector(".add_trip").style.display = "none"
    document.querySelector(".add_message").style.display = "none"
    document.querySelector(".add").setAttribute("onclick", "openAdd()")
    document.querySelector(".add").setAttribute("class","fa-solid fa-plus add")
}

/* add message */
document.querySelector(".add_message").addEventListener("click", () => {
    document.querySelector(".new_message").style.display="block"
})
document.querySelector(".new_message .close").addEventListener("click", () => {
    document.querySelector(".new_message").style.display="none"    
})
/* add trip */
document.querySelector(".add_trip").addEventListener("click", () => {
    document.querySelector(".new_trip").style.display="block"
})
document.querySelector(".new_trip .close").addEventListener("click", () => {
    document.querySelector(".new_trip").style.display="none"    
})

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
    document.querySelector(".list_countries").innerHTML = ''
    document.querySelector(".not_results").innerHTML = ''
    e.preventDefault()

    if(document.querySelector(".input_result").value.length > 3){
        getUsers(e)
        getCountries()
    }
})

function getUsers(e){
    url = ''
    if(document.querySelector("#DEBUG").value=='True'){
        url = `http://127.0.0.1:8000/api/v1/users/${e.target.result.value}`
    } else {
        url = `http://valenn2.pythonanywhere.com/api/v1/users/${e.target.result.value}` 
    }
    fetch(url)
    .then(response => response.json())
    .then(json =>{
        if(json.length == 0){
            document.querySelector(".users_results").style.display='none'
        } else {
            document.querySelector(".users_results").style.display='flex'
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
}
function getCountries(){
    include = document.querySelector(".input_result").value
    url = 'https://restcountries.com/v3.1/all'
    fetch(url)
    .then(response => response.json())
    .then(json =>{
        countries = json.filter(el => el.name.common.toLowerCase().includes(include.toLowerCase()))
        if(countries.length == 0){
            document.querySelector(".countries_results").style.display='none'
        } else {
            document.querySelector(".countries_results").style.display='flex'
            countries.forEach(el => {
                    document.querySelector(".not_results").innerHTML = ''
                    node_li = document.createElement("li")
                    node_li.setAttribute("class", "option")

                    node_a = document.createElement("a")
                    const textnode_a = document.createTextNode(el.name.common)
                    node_a.appendChild(textnode_a)
                    /*node_a.setAttribute("href", `../profile/${el.username}`)*/
                    node_li.appendChild(node_a)

                    document.querySelector(".list_countries").appendChild(node_li)
                
            })
        }
    })
    .catch(err => console.log('Solicitud fallida', err));
    
}
