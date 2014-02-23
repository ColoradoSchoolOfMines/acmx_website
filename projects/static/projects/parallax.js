function sizeSliders()
{
	var windowHeight = $(window).innerHeight();
	var windowWidth = $(window).innerWidth();
	var headerHeight = $('#header').outerHeight();
	var viewportHeight = windowHeight - headerHeight;
	var sliderVerticalPadding = $('.slider').outerHeight() - $('.slider').height();
	var sliderHorizontalPadding = $('.slider').outerWidth() - $('.slider').width();
	$('.slider').height(viewportHeight - sliderVerticalPadding);
	$('.slider').width(windowWidth - sliderHorizontalPadding);	
	var sliderHeight = $('.slider').outerHeight();
	$('.slider.hidden').css('top', -(sliderHeight));
}

function positionSliders()
{
	var topPosition = $('#header').outerHeight();
	
	$('.slider').css('top', topPosition);
}
function slideUp(slider)
{
	var headerHeight = $('#header').outerHeight();
	var sliderHeight = $('.slider').outerHeight();
	$(slider).stop().animate({'top':'-=' + sliderHeight},
		{
			duration: window.DURATION,
			step: function(){
				var slided = Math.round($(slider).css('top').replace('px','') - headerHeight);
				$(slider).css('background-position', '50% ' + (- (window.RATE * slided)) + 'px');
			},
			always: function(){
				$(slider).addClass('hidden').css('top', -(sliderHeight));
			}
		});
}
function slideDown(slider)
{
	var headerHeight = $('#header').outerHeight();
	var sliderHeight = $('.slider').outerHeight();
	$(slider).stop().animate({'top':'+=' + (sliderHeight + headerHeight)},
		{
			duration: window.DURATION,
			step: function(){
				var slided = Math.round($(slider).css('top').replace('px','') - headerHeight);
				$(slider).css('background-position', '50% ' +  (-(window.RATE * slided)) + 'px');
			},
			always: function(){
				$(slider).removeClass('hidden').css('top', headerHeight);
			}
		});
}
function getTopVisibleSlider()
{
	var sliders = $('.slider').not('.hidden');
	var largestZ = 0;
	var largestZObject;
	$.each(sliders, function(key, value){
		var currentZ = $(value).css('z-index');
		if(currentZ > largestZ){
			largestZ = currentZ;
			largestZObject = value;	
		}
	});
	return largestZObject;
}
function getBottomHiddenSlider()
{
	var sliders = $('.hidden');
	var smallestZ = 999;
	var smallestHiddenZObject;
	$.each(sliders, function(key, value){
		var currentZ = $(value).css('z-index');
		if(currentZ < smallestZ){
			smallestZ = currentZ;
			smallestHiddenZObject = value;	
		}
	});
	return smallestHiddenZObject;
}
function detectMouseMomentum(wheelDelta)
{
	window.clearTimeout(window.mouseTimeout);
	window.wheelMomentum += wheelDelta;
	window.mouseTimeout = setTimeout(function(){
		console.log('mouse momentum cleared');
		window.wheelMomentum = 0;
	}, 500);
	if(window.wheelMomentum > window.scrollThresh && window.repeatFlag == 0){
		slideDown(getBottomHiddenSlider());
		window.wheelMomentum = 0;
		window.repeatFlag = 1;
		window.repeatTimeout = setTimeout(function(){
			window.repeatFlag = 0;
		}, window.REPEATTHRESH);
	}else if(window.wheelMomentum < -(window.scrollThresh) && window.repeatFlag == 0){
		slideUp(getTopVisibleSlider());
		window.wheelMomentum = 0;
		window.repeatFlag = 1;
		window.repeatTimeout = setTimeout(function(){
			window.repeatFlag = 0;
		}, window.REPEATTHRESH);
	}



	console.log(window.wheelMomentum);
}
function bindSliders()
{
	var sliders = $('.slider');
	$.each(sliders, function(key, value){
		var zIndex = sliders.length - key;
		$(value).css('z-index', zIndex);
	});
	$('.slider').unbind().click(function(){slideUp(this)});

	window.wheelMomentum = 0;
	$(window).bind('mousewheel', function(event){
		detectMouseMomentum(event.originalEvent.wheelDelta);
	});
	$(window).keydown(function(event){
		if(event.which == 40){
			slideUp(getTopVisibleSlider());
			event.preventDefault();
		}else if(event.which == 38){
			slideDown(getBottomHiddenSlider());
			event.preventDefault();
		}
	});
}

// On page load:
window.RATE = 0.7;
window.scrollThresh = 1500;
window.repeatFlag = 0;
window.DURATION = 1200;
window.REPEATTHRESH = 1.2 * window.DURATION;
$('body').css('overflow', 'hidden');
sizeSliders();	// Set the size of the sliders based on window parameters
$(window).resize(sizeSliders);	// Set the sliders again whenever window size changes

positionSliders();	// Stack all sliders on top of each other.

bindSliders();	// Slide the sliders up and off the page on click.