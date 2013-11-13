jQuery(function($){
    
    $( ".datePicker" ).datepicker({dateFormat: "yy-mm-dd"});
    
    function json_to_select(url, select_selector) {
	/*
	  Fill a select input field with data from a getJSON call
	  Inspired by: http://stackoverflow.com/questions/1388302/create-option-on-the-fly-with-jquery
	*/
	$.getJSON(url, function(data) {
	    var opt=$(select_selector);
	    var old_val=opt.val();
	    opt.html('');
	    $.each(data, function () {
		opt.append($('<option/>').val(this.id).text(this.value));
	    });
	    opt.val(old_val);
	    opt.change();
	})
    }
    
    $('#id_roaster').change(function(){
	json_to_select('/coffeebag_by_roaster_json?roaster=' + $(this).val(), '#id_coffeebag');
    });
    
});
