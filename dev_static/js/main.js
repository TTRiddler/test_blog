$(document).ready(function(){
	$('.read input').click(function() {
        csrf_token = $(this).siblings('[name="csrfmiddlewaretoken"]').val();
        post_id = $(this).attr('data-id');
        
        read = $(this).val()

		data = {
            "csrfmiddlewaretoken": csrf_token,
            post_id: post_id,
            read: read,
        }

		$.ajax({
			type: "POST",
			url: $(this).parent(".read").attr('action'),
            data: data,
			success: function(data) {}
		});
    });


    $('.remove button').click(function(e) {
        e.preventDefault();
        csrf_token = $(this).siblings('[name="csrfmiddlewaretoken"]').val();
        post_id = $(this).attr('data-id');

		data = {
            "csrfmiddlewaretoken": csrf_token,
            post_id: post_id,
        }

		$.ajax({
			type: "POST",
			url: $(this).parent(".remove").attr('action'),
            data: data,
			success: function(data) {
                $('.post_block_' + post_id).addClass('d-none');
            }
		});
    });
});