function updateDate() {
    return (document.getElementById("demo").innerHTML = Date());
}

function updateDateJquery() {
    return $("#demo").html(Date());
}

$(document).ready(function () {
    $("p").click(function () {
        $(this).hide();
    });
});