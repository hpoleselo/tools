// reqres.in/api/users/{{randomVal}}
// We don't need a body to use GET (but it can be used)

// This script will be ran before the request (GET)
var random = Math.floor(Math.random()*10);
// Meaning the randomVal in the reqres.in/api/users/{{randomVal}} will be randomly calculated
pm.variables.set('randomVal', random); 