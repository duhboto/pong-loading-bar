# Pong Animated Trivia Load Bar

Pong Animated Trivia Load Bar is a Python package that simulates a loading bar using the game Pong and displays random trivia facts.

## Installation

You can install Pong Animated Trivia Load Bar using pip:

pip install pong-animated-trivia-load-bar

javascript
Copy code

## Usage

To use Pong Animated Trivia Load Bar in your Python code, simply import the `pong_loading_bar` function from the `ponganimatedtrivialoadbar` module and call it with the desired wait time and total steps:

```python
from ponganimatedtrivialoadbar import pong_loading_bar

pong_loading_bar(wait_time=0.05, total_steps=200)
The wait_time parameter specifies the number of seconds to wait between each step of the loading bar animation. The total_steps parameter specifies the total number of steps in the loading bar animation.

Credits
This package was created by Spencer Duh.

License
Pong Animated Trivia Load Bar is licensed under the MIT License. See the LICENSE file for more information.

Contributing
If you'd like to contribute to Pong Animated Trivia Load Bar, you can:

Report a bug
Suggest a feature
Submit a pull request
When contributing code, please make sure to:

Write tests for your code
Follow the PEP 8 style guide
Document your code using Docstrings
Use Git commit conventions
Version History
0.1.0 (2023-05-05): Initial release
