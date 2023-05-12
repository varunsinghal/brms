function sendToRight(identifier) {
    $("#" + identifier + "Left option:selected").appendTo("#" + identifier);
}

function sendToLeft(identifier) {
    $("#" + identifier + " option:selected").appendTo("#" + identifier + "Left");
}

function moveUp(identifier) {
    var selectedOption = $("#" + identifier + " option:selected");
    var prevOption = selectedOption.prev();
    if (prevOption.length == 1) {
        selectedOption.insertBefore(prevOption);
    }
}

function moveDown(identifier) {
    var selectedOption = $("#" + identifier + " option:selected");
    var nextOption = selectedOption.next();
    if (nextOption.length == 1) {
        selectedOption.insertAfter(nextOption);
    }
}

function serializeForm(form) {
    var serialized = {};
    $(form).find(':input').each(function () {
        if (this.type === 'checkbox' || this.type === 'radio') {
            if (this.checked) {
                serialized[this.name] = $(this).val();
            } else {
                serialized[this.name] = '';
            }
        } else if (this.type === 'select-multiple') {
            var values = [];
            $(this).find('option').each(function () {
                values.push($(this).val());
            });
            serialized[this.name] = values;
        } else {
            serialized[this.name] = $(this).val();
        }
    });
    return serialized;
}

function submitForm(e) {
    e.preventDefault();
    var serializedData = serializeForm($("form"));
    console.log(serializedData);
    $.ajax({
        type: $("form").attr("method"),
        url: $("form").attr("action"),
        data: JSON.stringify(serializedData),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data) {
            window.location.href = $("form").attr("nextLink");
        },
        error: function(data) {
            console.log(data);
        },
    });
}


function goBack(event) {
    event.preventDefault();
    window.history.back();
}
