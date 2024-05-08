# WhatsApp Web Automation Project

## Description
This project is a WhatsApp Web automation application that uses Selenium and Microsoft Edge WebDriver to interact with WhatsApp Web. The code automates various tasks such as sending messages and attachments, reading unread messages, and interacting with contacts.

## Current Progress
- **Day 2 of Development**
  - The code now supports initializing the Edge driver with a specified user profile, allowing session persistence between browser launches.
  - Implemented functionality for login via QR Code, capturing and displaying the QR for manual authentication.
  - Functions to send text messages and attachments to specific contacts are operational.
  - Ability to fetch and display unread messages, as well as retrieve the message history from specific conversations.

## Technologies Used
- Python 3.8+
- Selenium 4
- WebDriver Manager
- Microsoft Edge WebDriver
- Matplotlib for QR Code visualization
- `dotenv` library for environment variable management

## Setup
1. Clone this repository.
2. Install the necessary dependencies using `pip install -r requirements.txt` (assuming a requirements file is present).
3. Set the environment variables `PATH_TO_YOUR_EDGE_DRIVER` and `PATH_TO_YOUR_BROWSER_PROFILE_DIRECTORY` to configure the driver path and user profile directory, respectively.

## Usage
- Run the main script to start the automation. The WhatsApp Web user interface will open, and the script will wait for you to scan the QR Code when necessary.
- Use the available functions in the `WhatsApp` class to perform various operations such as sending messages or attachments.

## Contributions
Contributions are welcome! Please create a pull request to propose improvements or add new features.

## License
Distributed under the MIT License. See `LICENSE` for more information.