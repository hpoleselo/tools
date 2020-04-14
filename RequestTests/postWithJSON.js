// body (data to be sent) should be, in another section
{
	"email": "henrivis@xample.com",
	"name": "{{name}}"
}


// In this case we're using JavaScript to make our request more dinamic (using variables)
// The address to be sent is: httpbin.org/post

pm.globals.set("name", "Disgrama");

// The variable name will be then replaced on the Body (which is where the data will be sent to the wished server), in this case we're using a JSON structured body messaget

// curl command (generated on Postman)
// curl --location --request POST 'httpbin.org/post' \
// --header 'Content-Type: application/json' \
// --data-raw '{
//	"email": "henrivis@xample.com",
//	"name": "Disgrama"
//}'