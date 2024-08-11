import Flmngr from "https://cdn.skypack.dev/flmngr";
document.addEventListener("DOMContentLoaded", () => {
    var fileInput = document.getElementById('fileInput');
    var previewImg = document.getElementById('previewImg');
    var uploadIcon = document.getElementById('uploadIcon');

    Flmngr.load({
        apiKey: "FLMNFLMN",
            urlFileManager: 'https://fm.n1ed.com/fileManager',
            urlFiles: 'https://fm.n1ed.com/files'
    }, {
        onFlmngrLoaded: () => {
            attachOnClickListenerToButton();
        }
    });

    const attachOnClickListenerToButton = () => {
        let fileInput = document.getElementById("fileInput");
        fileInput.addEventListener("click", () => {
            selectFiles();
        });
    }

    const selectFiles = () => {
        Flmngr.open({
            isMultiple: false,
            acceptExtensions: ["png", "jpeg", "jpg", "webp", "gif"],
            onFinish: (files) => {
                showSelectedImage(files);
            }
        });
    }

    const showSelectedImage = (files) => {
        let file = files[0];
        previewImg.src = file.url;
        previewImg.classList.remove('d-none');
        uploadIcon.classList.add('d-none');
        fileInput.value = file.url;
        console.log(fileInput.value)
    }
});