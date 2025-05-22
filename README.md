<p align="center"><h1 align="center">DUCKYAI</h1></p>
<p align="center">
	<em>Whisper wisdom, code with a friendly quack!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/JCampy/DuckyAI?style=plastic&logo=opensourceinitiative&logoColor=white&color=00ffa1" alt="license">
	<img src="https://img.shields.io/github/last-commit/JCampy/DuckyAI?style=plastic&logo=git&logoColor=white&color=00ffa1" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/JCampy/DuckyAI?style=plastic&color=00ffa1" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/JCampy/DuckyAI?style=plastic&color=00ffa1" alt="repo-language-count">
</p>
<p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=Python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/PyQt5-41CD52?style=plastic&logo=qt&logoColor=white" alt="PyQt5">
    <img src="https://img.shields.io/badge/OpenAI-412991?style=plastic&logo=openai&logoColor=white" alt="OpenAI">
    <img src="https://img.shields.io/badge/pyttsx3-FFD43B?style=plastic" alt="pyttsx3">
    <img src="https://img.shields.io/badge/SpeechRecognition-FF6F00?style=plastic" alt="SpeechRecognition">
</p>
<br>

## 🔗 Quick Links

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [🚧 Work in Progress](#-work-in-progress)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

DuckyAI is an open-source project revolutionizing programming support with a rubber duck chatbot powered by AI. It assists users by generating conversational responses to code challenges. Its intuitive GUI and audio features enhance real-time interaction, making it ideal for developers seeking friendly, AI-guided advice.

---

## 👾 Features

|     |      Feature      | Summary                                                                                                                                                                                                                                                                                       |
| :-- | :---------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Uses **Python** as the primary language for development.</li><li>Utilizes a modular architecture with distinct components such as GUI, AI models, and audio processing.</li><li>Employs **OpenAI's GPT model** for conversational assistance.</li></ul>                               |
| 🔩  | **Code Quality**  | <ul><li>Follows PEP 8 guidelines for Python code styling.</li><li>Utilizes type hints for improved code readability and maintainability.</li></ul>                                                                                                                                            |
| 📄  | **Documentation** | <ul><li>Comprehensive documentation with **Python** as the primary language.</li><li>Includes detailed explanations of code functionality and usage commands.</li><li>Provides install commands for ease of setup.</li></ul>                                                                  |
| 🔌  | **Integrations**  | <ul><li>Integrates **OpenAI's GPT model** for conversational assistance.</li><li>Utilizes environment variables for API access and model configuration.</li><li>Supports integration with audio processing libraries for text-to-speech and speech-to-text functionalities.</li></ul>         |
| 🧩  |  **Modularity**   | <ul><li>Organized into distinct modules for GUI, AI models, audio processing, and speech recognition.</li><li>Encapsulates functionalities within separate components for ease of maintenance and scalability.</li><li>Promotes code reusability through modular design principles.</li></ul> |
| ⚡️ |  **Performance**  | <ul><li>Optimizes performance by utilizing **pre-trained models** for speech recognition and generation.</li><li>Implements multithreading for efficient audio capture and processing.</li><li>Focuses on real-time interaction with users for a seamless experience.</li></ul>               |
| 🛡️  |   **Security**    | <ul><li>Implements secure handling of API keys and environment variables.</li><li>Follows best practices for data handling and storage to ensure user privacy.</li><li>Regularly updates dependencies for addressing security vulnerabilities.</li></ul>                                      |
| 📦  | **Dependencies**  | <ul><li>Manages dependencies using **pip** and a **requirements.txt** file.</li><li>Ensures version control for libraries and packages used in the project.</li><li>Keeps track of dependency updates for maintaining compatibility and security.</li></ul>                                   |

---

## 🚧 Work in Progress

This project is actively being developed!  
:construction: **Features and improvements are ongoing. Expect frequent updates and new capabilities.**  
If you have suggestions or want to contribute, check out the [issues](https://github.com/JCampy/DuckyAI/issues) or [discussions](https://github.com/JCampy/DuckyAI/discussions) pages.

---

## 📁 Project Structure

```sh
└── DuckyAI/
    ├── LICENSE
    ├── requirements.txt
    └── src
        ├── assets
        ├── duck_window.py
        ├── ducky_ai_model.py
        ├── main.py
        ├── speech_to_text.py
        └── text_to_speech.py
```

### 📂 Project Index

<details open>
	<summary><b><code>DUCKYAI/</code></b></summary>
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/JCampy/DuckyAI/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Lists all Python dependencies required to run the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/DuckyAI/blob/master/LICENSE'>LICENSE</a></b></td>
				<td>- The MIT License file for this project.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details>
		<summary><b>src</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/JCampy/DuckyAI/blob/master/src/.env.example'>.env.example</a></b></td>
				<td>- Provides a template for required environment variables.<br>- Includes placeholders for sensitive information such as API keys and model configuration.<br>- Helps users set up their own <code>.env</code> file to enable secure and correct operation of the application.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/DuckyAI/blob/master/src/main.py'>main.py</a></b></td>
				<td>- Initializes a GUI application for a rubber duck chatbot using AI models for speech recognition and generation.<br>- Sets up threads for audio capture, enhancing real-time interaction with the user.<br>- Facilitates seamless communication between the user and the duck window interface.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/DuckyAI/blob/master/src/text_to_speech.py'>text_to_speech.py</a></b></td>
				<td>- Generates audio output from text using a TTS model, ensuring clean text input for accurate conversion.<br>- Handles file creation, playback, and cleanup, offering robust error handling.<br>- This functionality encapsulates text-to-speech processing within the project's architecture, providing a seamless user experience.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/DuckyAI/blob/master/src/ducky_ai_model.py'>ducky_ai_model.py</a></b></td>
				<td>- Enables interaction with OpenAI's GPT model to provide conversational assistance to users by generating responses based on input prompts.<br>- Integrates with environment variables for API access and model configuration, utilizing a friendly rubber duck persona to guide users through programming challenges.<br>- Supports maintaining chat history and synthesizing model responses into audio output for a seamless user experience.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/DuckyAI/blob/master/src/duck_window.py'>duck_window.py</a></b></td>
				<td>- Defines a customized GUI window for a Rubber Duck application.<br>- Manages window properties, loads an image, and sets up context menus for user interaction.<br>- Implements mouse event handling and an exit feature to update the application's run condition and close it gracefully.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JCampy/DuckyAI/blob/master/src/speech_to_text.py'>speech_to_text.py</a></b></td>
				<td>- Enables real-time transcription of audio captured from a microphone using a pre-trained whisper model.<br>- The processed audio is transcribed, and the resulting text is passed to another module for further processing.<br>- Additionally, it provides a method to update the condition for capturing audio.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with DuckyAI, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python 3.8+
- **Package Manager:** pip
- **OpenAI API Key:** Required for AI features

### ⚙️ Installation

1. **Clone the DuckyAI repository:**

```sh
git clone https://github.com/JCampy/DuckyAI
```

2. **Navigate to the project directory:**

```sh
cd DuckyAI
```

3. **Install the project dependencies:**

```sh
pip install -r requirements.txt
```

4. **Set up your environment variables:**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### 🤖 Usage

Run DuckyAI using the following command:

```sh
python src/main.py
```

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/JCampy/DuckyAI/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/JCampy/DuckyAI/issues)**: Submit bugs found or log feature requests for the `DuckyAI` project.
- **💡 [Submit Pull Requests](https://github.com/JCampy/DuckyAI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/JCampy/DuckyAI
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/JCampy/DuckyAI/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=JCampy/DuckyAI">
   </a>
</p>
</details>

---

## 🎗 License

This project is licensed under the [MIT License](https://github.com/JCampy/DuckyAI/blob/master/LICENSE). See the [LICENSE](https://github.com/JCampy/DuckyAI/blob/master/LICENSE) file for details.

---

## 🙌 Acknowledgments

- [OpenAI](https://openai.com/) for the GPT models and API.
- [Coqui TTS](https://github.com/coqui-ai/TTS) for open-source text-to-speech.
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) for audio input.
- [PyQt](https://riverbankcomputing.com/software/pyqt/) for the GUI framework.
- [Icons8](https://icons8.com/) for the duck icon.
- Inspiration from the [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging) concept.
- Thanks to all the open-source community!

---
