import winsound
import time


def sound():

    for _ in range(2):  # Number of repeats

        for _ in range(3):  # Number of beeps

            winsound.MessageBeep(-1)  # Sound played

        time.sleep(2)  # How long between beeps


def alarm(n):

    print(f"\nAlarm set for {n} second(s).")
    time.sleep(n)  # Waits 'n' seconds before playing sound

    sound()


def setup():

    while True:

        user_input = input(
            "\nWhat unit of time would you like to set your alarm?\n(1) Hours\n(2) Minutes\n(3) Seconds\n(4) Combination of units\n>>> ")

        if user_input == '1':

            user_input = int(
                input("Enter the number of hours you'd like to wait: "))

            wait_time = (user_input * 60) * 60
            alarm(wait_time)
            break

        elif user_input == '2':

            user_input = int(
                input("Enter the number of minutes you'd like to wait: "))

            wait_time = user_input * 60
            alarm(wait_time)
            break

        elif user_input == '3':

            user_input = int(
                input("Enter the number of seconds you'd like to wait: "))

            wait_time = user_input
            alarm(wait_time)
            break

        elif user_input == '4':

            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            seconds = int(input("Seconds: "))

            wait_time = ((hours*60)*60) + (minutes*60) + seconds
            alarm(wait_time)
            break

        else:

            print("\nPlease input a number for your desired unit of time (1-4): ")


setup()
