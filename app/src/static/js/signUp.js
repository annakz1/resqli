$(function(){
    $('button').click(function(){
        $.ajax({
            url: '/signUpUser',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
                // alert(response)
                // $("html").append(response);
                // $('form').append(response);
                // document.getElementById('anna').innerHTML = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                $("#result").text(response);
                // var response_obj = JSON.parse(response);

                // alert(response);
                //
                // var fatherDiv = document.getElementById('result');
                //
                // for (var i = 0; i < response_obj.length; i++) {
                //     var obj = response_obj[i];
                //
                //     var div = document.createElement('div');
                //
                //     var div1 = document.createElement('div');
                //     div1.innerHTML = obj.field  + ": ";
                //     div.appendChild(div1);
                //
                //     var div2 = document.createElement('div');
                //     div2.innerHTML = obj.field_val;
                //     div.appendChild(div2);
                //
                //     var div3 = document.createElement('div');
                //     div3.innerHTML = "Our prediction: ";
                //     div.appendChild(div3);
                //
                //     var div4 = document.createElement('div');
                //     div4.innerHTML = obj.prediction;
                //     div.appendChild(div4);
                //
                //     fatherDiv.appendChild(div);
                // }


                // // we create the <div> element:
                // var div = document.createElement('div');
                // // give it the id that we're looking for:
                // div.id = 'ajaxResponse';
                // // append it to the document.body:
                // document.body.appendChild(div);
                // // find the element we want to work with (the <div> we
                // // created, above:
                // var responseDiv = document.getElementById('result');
                // set its innerHTML:
                // responseDiv.innerHTML = "This is a div.";
            },
            error: function(error){
                // $("#result").text(error);
                // alert(error)
                // console.log(error);
            }
        });
    });
});