$(document).ready(function () {


    // получение пути
    const pathname = window.location.pathname.slice(6);

    function clearForms() {
        // для input
        $('#forms').trigger('reset');

        // чистит все атритубы selected == selected
        selectClear = $('#forms').find('select');
        for (let i = 0; i < selectClear.length; i++) {
            for (const option of selectClear[i].children) {
                if (option.getAttribute('selected') === 'selected') {
                    option.removeAttribute('selected');
                }
            }
        }
    }

    function method_ajax(form, methodAjax, td_id) {

        if (!form.valid()) {
            return false;
        } else {

            const json_map = new Map()
            a = $(form).find('input, select, textarea')

            for (let i = 0; i < a.length; i++) {
                json_map.set(a[i].name, a[i].value)
            }

            if ("PUT" === methodAjax) {
                var tr_id = $(form)
                for (var i=0; i<5; i++){
                    tr_id = tr_id.parent();
                }
                json_map.set('id', tr_id.attr('id'))
            }

            if ("DELETE" === methodAjax) {
                var tr_id = $(form)
                for (var i=0; i<3; i++){
                    tr_id = tr_id.parent();
                }
                json_map.set('id', tr_id.attr('id'))
            }


            $.ajax({
                url: pathname,
                type: methodAjax,
                dataType : 'json',

                data: JSON.stringify(Object.fromEntries(json_map)),

                contentType: 'application/json;charset=UTF-8',
                success: function (response) {
                    clearForms();
                    location.reload();
                },
                error: function (response) {
                    console.log("Ошибка добавления");
                    console.log(response);
                }
            });
            return false
        }
    };

    $('#form_create').on('click', '.add_item', function () {
        method_ajax($(this).parent(), "POST");
        return false
    });

    $('.form_ed').on('click', '.edit_item', function () {
        method_ajax($(this).parent(), "PUT");
        return false
    });

    $('.form_del').on('click', '.del_item', function () {
        method_ajax($(this).parent(), "DELETE");
        return false
    });
});