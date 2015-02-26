$(document).ready(function(){

	$('#likes').click(function(e){

		var product_id = $(this).attr('data-product-id');

		$.ajax({
		
			type: 'POST',
			url: '/order/product/like/',
			data: {product_id: product_id}
		
		}).done(function(data){
		
			$('#like_count').html(data);
			$('#likes').hide();
		
		}).fail(function(error){
		
			console.log(error);
		
		});
	});


	$('#customer_list_button').click(function(e){
    $.ajax({
      type: 'GET',
      url: '/order/customer/ajax/'
    }).done(function(data){
        $.each(data, function(key, value){
          console.log(value.customer_name);
          $('#customer_list').append(
            '<li><a href="/order/customer/detail/' + value.customer_slug + '/">' +
            value.customer_name + '</a></li>');
      });
    }).fail(function(xhr, error, displayError){
      console.log(error);
    });
  });
});