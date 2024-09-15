Register and Log In:

    Start by registering an account on the website and logging in. Upon successful login, you will be redirected to your profile page.

Observe the Token:

    On the profile page, take note of the token displayed. This token is composed of your username and account creation date, formatted as username:DD/MM/YYYY and encoded in Base64.

Understand the Token Format:

    The token follows the format username:DD/MM/YYYY. For example, if the admin user was created on 25/01/2095, the token string would be admin:25/01/2095.

Generate the Admin Token:

    Use a Base64 encoding tool to generate the token for the admin user.
    This will output the token: YWRtaW46MjUvMDEvMjA5NQ==

Access the Admin Profile:

    Send a POST request to /profile/1 with the generated token in JSON format. The request would look like:
    POST /profile/1 HTTP/1.1
    ...
    Content-Type: application/json

    {
    "token": "YWRtaW46MjUvMDEvMjA5NQ=="
    }

View the Admin Profile:

    Upon successful submission, you will access the admin profile and get the flag.

Flag is : FSIIECTF{6440b0271f39e21399d08c7b3826a336}