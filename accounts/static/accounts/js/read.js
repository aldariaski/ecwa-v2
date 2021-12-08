$(document).on('click', "#delete", function () {
    if (confirm('Are you sure want to delete account?')) {
        $.ajax({
            type: 'POST',
            url: "/accounts/delete/",
            success: function (data) {
                window.location = `/accounts/login/`
            },
            Error: function(data){
                console.log("error");
            },
            fail: function(data){
                console.log("fail");
            }
        });
    }
})