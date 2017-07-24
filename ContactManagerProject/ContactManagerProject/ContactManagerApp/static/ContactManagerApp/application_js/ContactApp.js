function searchContact(event, obj) {
  if (event.keyCode == 13) {
    var textToSearch = obj.value;
    if (textToSearch == '' || textToSearch == undefined) {
      alert('Please enter text to search...!!');
    }
    else {
      var url = '/contact/?textToSearch=' + textToSearch;
      window.open('/contact/?textToSearch=' + textToSearch, "_self");
    }
  }
}
function deleteContact(event,obj) {
  var ans = confirm('Do you really want to delete record?');
  if (ans == false)
      event.preventDefault();
}