
function success(position) {
    let lat = position.coords.latitude;
    let long = position.coords.longitude;
    let req = new XMLHttpRequest();
    let appid = '8141967de73133be10bbf5a4ff469474'
    let url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&lat='+lat+'&lon='+long+'&appid=' + appid
    req.open('GET', url, true)
    req.send()
    req.onload = function (){
        if (req.status == 200)
        {
            let ans = JSON.parse(req.response);
            let context = {
                'city': ans['name'],
                'temp': ans['main']['temp'],
                'icon': ans['weather'][0]['icon'],
            }
            document.getElementsByClassName('weather-city')[0].textContent = context['city'];
            document.getElementsByClassName('weather-temp')[0].textContent = parseInt(context['temp']).toString();
            document.getElementsByClassName('weather-icon')[0].src = 'http://openweathermap.org/img/wn/'+context['icon']+'.png';
            // $.ajax({
            //     url:"",
            //     method:'POST',
            //     data: {
            //         'data': req.response,
            //     },
            //     success:function(data){
            //
            //     }
            // })
        }
        else
        {
            document.getElementsByClassName('weather-info')[0].textContent = 'Ошибка при запросе местоположения';
        }
    }
}

function error() {
    console.log('fail Geolocation');
    content_block = document.getElementById('content-block');
    request_block = document.getElementById('request-block');
    request_block.style.display = "block";
    content_block.style.display = "none";
}

function init() {
    navigator.geolocation.getCurrentPosition(success, error);
}

window.onload = init;