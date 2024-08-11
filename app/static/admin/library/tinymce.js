'use strict'
const example_image_upload_handler = (blobInfo, progress) => new Promise((resolve, reject) => {
    $.ajax({
        url: `{{ url_for('admin.upload_image') }}`,
        type: 'POST',
        data: (() => {
            const formData = new FormData();
            formData.append('file', blobInfo.blob(), blobInfo.filename());
            return formData;
        })(),
        contentType: false,
        processData: false,
        xhr: function() {
            var xhr = new window.XMLHttpRequest();
            xhr.upload.onprogress = function(e) {
                if (e.lengthComputable) {
                    progress(e.loaded / e.total * 100);
                }
            };
            return xhr;
        },
        success: function(data) {
            if (data && typeof data.location === 'string') {
                resolve(data.location);
            } else {
                reject('Invalid JSON: ' + JSON.stringify(data));
            }
        },
        error: function(xhr, status, error) {
            if (xhr.status === 403) {
                reject({ message: 'HTTP Error: ' + xhr.status, remove: true });
            } else {
            reject('HTTP Error: ' + xhr.status);
          }
        }
    });
});
$('textarea').tinymce({
    skin: 'oxide-dark',
    content_css: 'dark',
    height:500,
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }',
    external_plugins: {
        'file-manager': `http://flask-news.local/static/admin/plugins/file-manager/plugin.min.js`
    },
    plugins: [
        'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
        'anchor', 'searchreplace', 'visualblocks', 'fullscreen', 'file-manager',
        'insertdatetime', 'media', 'table', 'code', 'help', 'wordcount',
    ],
    toolbar: 'undo redo | link image | code | blocks | bold italic backcolor | ' +
        'alignleft aligncenter alignright alignjustify | ' +
        'bullist numlist outdent indent | removeformat | help',
    images_file_types: 'jpg, svg, webp, png',
    file_picker_types: 'file image media',
    /* enable title field in the Image dialog */
    image_title: true,
    /* enable automatic uploads of images represented by blob or data URIs*/
    automatic_uploads: true,
    /* and here's our custom image picker*/
    file_picker_callback: (cb, value, meta) => {
        const input = document.createElement('input');
        input.setAttribute('type', 'file');
        input.setAttribute('accept', 'image/*');

        input.addEventListener('change', (e) => {
            const file = e.target.files[0];

            const reader = new FileReader();
            reader.addEventListener('load', () => {
                /*
                  Note: Now we need to register the blob in TinyMCEs image blob
                  registry. In the next release this part hopefully won't be
                  necessary, as we are looking to handle it internally.
                */
                const id = 'blobid' + (new Date()).getTime();
                const blobCache =  tinymce.activeEditor.editorUpload.blobCache;
                const base64 = reader.result.split(',')[1];
                const blobInfo = blobCache.create(id, file, base64);
                blobCache.add(blobInfo);

                /* call the callback and populate the Title field with the file name */
                cb(blobInfo.blobUri(), { title: file.name });
            });
            reader.readAsDataURL(file);
        });

        input.click();
    },
    images_upload_handler: example_image_upload_handler,
    Flmngr: {
        apiKey: "FLMNFLMN", // default free key
    },
    setup: (editor) => {
        editor.on('init', (event) => {
            // ...and get Flmngr API
            editor.getFlmngr((Flmngr) => {
                // In this demo we pass Flmngr API into inner functions and callbacks.
                // You can save it somewhere and reuse without passing as an argument.
                attachOnClickListenerToButton(Flmngr);
            });
        });
    }
});
function attachOnClickListenerToButton(Flmngr) {
    let elBtn = document.getElementById("btn");
    // Style button as ready to be pressed
    elBtn.style.opacity = 1;
    elBtn.style.cursor = "pointer";
    let elLoading = document.getElementById("loading");
    elLoading.parentElement.removeChild(elLoading);
    // Add a listener for selecting files
    elBtn.addEventListener("click", () => {
        selectFiles(Flmngr);
    });
}
function selectFiles(Flmngr) {
    // Collect URLs of images of existing gallery set
    let elsExistingImages = document.querySelectorAll("#images img");
    let urls = [];
    for (let i = 0; i < elsExistingImages.length; i++)
        urls.push(elsExistingImages.item(i).src);
    Flmngr.open({
        list: urls,
        isMultiple: true,
        acceptExtensions: ["png", "jpeg", "jpg", "webp", "gif"],
        onFinish: (files) => {
            showSelectedImages(Flmngr, files);
        }
    });
}
function showSelectedImages(Flmngr, files) {
    let elImages = document.getElementById("images");
    elImages.innerHTML = "";
    /*let elP =  document.createElement("p");
    elP.textContent = files.length + " images selected";
    elImages.appendChild(elP);*/
    for (let file of files) {
        let urlOriginal = Flmngr.getNoCacheUrl(file.url);
        let el = document.createElement("div");
        el.className = "image";
        elImages.appendChild(el);
        let elDiv = document.createElement("div");
        el.appendChild(elDiv);
        let elImg = document.createElement("img");
        elImg.src = urlOriginal;
        elImg.alt = "Image selected in Flmngr";
        elDiv.appendChild(elImg);
        let elP = document.createElement("p");
        elP.textContent = file.url;
        el.appendChild(elP);
    }
}