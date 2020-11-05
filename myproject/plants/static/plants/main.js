function init() {
    btns_active();
    plants_create();
    plant_functions_form_visible()
}


function plant_functions_form_visible() {
    let show_btn = document.querySelector('.plant-functions-form-show-btn');
    let hide_btn = document.querySelector('.plant-functions-form-hide-btn');
    let form = document.querySelector('.plant-functions-form');
    $(show_btn).click(function () {
        form.style.display = 'block';
        this.style.display = 'none';
        hide_btn.style.display = 'block';
    })
    $(hide_btn).click(function () {
        form.style.display = 'none';
        this.style.display = 'none';
        show_btn.style.display = 'block';
    })
    plant_functions_form()
}

function plant_functions_form() {
    $('.plant-functions-form-submit').click(function () {
        let form = $('.plant-functions-form')[0];
        plant_functions_form_validate(form);
    })
}

function plant_functions_form_validate(form) {
    $(form).validate({
        submitHandler: function (form) {
            let id = $('.plant-functions')[0].id;
            let date = new Date();
            $.ajax({
                method: 'post',
                url: 'function_create',
                data: {
                    'plant_id': id,
                    'name': form.name.value,
                    'first_date': form.date.value,
                    'period': form.period.value,
                    'day': date.getDate(),
                    'month': date.getMonth()+1,
                    'year': date.getFullYear(),
                },
                success: function (data) {
                    data = new DOMParser().parseFromString(data, 'text/html');
                    let new_plant_functions = data.querySelector('.plant-functions');
                    $('.plant-functions').html($(new_plant_functions).html());
                    plant_functions_form_visible();
                },
            })
        },
        rules: {
            'name': {
                minlength: 2,
                maxlength: 50,
                required: true,
            },
            'date': {
                required: true,
            },
            'period': {
                required: true,
                digits: true,
                minlength: 1,
                maxlength: 5,
            },
        },
        messages: {
            'name': 'Поле обязательное. От 2 до 50 символов',
            'date': 'Поле обязательное.',
            'period': 'Поле обязательное. От 1 до 5 цифр',
        }
    })
}

function function_del(id) {
    let plant_id = $('.plant-functions')[0].id;
    $.ajax({
        method: 'post',
        url: 'function_del',
        data: {
            'id': id,
            'plant_id': plant_id,
        },
        success: function (data) {
            data = new DOMParser().parseFromString(data, 'text/html');
            let new_plant_functions = data.querySelector('.plant-functions');
            $('.plant-functions').html($(new_plant_functions).html());
            plant_functions_form_visible();
        },
    })
}


///// Информация и редактирование растений

function plant_get(plant_id) {
    // let date = new Date()
    // console.log(date.getMonth());
    // let d = new Date(date.getFullYear(), date.getMonth(), date.getDate());
    // console.log(d);
    let block = $('.bed-content-info')[0];
    let plants_list = block.querySelector('.plants-list');
    let btns = plants_list.querySelectorAll('button');
    for (let btn of btns){
        if(btn.id == plant_id){
            btn.style.backgroundColor = 'red';
        }
        else
            btn.style.backgroundColor = '#53ff30';
    }
    if (plant_id) {
        $.ajax({
            method: 'POST',
            url: 'plant_get',
            data: {
                'id': plant_id,
            },
            success: function (data) {
                data = new DOMParser().parseFromString(data, 'text/html');
                let one_plant_info_title = data.querySelector('.one-plant-info-title');
                let plant_functions = data.querySelector('.plant-functions');
                $('.one-plant-info-title').html($(one_plant_info_title).html());
                $('.plant-functions').html($(plant_functions).html());
                $('.one-plant-info')[0].style.opacity = '1';
                $('.one-plant-info')[0].style.pointerEvents = 'auto';
                $('.plant-functions')[0].id = plant_id

                let new_plant_profile = data.querySelector('.div-plant-profile');
                let old_plant_profile = $('.div-plant-profile')[0];
                $(old_plant_profile).html($(new_plant_profile).html())
                let plant_profile = $('.plant-profile')[0];
                plant_profile.id = plant_id;
                plant_functions_form_visible()
            },
        })
    }
}

function plant_save() {
    let plant_profile = $('.plant-profile')[0];
    $(plant_profile).validate({
        submitHandler: function (form) {
            $.ajax({
                method: 'post',
                url: 'plant_save',
                data: {
                    'id': form.id,
                    'name': form.name.value,
                    'desc': form.desc.value,
                },
                success: function (data) {
                    data = new DOMParser().parseFromString(data, 'text/html');
                    let new_plant_profile = data.querySelector('.plant-profile');
                    let old_plant_profile = $('.plant-profile');
                    $(old_plant_profile).html($(new_plant_profile).html());
                    $('.success-message').slideDown(200, function () {
                        setTimeout(function () {
                            $('.success-message').slideUp(200);
                        }, 500);
                    });

                    let one_plant_info_title = data.querySelector('.one-plant-info-title');
                    $('.one-plant-info-title').html($(one_plant_info_title).html());

                }
            })
        },
        rules: {
            'name': {
                minlength: 2,
                maxlength: 15,
                required: true,
            },
            'desc': {
                minlength: 0,
                required: false,
            }
        },
        messages: {
            'name': 'Поле обязательное. От 2 до 15 символов'
        }
    })
}

function plant_del() {
    let plant_profile = $('.plant-profile')[0];
    $.ajax({
        method: 'post',
        url: 'plant_del',
        data: {
            'id': plant_profile.id,
        },
        success: function (data) {
            let datadom = new DOMParser().parseFromString(data, 'text/html');
            let new_data_create = datadom.querySelector('.plants-create .plants-list')
            $('.plants-create .plants-list').html($(new_data_create).html())
            let new_data_info = datadom.querySelector('.plants-info .plants-list')
            $('.plants-info .plants-list').html($(new_data_info).html())

            let new_one_plant_info = datadom.querySelector('.one-plant-info');
            let one_plant_info = $('.one-plant-info')[0];
            $(one_plant_info).html($(new_one_plant_info).html());
            //console.log(plant_profile);
            one_plant_info.style.opacity = '0.5';
            one_plant_info.style.pointerEvents = 'none';
        },
    })
}


///// Создание растений
function plants_create() {
    let block = document.querySelector('.bed-custom');
    let cursorBlock = document.querySelector('.cursorBlock');
    let cursorBlockActive = document.querySelector('.cursorBlockActive');
    cursor_events(block, cursorBlock);

    $(block).click(function (event) {
        let target = this.getBoundingClientRect();
        let coords = {
            'x': event.clientX - target.left,
            'y': event.clientY - target.top,
        }
        cursorBlockActive.style.left = coords['x'] + 'px';
        cursorBlockActive.style.top = coords['y'] + 'px';
        cursorBlockActive.style.display = 'block';
        let createform = document.querySelector('.plant-create-form');
        createform.style.opacity = '1';
        createform.style.pointerEvents = 'auto';
        createform.style.borderColor = '#4dff6f';
        //console.log(createform);
        $('.plant-create-btn-submit').click(function () {
            form_validation(createform, cursorBlockActive)
        })
    })
}

function form_validation(form, cursorActive) {

    $(form).validate({
        submitHandler: function (form) {
            let date = new Date()
            $.ajax({
                method: 'post',
                url: 'plant_create',
                data: {
                    'name': form.name.value,
                    'desc': form.desc.value,
                    'x': getComputedStyle(cursorActive).left,
                    'y': getComputedStyle(cursorActive).top,
                    'day': date.getDate(),
                    'month': date.getMonth()+1,
                    'year': date.getFullYear(),
                },
                success: function (data) {
                    let datadom = new DOMParser().parseFromString(data, 'text/html')
                    // let plants_content = data.querySelector('.plants-content');
                    // $('.plants-content').html($(plants_content).html());

                    let new_data_create = datadom.querySelector('.plants-create .plants-list')
                    $('.plants-create .plants-list').html($(new_data_create).html())
                    let new_data_info = datadom.querySelector('.plants-info .plants-list')
                    $('.plants-info .plants-list').html($(new_data_info).html())

                    $(form).html($(datadom.querySelector('.plant-create-form')).html());
                    form.style.opacity = '0.5';
                    form.style.pointerEvents = 'none';
                    form.style.borderColor = 'black';
                    cursorActive.style.display = 'none';
                },
            })
        },
        rules: {
            'name': {
                minlength: 2,
                maxlength: 15,
                required: true,
            },
            'desc': {
                required: false,
            }
        },
        messages: {
            'name': 'Поле обязательное. От 2 до 15 символов'
        }
    })
}

function cursor_events(block, cursorBlock) {
    let blockWidth = getComputedStyle(block).width.slice(0, -2);
    let blockHeight = getComputedStyle(block).height.slice(0, -2);
    block.addEventListener('mousemove', function (event) {
        let target = this.getBoundingClientRect();
        let mouseX = event.pageX;
        let mouseY = event.clientY;
        let x = mouseX - target.left;
        let y = mouseY - target.top;
        let active = target.left <= mouseX && mouseX <= target.right && target.top <= mouseY && mouseY <= target.bottom;
        if (!active) {
            cursorBlock.style.display = 'none';
        } else {
            cursorBlock.style.display = 'block';
            cursorBlock.style.top = (y).toString() + 'px';
            cursorBlock.style.left = (x).toString() + 'px';
        }

    })
    block.addEventListener('mouseleave', function (event) {
        cursorBlock.style.display = 'none';
    })
}

function btns_active() {
    let btn1 = $('.plant-create-btn')[0]
    let btn2 = $('.plant-info-btn')[0]
    $(btn1).click(function () {
        btn1.classList.add('plant-btn-active');
        btn2.classList.remove('plant-btn-active');

        $('.plants-create')[0].style.display = 'block';
        $('.plants-info')[0].style.display = 'none';
    })
    $(btn2).click(function () {
        btn1.classList.remove('plant-btn-active');
        btn2.classList.add('plant-btn-active');
        $('.plants-create')[0].style.display = 'none';
        $('.plants-info')[0].style.display = 'block';
    })
}

window.onload = init;