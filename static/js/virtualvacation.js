'use strict;';

$('#upload').on('click', (evt) => {
	evt.preventDefault();

	let radios = $("input[type='radio']");
	let data = radios.filter(':checked').val();
	let filename = $("input[type='file']").val();
  let cleaned = filename.replace(/^.*?([^\\\/]*)$/, '$1'); 

	// Save to Database
	$.post('/upload', { name: data, file: cleaned });
});