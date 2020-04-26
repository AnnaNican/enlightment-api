# Enlightenment API

REST-style service designed to inspire reason, science, humanism and progress. The API was inspired by Steven Pinker’s book “Enlightenment Now” and aims to make knowledge and opinions shared in the book accessible in small, but inspiring fragments. 

## Access to the API
All requests to the API begin with:

`https://enlightenment-api.herokuapp.com`

Currently the following request is available

`https://enlightenment-api.herokuapp.com/chart`
And it returns a .jpeg image of charts used in the book. 

### Try It
`curl -XGET https://enlightenment-api.herokuapp.com/chart > chart.png`




