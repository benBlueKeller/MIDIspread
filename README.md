## Contents
  1. [Introduction](README.md#introduction)
  1. [Usage](README.md#usage)
      1. [Installation](README.md#installation)
      1. [Run](README.md#run)

# Introduction
  MIDIspread turns a dataset into a midi file.

  Using [MIDITime](https://github.com/cirlabs/miditime), a [Google Sheet](https://sheets.google.com), and some instructions MIDIspread makes sound out of spreadsheets

# Usage

### Installation

  For MIDIspread to use Google Sheets, a Google account is used to API must be enabled and clients library installed. The first two steps in Google's Python Quickstart provide a simple guide.


  - [Step 1](https://developers.google.com/docs/api/quickstart/python#step_1_turn_on_the);

      > Click [the "Enable the Google Docs API" shortcut] to create a new Cloud Platform project and automatically enable the Google Docs API:

      > In resulting dialog click DOWNLOAD CLIENT CONFIGURATION and save the file credentials.json to your working directory.


  - [Step 2](https://developers.google.com/docs/api/quickstart/python#step_2_install_the_google_client_library); I've found it best to install the pip packages one at a time.

      > Run the following command to install the library using pip:

      > `$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

      > See the library's installation page for the alternative installation options.

      *[Link to installation page](https://github.com/googleapis/google-api-python-client)*

### Run

  Clone into working directory and call: `$python3 convert.py`
