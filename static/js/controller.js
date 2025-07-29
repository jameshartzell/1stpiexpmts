function controller(){
    var zone = document.getElementById("zone");
    var zr = zone.getBoundingClientRect();
    var p = document.getElementById("print");
    p.innerHTML = zr.height + " x " + zr.width;

}

(function() {
    document.onmousemove = handleMouseMove;
    function handleMouseMove(event) {
        var eventDoc, doc, body;
        var zone = document.getElementById("zone");
        var zr = zone.getBoundingClientRect();
        var p = document.getElementById("print");

        event = event || window.event; // IE-ism

        // If pageX/Y aren't available and clientX/Y are,
        // calculate pageX/Y - logic taken from jQuery.
        // (This is to support old IE)
        if (event.pageX == null && event.clientX != null) {
            eventDoc = (event.target && event.target.ownerDocument) || document;
            doc = eventDoc.documentElement;
            body = eventDoc.body;

            event.pageX = event.clientX +
            (doc && doc.scrollLeft || body && body.scrollLeft || 0) -
            (doc && doc.clientLeft || body && body.clientLeft || 0);
            event.pageY = event.clientY +
            (doc && doc.scrollTop  || body && body.scrollTop  || 0) -
            (doc && doc.clientTop  || body && body.clientTop  || 0 );
        }
        var pl,br,ab,bt;
        pl = parseInt(event.pageX) > parseInt(zr.x);
        br = parseInt(event.pageX) < parseInt(zr.x + zr.width);
        ab = parseInt(event.pageY) < parseInt(zr.y + zr.height);
        bt = parseInt(event.pageY) > parseInt(zr.y);
        // Use event.pageX / event.pageY here
        p.innerHTML = "x " + event.pageX +
                      "<br>y " + event.pageY +
                      "<br>top " + zr.top + " " + bt +
                      "<br>bottom " + zr.bottom + " " + ab +
                      "<br>left " + zr.left + " " + pl +
                      "<br>right " + zr.right + " " + br;

        console.log(pl && br && !ab && !bt);
        if (pl && br && ab && bt) {
            console.log("ran");
            p.style.color = "green";
            var RXR,RYR;
            RXR = (event.pageX-zr.x)/(zr.width)
            RYR = (event.pageY-zr.y)/(zr.height)
            p.innerHTML += "<br>X to send " + RXR +
                           "<br>Y to send " + RYR;
            fetch("/control", {
                method: "POST",
                body: JSON.stringify({x: RXR,y: RYR}),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            });
        } else {
            p.style.color = "black";
        };
    }
})();
