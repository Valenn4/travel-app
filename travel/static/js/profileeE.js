window.addEventListener("load", e => {
    document.querySelector(".container").style.display = 'flex'
    document.querySelector(".load").style.display = 'none'
})
/* click publication */
document.querySelectorAll(".publication").forEach(p => {
    p.addEventListener("click", (e) => {
        if(e.target.getAttribute("id") != 'favorite'){
            location.href = `../publication/${p.id}`
        } else {
            let likes = p.childNodes[7].childNodes[3].textContent
            if(e.target.style.color=="red"){
                e.target.style.color = "white"
                p.childNodes[7].childNodes[3].textContent = Number(likes)-1
            } else {
                e.target.style.color = "red"
                p.childNodes[7].childNodes[3].textContent = Number(likes)+1
            }
        }
    })
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
document.querySelector(".close_image").addEventListener("click", () => {
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
                el.style.borderBottom = "2px solid white"
            }
        })
        document.querySelectorAll(".section").forEach(section => {
            if(el.getAttribute("class") == section.id){
                section.style.display="grid"
            } else {
                section.style.display="none"
            }
        })
    })
})
/* BUTTON FOLLOW */
document.querySelector(".follow").addEventListener("click", () => {
    id = document.querySelector(".follow").id
    const user = window.location.pathname.substring(9);
    url = ''
    if(document.querySelector("#DEBUG").value=='True'){
        url = `http://127.0.0.1:8000/api/v1/following/${id}`
    } else {
        url = `http://valenn2.pythonanywhere.com/api/v1/following/${id}`
    }
    fetch(url)
    .then(response => response.json())
    .then(json => {
        if(document.querySelector("#DEBUG").value=='True'){
            url = `http://127.0.0.1:8000/api/v1/user/${user}`
        } else {
            url = `http://valenn2.pythonanywhere.com/api/v1/user/${user}`
        }
        fetch(url)
        .then(response => response.json())
        .then(username => {
            if(json.following.followings.includes(username.id)){
                list = json.following.followings.filter(user => user != username.id)
                changeFollowings(id, {"followings":list})
                document.querySelector(".follow").innerHTML="Seguir"
            } else{
                json.following.followings.push(username.id)
                changeFollowings(id, json.following)
                document.querySelector(".follow").innerHTML="Siguiendo"
            }
        })
    })
})


function changeFollowings(user, list){
    csrftoken = document.cookie.substring(10)
    url = ''
    if(document.querySelector("#DEBUG").value=='True'){
        url = `http://127.0.0.1:8000/api/v1/following/${user}`
    } else {
        url = `http://valenn2.pythonanywhere.com/api/v1/following/${user}`
    }

    fetch(url, {
        method:'PUT',
        body:JSON.stringify({"following":list}),
        headers:{"Content-Type": 'application/json', "X-Csrftoken": csrftoken}
    })
    .then(response => response.json())
    .then(json => {
    })
}