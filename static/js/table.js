// var searchContent = document.getElementById("search");
// searchContent.addEventListener("input",test);

// function test(){
// 	alert("hi");
// }


// var $rows = $('#table tr');
// var $input = $('#search');
// $input.keyup(filter);

// function filter() {
//     var val = $.trim($input.val()).replace(/ +/g, ' ').toLowerCase();
//     $rows.show().filter().hide(hideFnc);
// }

// function hideFnc() {
//         var text = $input.text().replace(/\s+/g, ' ').toLowerCase();
//         return !~text.indexOf(val);
// }

var $rows = $('#table tr');
$('#search').keyup(function() {
    var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
    
    $rows.show().filter(function() {
        var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
        if (text.indexOf('first') === 1){
        	return 0;
        }
        return !~text.indexOf(val);
    }).hide();
    $('tr : first').show();
});