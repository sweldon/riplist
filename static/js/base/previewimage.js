var all_files = [];
var count=0;
function removePhoto(image, currentFiles){
	image.parent().remove();
	count--;
}

function handleFileSelect(evt) {

	var $fileUpload = $("input#files[type='file']");

	count=count+parseInt($fileUpload.get(0).files.length);

	if (parseInt($fileUpload.get(0).files.length) > 6 || count>5) {
		alert("Please limit your album to 5 photos.");
		count=count-parseInt($fileUpload.get(0).files.length);
		evt.preventDefault();
		evt.stopPropagation();
		return false;
	}
	var files = evt.target.files;
	for (var i = 0, f; f = files[i]; i++) {
		if (!f.type.match('image.*')) {
			continue;
		}
		var reader = new FileReader();

		reader.onload = (function (theFile) {
			return function (e) {

				var span = document.createElement('span');
				span.innerHTML = ['<img class="thumb" src="', e.target.result, '" title="', escape(theFile.name), '"/><span class="remove_img_preview" onclick="removePhoto($(this), files)"></span>'].join('');
				document.getElementById('list').insertBefore(span, null);
			};
		})(f);

		reader.readAsDataURL(f);
	}
	all_files.push(files)
	console.log("ADDED: "+all_files);
}
	
$('#files').change(function(evt){
    handleFileSelect(evt);
});
