<h1 align="center">Welcome to MechaKaren.py 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/Rapi-Dev/mechakaren.py/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://pypi.org/project/MechaKaren.py" target="_blank">
    <img alt="Pypi" src="https://raster.shields.io/badge/Package-PyPi-informational.svg" />
  </a>
  <a href="https://discord.gg/4haKeuFn" target="_blank">
    <img alt="Discord server" src="https://discord.com/api/guilds/839184636948774963/embed.png" />
  </a>
</p>

### 🏠 [Homepage](https://github.com/Rapi-Dev/MechaKaren)

## Key Features
- Easy To Learn!
- Lightning Fast!
- Super Secure!

## Install

```sh
pip install MechaKaren
```

## Examples
```py
import MechaKaren
from MechaKaren import mechak

mechak.config(api_key="")
# Get an API key at https://api.mechakaren.xyz.
## An api key is not needed for the math endpoint.

image_response = mechak.image(filter_type="invert", image_url="https://host.galactic-hosting.xyz/files/9tMmLv2M7f0UfewoTQ4p2M1M2.png")
# The following, returns a BytesIO object.
mechak.save_filter_image(image_response)
## This lets you download the responded image.

chatbot_response = mechak.chatbot(message="Hello!")
print(chatbot_response)
# Returns the AI response.

anime_response = mechak.anime(category="slap")
print(anime_response)
# Returns an image url.

math_response = mechak.math(equation="one plus one")
print(math_response)
# Returns the math answer.
```

## Author

👤 **Daftscientist & S4qib**

* Website: https://daftscientist.com | https://sayu-chan.ml
* Github: [Daftscientist](https://github.com/Daftscientist) | [S4qib](https://github.com/S4qib)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Rapi-Dev/MechaKaren/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Daftscientist](https://github.com/Daftscientist) | [S4qib](https://github.com/S4qib).<br />
This project is [MIT](https://github.com/Rapi-Dev/MechaKaren/blob/main/LICENSE) licensed.
