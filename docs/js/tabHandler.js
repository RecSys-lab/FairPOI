function tabHandler(evt, tabName) {
    var item, tabContent, tabLinks;
    tabContent = document.getElementsByClassName("tabContent");
    for (item = 0; item < tabContent.length; item++) {
        tabContent[item].style.display = "none";
    }
    tabLinks = document.getElementsByClassName("tabLinks");
    for (item = 0; item < tabLinks.length; item++) {
        tabLinks[item].className = tabLinks[item].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}