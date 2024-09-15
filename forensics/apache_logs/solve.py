import urllib.parse

# The URL-encoded string containing ASCII character codes
encoded_string = "%28%2B70%2C%2B108%2C%2B97%2C%2B103%2C%2B32%2C%2B105%2C%2B115%2C%2B32%2C%2B58%2C%2B32%2C%2B70%2C%2B83%2C%2B73%2C%2B73%2C%2B69%2C%2B67%2C%2B84%2C%2B70%2C%2B123%2C%2B53%2C%2B48%2C%2B49%2C%2B49%2C%2B57%2C%2B99%2C%2B49%2C%2B56%2C%2B100%2C%2B51%2C%2B99%2C%2B52%2C%2B50%2C%2B99%2C%2B56%2C%2B53%2C%2B98%2C%2B57%2C%2B101%2C%2B102%2C%2B53%2C%2B102%2C%2B48%2C%2B98%2C%2B49%2C%2B100%2C%2B100%2C%2B98%2C%2B56%2C%2B101%2C%2B52%2C%2B50%2C%2B125%29"

# Decode the URL-encoded string
ascii_code_string = urllib.parse.unquote(encoded_string)

# Convert the ASCII character codes into a list of integers
ascii_codes = [int(code.replace('+', '')) for code in ascii_code_string.strip('()').split(',')]

# Convert the ASCII codes to characters and form the flag string
flag = ''.join(chr(code) for code in ascii_codes)

# Print the flag
print(f"{flag}")

# Result : Flag is : FSIIECTF{50119c18d3c42c85b9ef5f0b1ddb8e42}
