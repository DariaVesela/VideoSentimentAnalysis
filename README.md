# CineSense
### TO VIEW THE MAIN REPORT, GO TO services/CineSense.ipynb
### FOR VIEWING THE OUTPUT FOLDERS, GO TO services/output


### About Implementation:

## Architecture

I’ve selected the hexagonal (also called **ports and adapters**) architecture for this project as it is widely used in industry settings due to its scalability and reusability. 

The architecture breaks the program down into **Domain**, **Services**, **Use cases** and **Adapters**. The Domain is the broad data that we’re working with – in this case YouTube videos and their content. Services represent the results we want to obtain from the domain – in this case a Jupyter file which presents the log of what we did with the data, and the #1 downloaded videos, #2 transcribed audio, #3 sentiment analysis, #4 emotion extraction and #5 text translation into Spanish – the result of which can be found in the output files. Because the actual implementation – which lives in the adapters folder – is decoupled from the business logic, the application can be easily maintained should the requirements change – e.g. if we want to use a different library to extract emotions, we simply modify the adapter. 

## Use cases
There are two major use cases: the actual downloading of the YouTube videos and the **actions we can perform on the content**, such as **sentiment analysis**. I have enveloped the actions into a single use case called utilities to separate the obtaining of the data and the analysis of the data. 
# Downloading Videos
Downloading videos only requires one method. I have compared the speed of download for sequential download, threading and multiprocessing. The results of this can be found in the **pandas data frame** in the Jupyter file. Unsurprisingly, the sequential method is the least efficient. The multiprocessing method is the most efficient, as this is a CPU bound task and multiprocessing is taking advantage of multi-core processors and processes downloads in parallel. The time saving is evident, as multiprocessing is roughly 4x quicker than sequential download in this case. Threading also brings a much improved result compared to sequential download, however, as this is not an I/O bound task, it is less efficient than multiprocessing. 

## Analysing Videos
The **video analysis** consists of **extracting audio**, **transcribing audio**, **extracting sentiment analysis** and **extracting emotions**. I have used the **MoviePy** library for extracting the audio and **speechrecognition** for transcribing it. For extracting emotions I’ve used the **text2emotion** library, for sentiment analysis I’ve used the **TextBlob** library (returning the polarity and sensitivity) and for translation I’ve relied on Google Translate. The results for each video can be found in the respective folder, labelled according to the name of the video. 
As the extract emotions, extract sentiment analysis and translate methods repeatedly rely on the results of the extract audio and transcribe audio methods, I have used caching to store the extracted and transcribed audio, which significantly increased the overall speed of the program. 
I have also compared the sequential, threading and multiprocessing methods for extracting audio. Once again, the multiprocessing method is the most efficient due to its suitability for CPU bound tasks. Surprisingly, the sequential method performed marginally better than the threading method. There is a variety of possible reasons for this, with a likely one being that threading creates a lot of overhead in terms of managing context switching and synchronization. Furthermore, threads working on extracting one audio might lead to contention for resources, which is avoided when using the sequential method. 
Logging
I have implemented a simple logger to inform the user regarding the state of the processing of individual videos, as well as any potential errors. 
There is also the option to use loguru for a more scaled up logging experience. 





This project requires the installation of Poetry, FFmpeg, and necessary dependencies for smooth operation across various platforms. Additionally, it contains a Jupyter notebook titled `services.ipynb` which needs to be run.

## Table of Contents
1. [Installation](#installation)
    - [Poetry](#poetry)
    - [FFmpeg](#ffmpeg)
2. [Install Project Dependencies](#install-project-dependencies)
3. [Running the Jupyter Notebook](#running-the-jupyter-notebook)

## Installation

### Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and manages (install/update) them for you.

#### Windows
Open Command Prompt or PowerShell and run the following command:
```sh
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
Add Poetry to your PATH by adding the following line to your PowerShell profile (`$PROFILE`):
```sh
$Env:Path += ";$env:APPDATA\Python\Scripts"
```

#### macOS / Linux
Open Terminal and run the following command:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```
Add Poetry to your PATH by adding the following line to your shell profile (`.bashrc`, `.zshrc`, etc.):
```sh
export PATH="$HOME/.local/bin:$PATH"
```

### FFmpeg

FFmpeg is a comprehensive multimedia framework for handling audio, video, and other multimedia files and streams.

#### Windows
1. Download FFmpeg from the official [FFmpeg website](https://ffmpeg.org/download.html).
2. Extract the downloaded zip file.
3. Add the `bin` directory of FFmpeg to your system's PATH.

#### macOS
You can install FFmpeg using Homebrew:
```sh
brew install ffmpeg
```

#### Linux
On Ubuntu/Debian-based distributions:
```sh
sudo apt update
sudo apt install ffmpeg
```
On Fedora-based distributions:
```sh
sudo dnf install ffmpeg
```

## Install Project Dependencies

Once Poetry is installed, navigate to your project directory and install the project dependencies by running:
```sh
poetry install
```

## Running the Jupyter Notebook

To run the `CineSense.ipynb` Jupyter notebook:

1. Start the Jupyter notebook server:
    ```sh
    poetry run jupyter notebook
    ```
1. In the opened Jupyter interface, navigate to and open `CineSense.ipynb`.

This will allow you to interact with the notebook and run the required services.

## Troubleshooting

- If you encounter any issues with the installation or running of the notebook, ensure all environment variables are set correctly and the paths to Poetry and FFmpeg are included in your system's PATH.
- Refer to the official documentation of [Poetry](https://python-poetry.org/docs/) and [FFmpeg](https://ffmpeg.org/documentation.html) for more detailed instructions and troubleshooting tips.

## Disclaimer:
- please note that this readme was part-generated by chatGPT.
