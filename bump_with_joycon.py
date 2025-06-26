import pygame
import time

# Initialize pygame
pygame.init()
pygame.joystick.init()
pygame.mixer.init()

# Try to connect the first controller
if pygame.joystick.get_count() == 0:
    print("❌ No controller detected. Please connect a controller and try again.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"✅ Controller connected: {joystick.get_name()}")

# Load wall bump sound effect
sound = pygame.mixer.Sound("se_wall_bump.wav")

hold_start = None
threshold = 0.5  # Movement sensitivity threshold
bump_hold_time = 1.5  # Seconds to hold direction before triggering bump
play_interval = 1.0  # Interval between repeated sounds

last_play_time = 0

print("🎮 Move left or right Joy-Con stick for 1.5 seconds to trigger wall bump sound")

while True:
    pygame.event.pump()

    try:
        x = joystick.get_axis(0)
        y = joystick.get_axis(1)
    except IndexError:
        x = y = 0

    is_pushing = abs(x) > threshold or abs(y) > threshold
    current_time = time.time()

    if is_pushing:
        if hold_start is None:
            hold_start = current_time
        elif current_time - hold_start >= bump_hold_time:
            if current_time - last_play_time >= play_interval:
                print("🔊 Wall bump sound triggered")
                sound.play()
                last_play_time = current_time
    else:
        hold_start = None

    time.sleep(0.01)