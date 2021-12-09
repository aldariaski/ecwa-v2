$(document).on('click', "#submit", function () {
    var json = {}
    var username = $('#username').val();
    if (username.length == 0) {
        alert('Username is required');
        return;
    }
    var name = $('#name').val();
    if (name.length == 0) {
        alert('Name is required');
        return;
    }

    var date = new Date($('#birth_date').val());
    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();
    var gender = $('#gender').find(":selected").text();
    var phone_number = $('#phone_number').val();
    if (phone_number.length == 0) {
        alert('Phone number is required!')
        return;
    }
    var password = $('#password').val();
    if (password.length == 0) {
        alert('Password is required!')
        return;
    }
    json['username'] = username
    json['name'] = name
    json['day'] = day
    json['month'] = month
    json['year'] = year
    json['gender'] = gender
    json['phone_number'] = phone_number
    json['password'] = password
    json = JSON.stringify(json);

    console.log(json);
    $.ajax({
        type: 'POST',
        url: "/register/",
        data: json,
        success: function (data) {
            window.location = `/`
        },
        Error: function(data){
            console.log("error");
        },
        fail: function(data){
            console.log("fail");
        },
        statusCode: {
            500: function(){
                alert("Make sure all forms are filled!");
            },
            409 : function(){
                alert("Username is already used!")
            }

        }
    });

})

