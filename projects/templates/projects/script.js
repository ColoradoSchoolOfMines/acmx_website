// make squares... square
$('.square').each(function(){
	var color = 'rgb(85,85,' + (85 + Math.ceil(150*Math.random())) + ')';
	$(this).css({'background-color':color});
});
$('.square').height($('.square').width());
$(window).resize(function(){
	$('.square').height($('.square').width());
});

// search bar causes gross jumpiness in Chrome
// // awesome search bar (css animate won't cut it)
// $('input#search').focus(function(){
// 	$(this).animate({'width':'200px'});
// }).blur(function(){
// 	if($(this).val() == '' || $(this).val() == undefined){
// 		$(this).animate({'width':'74px'});
// 	}
// });

// animate gigabot
var gigabot = $('#gigabot');
var speed = 10;
var width = $(gigabot).width();
$(window).keydown(function(e){
	if(e.which == 37 && $(gigabot).css('margin-left') > '0px'){
		// left
		$(gigabot).css({'margin-left':'-=' + speed});
		console.log('left');
	}else if(e.which == 39 && document.getElementById('gigabot').getBoundingClientRect().left + width + 10 < window.innerWidth){
		// right
		$(gigabot).css({'margin-left':'+=' + speed});
	}
});