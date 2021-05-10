#!venv/bin/python3
import sys
import datetime
from typing import List


def get_first_time(curr_time: str, config: List[str]) -> List[str]:
    """Accept simulated current time and a list of config lines, and output the soonest time at which
    each of the commands will fire and whether it is today or tomorrow."""

    curr_h, curr_m = curr_time.split(":")
    curr_time = datetime.time(int(curr_h), int(curr_m))

    result = []

    for line in config:
        if len(line) > 0:
            m, h, command = line.split()

            assert h == "*" or (0 <= int(h) < 24)
            assert m == "*" or (0 <= int(m) < 60)

            if h != "*":
                if m != "*":
                    exec_h = int(h)
                    exec_m = int(m)

                    exec_day = "today" if datetime.time(exec_h, exec_m) >= curr_time else "tomorrow"
                else:
                    exec_h = int(h)
                    exec_m = curr_time.minute if exec_h == curr_time.hour else 0
                    exec_day = "today" if exec_h >= curr_time.hour else "tomorrow"
            else:
                if m != "*":
                    exec_m = int(m)
                    if exec_m >= curr_time.minute:
                        exec_h = curr_time.hour
                        exec_day = "today"
                    else:
                        exec_h = curr_time.hour + 1 if curr_time.hour < 23 else 0
                        exec_day = "tomorrow" if curr_time.hour >= 23 else "today"
                else:
                    exec_h, exec_m = curr_time.hour, curr_time.minute
                    exec_day = "today"

            exec_time = datetime.time(exec_h, exec_m)
            result.append(f"{int(exec_time.hour)}:{exec_time:%M} {exec_day} - {command}")

    return result


if __name__ == "__main__":
    inp = sys.stdin.readlines()
    results: List[str] = get_first_time(sys.argv[1], inp)
    for res in results:
        print(res)
