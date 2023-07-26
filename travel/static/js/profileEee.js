window.addEventListener("load", e => {
    document.querySelector(".profile").style.display = 'block'
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
/* BUTTON FOLLOW */
document.querySelector(".follow").addEventListener("click", () => {
    id = document.querySelector(".follow").id
    const user = window.location.pathname.substring(9);
    /*fetch(`http://127.0.0.1:8000/api/v1/following/${id}`)*/
    fetch(`http://valenn2.pythonanywhere.com/api/v1/following/${id}`)
    .then(response => response.json())
    .then(json => {
        /*fetch(`http://127.0.0.1:8000/api/v1/user/${user}`)*/
        fetch(`http://valenn2.pythonanywhere.com/api/v1/user/${user}`)
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
    /*fetch(`http://127.0.0.1:8000/api/v1/following/${user}`*/
    fetch(`http://valenn2.pythonanywhere.com/api/v1/following/${user}`, {
        method:'PUT',
        body:JSON.stringify({"following":list}),
        headers:{"Content-Type": 'application/json', "X-Csrftoken": csrftoken}
    })
    .then(response => response.json())
    .then(json => {
    })
}