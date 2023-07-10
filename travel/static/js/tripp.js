'use strict';

/* CLICK ICON ADD */
document.querySelector(".add").addEventListener("click", () => {
    document.querySelector(".add_image").style.display = "flex"
})
/* CLICK ICON CLOSE */
document.querySelector(".close").addEventListener("click", () => {
    document.querySelector(".add_image").style.display = "none"
})
/* WINDOW ADD IMAGE */
;( function ( document, window, index )
{
	var inputs = document.querySelectorAll( '.inputfile' );
	Array.prototype.forEach.call( inputs, function( input )
	{
		var label	 = input.nextElementSibling,
			labelVal = label.innerHTML;

		input.addEventListener( 'change', function( e )
		{
			var fileName = '';
			if( this.files && this.files.length > 1 )
				fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
			else
				fileName = e.target.value.split( '\\' ).pop();

			if( fileName )
				label.querySelector( 'span' ).innerHTML = fileName;
			else
				label.innerHTML = labelVal;
		});
	});
}( document, window, 0 ));