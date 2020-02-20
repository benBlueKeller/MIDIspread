## Contents
  1. [Introduction](README.md#introduction)
  1. [Usage](README.md#usage)

# Introduction
  MIDIspread turns a dataset into a midi file.

  Using [MIDITime](https://github.com/cirlabs/miditime), a [Google Sheet](https://sheets.google.com), and some instructions MIDIspread makes sound out of spreadsheets

# Usage
  For MIDIspread to use Google Sheets, a Google account is used to API must be enabled and clients library installed.
    - [Step 1](https://developers.google.com/docs/api/quickstart/python#step_1_turn_on_the);
      > Click [the "Enable the Google Docs API" shortcut](https://developers.google.com/docs/api/quickstart/python#step_1_turn_on_the) to create a new Cloud Platform project and automatically enable the Google Docs API:
      >
      > Enable the Google Docs API
      >
      > In resulting dialog click DOWNLOAD CLIENT CONFIGURATION and save the file credentials.json to your working directory.

  Python3.6 is currently recommended, but any version should be OK.
  Clone into working directory and call: `$python3.6 convert.py`
