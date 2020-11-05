function init() {
    send_date()
    notif_done()
}

function send_date() {
    let date = new Date()
    $.ajax({
        method: 'post',
        url: '',
        data: {
            'day': date.getDate(),
            'month': date.getMonth() + 1,
            'year': date.getFullYear(),
        },
        success: function (data) {
            data = new DOMParser().parseFromString(data, 'text/html');
            let notif_content = data.querySelector('.notifications-content');
            $('.notifications-content').html($(notif_content).html());
            notif_done()
        },
    })
}

function notif_done() {
    $('.notif-item-done').click(function () {
        this.innerHTML = '\t&#10004;';
        let date = new Date()
        $.ajax({
            method: 'post',
            url: 'notif_done',
            data: {
                'id': this.id,
                'day': date.getDate(),
                'month': date.getMonth() + 1,
                'year': date.getFullYear(),
            },
            success: function (data) {
                data = new DOMParser().parseFromString(data, 'text/html');
                let notif_content = data.querySelector('.notifications-content');
                $('.notifications-content').html($(notif_content).html());
                notif_done()
            },
        })
    })
}


window.onload = init;