/**
 * Created by lvhuiyang on 2016/11/9.
 */
window.onload = initPage;

function initPage() {
    accordion = document.getElementById("accordion").getElementsByTagName("a");
    for (var i = 0; i < accordion.length; i++) {
        link = accordion[i];
        link.onclick = function () {
            // find the image name
            //alert('Hello');
            //detailURL = 'competition.html';
            //document.getElementsByClassName("content").innerHTML = "HTML";
            getDetails(this.title);
        };
    }

    function createRequest() {
        try {
            request = new XMLHttpRequest();
        } catch (tryMS) {
            try {
                request = new ActiveXObject("Msxm12.XMLHTTP");
            } catch (otherMS) {
                try {
                    request = new ActiveXObject("Microsoft.XMLHTTP");
                } catch (failed) {
                    request = null;
                }
            }
        }
        return request;
    }

    function getDetails(title) {
        request = createRequest();
        if (request == null) {
            alert("无法创建请求对象，请检查是否开启JS?");
            return request;
        }
        var url = "for_request/" + title + '.html';
        request.open("GET", url, true);
        request.onreadystatechange = displayDetails; // 回调函数
        request.send(null);
    }


    function displayDetails() {
        if (request.readyState == 4) {

            detailDiv = document.getElementById("content");
            detailDiv.innerHTML = request.responseText;
        }
    }
}