jQuery(function($){
    // using jQuery
    function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
	    var cookies = document.cookie.split(';');
	    for (var i = 0; i < cookies.length; i++) {
		var cookie = jQuery.trim(cookies[i]);
		// Does this cookie string begin with the name we want?
		if (cookie.substring(0, name.length + 1) == (name + '='))
		{
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
		}
	    }
	    
	    return cookieValue;
	}
    }
    
    var csrftoken = getCookie('csrftoken');

    $('.addremoveuserroaster').click(function(){

	//alert(csrftoken);	    

	if ($(this).hasClass('icon-plus')){
	    $.ajax({type: "POST",
                    url: "/adduserroaster/",
               	    // data: {'roaster_pk': $(this).attr('name'), 'csrfmiddlewaretoken': '{{csrf_token}}'},
               	    data: {'roaster_pk': $(this).attr('name'), 'csrfmiddlewaretoken': csrftoken},
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
                    url: "/removeuserroaster/",
                    data: {'roaster_pk': $(this).attr('name'), 'csrfmiddlewaretoken': csrftoken},
		// data: {'roaster_pk': $(this).attr('name'), 'csrfmiddlewaretoken': '{{csrf_token}}'},
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
                url: "/rateuserroaster/",
                data: {'roaster_pk': $(this).attr('name'), 
                       'rating': $(this).attr('value'),
                       'csrfmiddlewaretoken': csrftoken},
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
