let str1 = 'Hello World!!!:)';

console.log(str1);

function get_outer_user() {
    var id = document.getElementById("user_id").value;
    fetch('https://reqres.in/api/users/' + id.toString())
    .then(result => result.json())
    .then((output) => {
      const myJSON = JSON.stringify(output);
      document.getElementById("output").innerHTML = myJSON;
    }).catch(err => console.error(err));
  document.getElementById("output").innerHTML = "error";

}

