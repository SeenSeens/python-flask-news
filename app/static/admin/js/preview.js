document.addEventListener("DOMContentLoaded", () => {
    var fileInput = document.getElementById('fileInput');
    var previewImg = document.getElementById('previewImg');
    var uploadIcon = document.getElementById('uploadIcon');

    fileInput.addEventListener('change', (event) => {
        var file = event.target.files[0];
        if (file) {
            var reader = new FileReader();
            reader.onload = function(e) {
                previewImg.src = e.target.result;
                previewImg.classList.remove('d-none');
                uploadIcon.classList.add('d-none');
            };
            reader.readAsDataURL(file);
        }
    });
});
