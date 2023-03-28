#type: ignore
import time
import board
import pwmio


# Define a list of tones/music notes to play.
TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4

# Create piezo buzzer PWM output.
#buzzer = pulseio.PWMOut(board.GP2, frequency=5000, duty_cycle =0)
buzzer = pwmio.PWMOut(board.GP14, frequency=660, duty_cycle=0, variable_frequency=True)

# Start at the first note and start making sound.
buzzer.frequency = TONE_FREQ[0]
buzzer.duty_cycle = 2**15  # 32768 value is 50% duty cycle, a square wave.

# Main loop will go through each tone in order up and down.
while True:
    print("Asdf")
    # Play tones going from start to end of list.
    for i in range(len(TONE_FREQ)):
        buzzer.frequency = TONE_FREQ[i]
        time.sleep(0.5)  # Half second delay.
    # Then play tones going from end to start of list.
    for i in range(len(TONE_FREQ)-1, -1, -1):
        buzzer.frequency = TONE_FREQ[i]
        time.sleep(0.5)
