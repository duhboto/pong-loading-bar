import os
import sys
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pong_loading_bar(wait_time, total_steps):
    paddle = "║"
    ball = "⬤"
    screen_width = 40
    screen_height = 10
    colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
    reset_color = '\033[0m'

    left_paddle_y = 0
    right_paddle_y = screen_height - 2
    ball_position = [screen_width // 2, screen_height // 2]

    left_paddle_direction = 1
    right_paddle_direction = -1
    ball_direction = [-1, 1]

    pong_facts = [
        "Pong was one of the first arcade video games.",
        "Pong was released in 1972 by Atari.",
        "Pong was created by Allan Alcorn.",
        "The original Pong game was played on an oscilloscope.",
        "Pong was inspired by the Magnavox Odyssey's Table Tennis game.",
        "Atari's Pong was the first commercially successful video game.",
        "Pong was originally intended as a training exercise for Allan Alcorn.",
        "Pong helped kick-start the video game industry.",
        "The first Pong prototype was installed in a local bar in Sunnyvale, California.",
        "Pong was later released as a home console.",
        "The success of Pong led to the creation of other arcade games and consoles.",
        "Pong is considered one of the most important video games in history."
    ]

    step = 0

    clear_screen()
   
    print("Random Fact: " + random.choice(pong_facts))

    while step <= total_steps:
        # Save cursor position
        print("\033[s", end='')

        # Update paddle positions
        left_paddle_y = ball_position[1] - 1
        right_paddle_y = ball_position[1] - 1

        # Update ball position
        ball_position[0] += ball_direction[0]
        ball_position[1] += ball_direction[1]

        # Reverse ball direction if it hits the paddles or top/bottom walls
        if (ball_position[0] == 1) or (ball_position[0] == screen_width - 3):
            ball_direction[0] *= -1
        if ball_position[1] == 0 or ball_position[1] == screen_height - 1:
            ball_direction[1] *= -1

        # Draw the updated state
        for y in range(screen_height):
            left_pad = paddle if y == left_paddle_y else " "
            right_pad = paddle if y == right_paddle_y else " "
            ball_pos = ball if y == ball_position[1] else " "
            row = left_pad + " " * (screen_width - 4) + right_pad
            row = row[:ball_position[0]] + ball_pos + row[ball_position[0] + 1:]
            print(row)

        # Restore cursor position
        print("\033[u", end='')

        sys.stdout.flush()
        time.sleep(wait_time)
        step += 1

    clear_screen()
    print("Loading complete!")
    print("Random Fact: " + random.choice(pong_facts))



if __name__ == "__main__":
    pong_loading_bar(wait_time=0.05, total_steps=200)