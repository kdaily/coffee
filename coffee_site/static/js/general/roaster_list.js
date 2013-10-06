jQuery(function($){
    $('.addremoveuserroaster').click(function(){
	if ($(this).hasClass('icon-plus')){
	    $.ajax({type: "POST",
                    url: "{% url 'add_user_roaster' %}",
               	    data: {'roaster_pk': $(this).attr('name'), 'csrfmiddlewaretoken': '{{csrf_token}}'},
               	    dataType: "text",
               	    success: function(response) {},
                    error: function(rs, e) {
                        //  alert(rs.responseText);
                    }
        	   });
	    $(this).val('Added!');
	    $(this).removeClass("icon-plus");
	    $(this).addClass("icon-minus");
	} 
        else if ($(this).hasClass('icon-minus')) {
            $.ajax({type: "POST",
                    url: "{% url 'remove_user_roaster' %}",
                    data: {'roaster_pk': $(this).attr('name'), 'csrfmiddlewaretoken': '{{csrf_token}}'},
                    dataType: "text",
                    success: function(response) {},
                    error: function(rs, e) {
                        alert(rs.responseText);
                    }
            });
	    $(this).val('Removed!');
	    $(this).removeClass("icon-minus");
	    $(this).addClass("icon-plus");
	}
			
    });

    $('.auto-submit-star').click(function(){
        <!-- alert("The value selected was '" + $(this).attr('value') + "' for name '" + $(this).attr('name') + "'"); -->

        $.ajax({type: "POST",
                url: "{% url 'rate_user_roaster' %}",
                data: {'roaster_pk': $(this).attr('name'), 
                       'rating': $(this).attr('value'),
                       'csrfmiddlewaretoken': '{{csrf_token}}'},
                dataType: "text",
                success: function(response) {},
                <!-- error: function(rs, e) { -->
                <!--     alert(rs.responseText); -->
                <!--     } -->
                });

	$(this).attr('checked', 'checked');

        // To submit the form automatically:
        //this.form.submit();

        // To submit the form via ajax:
        //$(this.form).ajaxSubmit();
    });

});
