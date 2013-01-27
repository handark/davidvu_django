$(window).load(function() {
	$('#slider').orbit();
	//menu opacity
	$('#nav a, #logo').hover(function() {
		$(this).animate({opacity: 1});
	}, function(){
		$(this).animate({opacity: 0.7});
	});
	//menu blur
	$('#nav a').hover(function() {
		$('#nav a').not(this).css({
			color: 'transparent',
			//textShadow: '0 0 2px #ff7301'
		}).toggleClass("active");
	}, function() {
		$('#nav a').not(this).css({
			color: '#ff7301',
			//textShadow: 'none'
		}).toggleClass("active");
	})
	//portfolio images
	console.log($('.portfolio-preview').width());
	if ($('.portfolio-preview').width() == '208'){
		$('.portfolio-preview').hover(function() {
			$(this).animate({height: '172px'});
		}, function() {
			$(this).animate({height: '152px'});
		})
	}
	//portfolio gallery
	$(".thumbs img").click(function() {
		// see if same thumb is being clicked
		if ($(this).hasClass("thumb-active")) { return; }
	 
		// calclulate large image's URL based on the thumbnail URL (flickr specific)
		var url = $(this).attr("rel");
	 
		// get handle to element that wraps the image and make it semi-transparent
		var wrap = $(".image-wrapper").fadeTo("medium", 0.5);
	 
		// the large image from www.flickr.com
		var img = new Image();
	 

		// call this function after it's loaded
		img.onload = function() {
	 
			// make wrapper fully visible
			wrap.fadeTo("fast", 1);
	 
			// change the image
			wrap.find("img").attr("src", url);
	 
		};
	 
		// begin loading the image from www.flickr.com
		img.src = url;
	 
		// activate item
		$(".thumbs img").removeClass("thumb-active");
		$(this).addClass("thumb-active");
	 
	// when page loads simulate a "click" on the first image
	}).filter(":first").click();
});