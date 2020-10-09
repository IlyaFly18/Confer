function success(position)
{
    let lat = position.coords.latitude;
    let long = position.coords.longitude;
    request_block = document.getElementById('request-geolocation');
    request_block.style.display = "none";
}

function error(){


}

function init(){
    navigator.geolocation.getCurrentPosition(success, error);
}

window.onload = init;