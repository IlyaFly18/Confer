function success(position)
{
    let lat = position.coords.latitude;
    let long = position.coords.longitude;
    content_block = document.getElementById('content-block');
    request_block = document.getElementById('request-block');
    request_block.style.display = "none";
    content_block.style.display = "block";
    console.log(content_block);
}

function error(){


}

function init(){
    navigator.geolocation.getCurrentPosition(success, error);
}

window.onload = init;