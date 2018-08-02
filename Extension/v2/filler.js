
function UserAction(imgData) {
    var t = document.body.getElementsByTagName("input")[0]
    var l;

    var data = {"imgstring": imgData };
    var url = 'https://yashkothari.in/api/captcha';
    console.log(imgData);
    console.log(imgData.length);
    fetch(url, {
            method: 'POST', 
	        body: JSON.stringify(data),
                headers: new Headers({
                'Content-Type': 'application/json'
            })
        }).then(res => res.json())
        .then(function(response){ 
             console.log(response.prediction);
            l = response.prediction;
            document.body.getElementsByTagName("input")[0].value = l;

        })

}

function getBase64Image(img) {
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;

    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);

    var dataURL = canvas.toDataURL("image/png");

    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
}

document.body.getElementsByTagName("input")[0].value = "filling...";
setTimeout(hola, 1000)


function hola() {
    var image = document.body.getElementsByTagName("img");

    var imgData = getBase64Image(image[1]);
    UserAction(imgData);

}
