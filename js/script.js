$(document).ready(function(){
	resize_squares();
});

function resize_squares(){
	// This function will force the 'square' class to be as tall as it is wide on page load.
	// When the window is resized, the height of the element will change along with the change in its width.
	$('.square').height($('.square').width());	// Call this once on page load to size elements correctly
	$(window).resize(function(){	// Set a listener to page resize, and resize elements whenever this event occurs.
		$('.square').height($('.square').width())
	});
}

function fill_square_backgrounds(){
	// This function will fetch each square's background image once the page has loaded.
	// Once each image has loaded successfully, the image should fade in as the background image
	// for its respective square.

	// to be written
}