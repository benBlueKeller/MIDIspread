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
  Unstable version up on Test PyPI:
  `$ pip install --index-url https://test.pypi.org/simple/ --upgrade --no-deps  MIDIspread-ben`

  A few dependencies are needed as well:

  `$ pip install miditime`

  For MIDIspread to use Google Sheets, a Google account is used to API must be enabled and clients library installed. The first two steps in Google's Python Quickstart provide a simple guide.


  - [Step 1](https://developers.google.com/sheets/api/quickstart/python#step_1_turn_on_the);

      > Click [the "Enable the Google Docs API" shortcut] to create a new Cloud Platform project and automatically enable the Google Docs API:

      > In resulting dialog click DOWNLOAD CLIENT CONFIGURATION and save the file credentials.json to your working directory.


  - [Step 2](https://developers.google.com/sheets/api/quickstart/python#step_2_install_the_google_client_library); I've found it best to install the pip packages one at a time.

      > Run the following command to install the library using pip:

      > `$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

      > See the library's installation page for the alternative installation options.

      *[Link to installation page](https://github.com/googleapis/google-api-python-client)*

### Run

An example using the default periodic table:
```python
from MIDIspread.convert import Convert
converter = Convert(
      find_pitch=lambda pi: 81 - pi * 2, find_velocity=lambda ve: 100 - ve * 4,
)
converter.data_to_file()
```
The Convert class can turn a range  any four google sheets columns into a midi file using the following parameters:
* spreadsheet_id (str): id of google sheet
* range (str): sheet range in a1 notation for notes.
    One to four columns can be used (with defaults for missing columns);
    time in first column, pitch in second (or first),
    velocity in third (or 100), duration in fourth (or 1).
* bpm (int): beats per minute for the midi output
* find_time(function): conversion function for time;
    the output will be when a note happens
* find_pitch(function): conversion function for pitch;
    how high or low is it?
* find_velocity(function): conversion function for velocity;
    how strong?
* find_duration(function): conversion function for duration;
    how long?
