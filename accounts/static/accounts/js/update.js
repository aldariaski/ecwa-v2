$(document).on('click', "#submit", function () {
    var json = {}
    var username = $('#username').val();
    var name = $('#name').val();
    if (name.length == 0) {
        alert('Name is required');
        return;
    }
    var gender = $('#gender').find(":selected").text();
    var phone_number = $('#phone_number').val();
    if (phone_number.length == 0) {
        alert('Phone number is required!')
        return;
    }
    var address = $('#address').val();
    if (address.length == 0) {
        alert('Address is required!')
        return;
    }
    var occupation = $('#occupation').val();
    if (occupation.length == 0) {
        alert('Occupation is required!')
        return;
    }
    var description = $('#description').val();
    if (description.length == 0) {
        alert('Description is required!')
        return;
    }

    json['username'] = username
    json['name'] = name
    json['gender'] = gender
    json['address'] = address
    json['occupation'] = occupation
    json['phone_number'] = phone_number
    json['description'] = description
    json = JSON.stringify(json);

    console.log(json);
    $.ajax({
        type: 'POST',
        url: "/accounts/update/",
        data: json,
        success: function (data) {
            window.location = `/accounts/profile/` + username
        },
        Error: function(data){
            console.log("error");
        },
        fail: function(data){
            console.log("fail");
        }
    });
})
