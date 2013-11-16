jQuery(function($){

    $( ".datePicker" ).datepicker({ dateFormat: 'yy-mm-dd' });
    
    var rateuserstore_url = "/rateuserstore/"
    var adduserstore_url = "/adduserstore/"
    var removeuserstore_url = "/removeuserstore/"

    // use jQuery to get specific cookie
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

    $('.addremoveuserstore').click(function(){

	//alert(csrftoken);	    

	if ($(this).hasClass('icon-plus')){
	    $.ajax({type: "POST",
                    url: adduserstore_url,
               	    // data: {'store_pk': $(this).attr('name'), 'csrfmiddlewaretoken': '{{csrf_token}}'},
               	    data: {'store_pk': $(this).attr('name'), 'csrfmiddlewaretoken': csrftoken},
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
                    url: removeuserstore_url,
                    data: {'store_pk': $(this).attr('name'), 'csrfmiddlewaretoken': csrftoken},
		// data: {'store_pk': $(this).attr('name'), 'csrfmiddlewaretoken': '{{csrf_token}}'},
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
        $.ajax({type: "POST",
                url: rateuserstore_url,
                data: {'store_pk': $(this).attr('name'), 
                       'rating': $(this).attr('value'),
                       'csrfmiddlewaretoken': csrftoken},
                dataType: "text",
                success: function(response) {},
                error: function(rs, e) {}
               });
	
	$(this).attr('checked', 'checked');
	
        // To submit the form automatically:
        //this.form.submit();
	
        // To submit the form via ajax:
        //$(this.form).ajaxSubmit();
    });
    
});
