import requests
import os

# Your API Key from Stability
API_KEY = 'sk-0SuAWJfrViMkuAwA4DQIdODxh4Kaxa0CLHta0TtLc5YYIGem'

# The correct URL of the API endpoint you can use the conservative or fast
url = 'https://api.stability.ai/v2beta/stable-image/upscale/fast'  
# url = 'https://api.stability.ai/v2beta/stable-image/upscale/conservative'

# Input Directory : Directory (You May change it.)
input_folder = 'InputImages/' 

# Output Directory : After upscale where you will save the image
output_folder = 'OutputImages/' 

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Accept': 'image/*',
}

# Loop through all image files in the input folder
for image_name in os.listdir(input_folder):
    if image_name.lower().endswith(('jpg', 'jpeg', 'png', 'webp')):
        image_path = os.path.join(input_folder, image_name)
        print(f"Upscale starting for {image_name}!")
        print(f"Processing...")
        with open(image_path, 'rb') as image_file:
            files = {
                'image': image_file,
            }

            data = {
                'output_format': 'png',  # Default: 'png', can also be 'jpeg' or 'webp'
            }

            # Send the POST request to the API endpoint
            response = requests.post(url, headers=headers, files=files, data=data)

            # Check the response status code
            if response.status_code == 200:
                print(f"Upscale successful for {image_name}!")

                # Save the upscaled image to the output folder
                upscaled_image_path = os.path.join(output_folder, f"upscaled_{image_name}")
                with open(upscaled_image_path, 'wb') as out_file:
                    out_file.write(response.content)
            else:
                print(f"Failed to upscale image {image_name}. Status Code: {response.status_code}")
                print(f"Response: {response.text}")
