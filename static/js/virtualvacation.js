'use strict;';

// Add Modal Window Pop Up

$(document).on('click', '[data-toggle="lightbox"]', function (event) {
	event.preventDefault();
	$(this).ekkoLightbox();
});