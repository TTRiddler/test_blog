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
});