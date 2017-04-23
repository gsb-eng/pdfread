
function validatePDF() {
    console.log("Validating PDF!!!!!!!!!!!");
    // emove existing errors before submitting
    var errors = document.getElementsByClassName('errorlist');
    for (let index = 0; index < errors.length; ++index) {
        errors[index].style.display = 'none';
    }
    var pdfFile = document.getElementById("id_pdf_file");
    var password = document.getElementById("id_password");
    var form = document.getElementById("id-pdf-form");

    if (password.value != "") {
        form.submit();
        return true;
    }
    var result = true;
    var file = pdfFile.files[0];

    var fileReader = new FileReader();

    fileReader.onload = function() {

        var typedarray = new Uint8Array(this.result);
        PDFJS.getDocument(typedarray).then(function(pdf) {
            console.log("File uploaded");
            form.submit();
        }, function (reason) {
            var msgEle = document.getElementById("msg-ele");
            msgEle.innerHTML = "It seems the pdf is encrypted, please provide the password";
            msgEle.style.color = "red"
            result = false;
        });
    };

    fileReader.readAsArrayBuffer(pdfFile.files[0]);
    console.log(result);
    return result;
    /*
    // The workerSrc property shall be specified.
    PDFJS.workerSrc = 'http://mozilla.github.io/pdf.js/build/pdf.worker.js';

    // Asynchronous download of PDF
    var loadingTask = PDFJS.getDocument(url);
    loadingTask.promise.then(function(pdf) {
    console.log('PDF loaded');
  
    // Fetch the first page
  
    }, function (reason) {
        // PDF loading error
        console.log("Password required!!!")
    });
   */
}
