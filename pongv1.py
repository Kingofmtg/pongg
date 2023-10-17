from ursina import *

app = Ursina()

# Constants for the game
window.color = color.black
window.borderless = False
paddle_width = 0.2
paddle_height = 2
ball_size = 0.2
initial_ball_speed = 0.06  # Adjusted initial speed

# Game entities
left_paddle = Entity(model='quad', color=color.white, scale=(paddle_width, paddle_height), position=(-7,0))
right_paddle = Entity(model='quad', color=color.white, scale=(paddle_width, paddle_height), position=(7,0))
ball = Entity(model='quad', color=color.white, scale=ball_size)

# Ball movement
ball.dx = initial_ball_speed
ball.dy = initial_ball_speed

# Score entities and display
left_score = 0
right_score = 0
left_score_text = Text(text=str(left_score), position=(-0.05,0.45), scale=2, color=color.white) # Adjusted position and scale
right_score_text = Text(text=str(right_score), position=(0.025,0.45), scale=2, color=color.white) # Adjusted position and scale

def update():
    global left_score, right_score

    # Ball movement
    ball.x += ball.dx
    ball.y += ball.dy

    # Collision with top and bottom
    if ball.y > 4.5 or ball.y < -4.5:
        ball.dy *= -1

    # Collision with paddles
    if ball.x < left_paddle.x + paddle_width and ball.y < left_paddle.y + paddle_height/2 and ball.y > left_paddle.y - paddle_height/2:
        ball.dx *= -1
    elif ball.x > right_paddle.x - paddle_width and ball.y < right_paddle.y + paddle_height/2 and ball.y > right_paddle.y - paddle_height/2:
        ball.dx *= -1

    # Scoring
    if ball.x > 8:
        left_score += 1
        left_score_text.text = str(left_score)
        reset_ball()
    elif ball.x < -8:
        right_score += 1
        right_score_text.text = str(right_score)
        reset_ball()

    # Paddle movement with boundaries
    new_left_y = left_paddle.y + (0.1 if held_keys['w'] else -0.1 if held_keys['s'] else 0)
    new_right_y = right_paddle.y + (0.1 if held_keys['up arrow'] else -0.1 if held_keys['down arrow'] else 0)

    left_paddle.y = max(-4, min(4, new_left_y)) # constraints for left paddle
    right_paddle.y = max(-4, min(4, new_right_y)) # constraints for right paddle

def reset_ball():
    global initial_ball_speed
    ball.position = (0, 0)
    ball.dx = initial_ball_speed * 1.1  # Increase speed by 10%
    ball.dy = initial_ball_speed * 1.1  # Increase speed by 10%
    initial_ball_speed = ball.dx  # Update the speed for the next reset

# Start the game
app.run()

# Useless comment here
