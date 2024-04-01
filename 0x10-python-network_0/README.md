# HTTP Basics README

## Overview
This README provides a brief overview of some fundamental concepts related to HTTP (Hypertext Transfer Protocol), including URLs, HTTP methods, request and response headers, and curl options.

## URL Components
- **Scheme**: Indicates the protocol used, such as HTTP or HTTPS.
- **Subdomain**: Optional part of a domain that comes before the domain name.
- **Domain**: The main part of the URL, typically identifying a website.
- **Resource Path**: Specifies the location of a specific resource on the server.
- **Query String**: Contains key-value pairs used for passing data to the server.

## HTTP Methods
- **GET**: Requests data from a specified resource.
- **POST**: Submits data to be processed to a specified resource.
- **PUT**: Updates data on the server.
- **DELETE**: Deletes the specified resource.
- **HEAD**: Similar to GET but retrieves only the headers, not the actual content.

## Request and Response Headers
- **Request Headers**: Provide additional information about the request, such as the User-Agent or Content-Type.
- **Response Headers**: Provide additional information about the response, such as Content-Length or Set-Cookie.

## Curl Options
- **-X, --request**: Specifies the HTTP method to use.
- **-s, --silent**: Disables the progression display.
- **-o, --output**: Saves the body of the resulting response to a file.
- **-b, --cookie**: Sets a cookie with a key-value pair.
- **-d, --data**: Sets a body key-value parameter.

## Example Usage
```bash
# Fetch a webpage
curl https://www.example.com

# Send a POST request with data
curl -X POST -d "param1=value1&param2=value2" http://www.example.com/resource

# Follow all redirects
curl -L https://www.example.com

# Save response body to a file
curl -o output.html https://www.example.com/page

# Set a cookie
curl -b "cookie_name=cookie_value" http://www.example.com
## Additional Resources
- [Mozilla Developer Network (MDN) - HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [curl Documentation](https://curl.se/docs/manpage.html)

