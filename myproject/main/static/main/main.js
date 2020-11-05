function init() {
    send_form()
}

function send_form() {
    $('.developer-letter-btn-submit').click(function () {
        let form = $('.developer-letter')[0];
        let block_success = $('.developer-form-success')[0];
        let block_success_btn = block_success.querySelector('button');
        $(form).validate({
            submitHandler: function (form) {
                $.ajax({
                    method: 'post',
                    url: 'http://127.0.0.1:8000/send_developer_message',
                    data: {
                        'topic': form.topic.value,
                        'body': form.body.value,
                    },
                    success: function (data) {
                        data = new DOMParser().parseFromString(data, 'text/html');
                        let new_form = data.querySelector('.developer-letter');
                        $(form).html($(new_form).html());
                        block_success.style.display = 'block';
                        form.style.display = 'none';
                        $(block_success_btn).click(function () {
                            form.style.display = 'block';
                            block_success.style.display = 'none';
                            send_form()
                        })
                    }
                })
            },
            rules: {
                'topic': {
                    required: true,
                    minlength: 1,
                    maxlength: 30,
                },
                'body': {
                    required: true,
                    minlength: 1,
                }
            },
            messages: {
                topic: 'Поле обязательное. От 1 до 30 символов.',
                body: 'Поле обязательное.'
            },
        })
    })
}

window.onload = init()