function init() {
    createBed()
}

function createBed() {
    let btn1 = document.querySelectorAll('.beds-create-btn')[0]
    let btn2 = document.querySelectorAll('.beds-create-btn')[1]
    let createFormBlock = document.querySelector('.beds-create')
    let createForm = document.querySelector('#createBedForm')
    send_createForm(createForm);
    btn1.addEventListener('click', function () {
        // $('html, body').animate({
        //     scrollTop: $('footer').offset().top
        // }, 1000);
        createFormBlock.style.display = 'block';
        btn1.style.display = 'none';
        btn2.style.display = 'block';
    })
    btn2.addEventListener('click', function () {
        createFormBlock.style.display = 'none';
        btn1.style.display = 'block';
        btn2.style.display = 'none';
    })
}

function send_createForm(createForm) {
    $('.beds-create-btn-submit').click(function () {
        create_form_valid(createForm)
    })

}


function create_form_valid(form) {
    $(form).validate({
        rules: {
            name: {
                required: true,
                minlength: 4,
            },
        },
        messages: {
            name: 'This field is required. Минимальная длина 4',
        },
        submitHandler: function (form) {
            $.ajax({
                type: 'POST',
                url: "bed_create",
                data: {
                    'name': form.name.value,
                    'shape': form.shape.value,
                },
                success: function (data) {
                    $(".beds-list").html(data);
                },
                error: function (xhr) {
                    console.log("Форма создания гряды Ошибка" + xhr.status + ": " + xhr.responseText);
                },
            })
        },
    });
}


window.onload = init;