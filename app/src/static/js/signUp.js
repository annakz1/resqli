$(function(){
    $('button').click(function(){
        $.ajax({
            url: '/signUpUser',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
                document.getElementById('result').innerHTML = response
            },
            error: function(error){
                $("#result").text(error);
            }
        });
    });
});