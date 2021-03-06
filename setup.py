import setuptools

with open("README.md", "r") as fh:
    read_me = fh.read()

setuptools.setup(
    name="MIDIspread-ben",
    version="0.0.2",
    author="Ben Keller",
    author_email="benbluekeller@gmail.com",
    description="MIDIspread makes MIDI files with Google Sheets",
    long_description=read_me,
    long_description_content_type="text/markdown",
    url="https://github.com/benBlueKeller/MIDIspread",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
