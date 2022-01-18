function myFunction() {
    var copyText = document.getElementById("myusername")

    copyText.select();
    
    navigator.clipboard.writeText(copyText.value);

    alert("Copied the username: " + copyText.value)
}