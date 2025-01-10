console.log('working fine');
console.log('working fine');
console.log('working fine');

    $('#comment').submit(function(e){
        e.preventDefault();
    
        $.ajax({
            data: $(this).serialize(),
    
            method: $(this).attr('method'),
    
            url: $(this).attr('action'),
    
            dataType: 'json',
    
            success: function(response){
                console.log('comment saved to DB')
                if (response.bool == true) {
                    $('#message').html('Review Submitted successfully')
                    $("#feedback").hide()
                    $(this).hide()

                }
            }

        })
    })

$(document).ready(function(){
    $('.example2').on('click', function(){
        console.log('A boxe has being clicked')

        let filter_objects = {}

        $('.example2').each(function(){

            let filter_value = $(this).val()
            let filter_key = $(this).data('fil')

            filter_objects[filter_key] = Array.from(document.querySelectorAll(['input[data-fil=' + filter_key + ']:checked'])).map(function(element){
                return element.value
            })
        })
        console.log('filter_objects is: ', filter_objects)
        $.ajax({

            url: '/filter-products',
            data: filter_objects,
            dataType: 'json',

            beforeSend: function(){
                console.log('Trying to filter data')
            },
            success: function(res){
                console.log(res);
                console.log('data filtered successfully.....');
                $('.filtered-product').html('i love u')
            }



        })


    })
})

$(document).ready(function(){
    $('#filter-price').on('blur', function(){
        console.log('price filtered......');

            let min_price = $(this).attr('min')
            let max_price = $(this).attr('max')
            let current_price = $(this).val()
    
            console.log(min_price)
            console.log(max_price)
            console.log(current_price)

            if(current_price < parseInt(min_price) || current_price > parseInt(max_price))
                console.log('price error occured');

                alert('price must be within' + min_price + 'and $' + max_price)
        })

    });