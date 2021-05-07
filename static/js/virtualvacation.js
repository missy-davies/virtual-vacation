'use strict;';

// Add Modal Window Pop Up

$(document).on('click', '[data-toggle="lightbox"]', function (event) {
	event.preventDefault();
	$(this).ekkoLightbox();
});


// Set Flask Flashed messages to fade out after 10 seconds
setTimeout(function () {
	$('.flash-msg').fadeOut('slow');
}, 10000);