#!venv/bin/python3
import sys
import datetime


def get_first_time(curtime, config):
    """Accept config lines to STDIN and output the soonest time at which
    each of the commands will fire and whether it is today or tomorrow."""
    t = curtime.split(":")
    cur_time = datetime.time(int(t[0]), int(t[1]), 00)

    result = []

    for line in config:
        if len(line) > 0:
            m, h, command = line.split()
            execution_time = None

            if h != "*":
                if m != "*":
                    execution_time = datetime.time(int(h), int(m))
                    execution_day = "today" if execution_time > cur_time else "tomorrow"
                else:
                    h = int(h)
                    execution_day = "today" if h >= cur_time.hour else "tomorrow"
                    m = cur_time.minute if h == cur_time.hour else 0

            else:
                if m != "*":
                    m = int(m)
                    if m >= cur_time.minute:
                        h = cur_time.hour
                        execution_day = "today"
                    else:
                        h = cur_time.hour + 1 if cur_time.hour < 23 else 0
                        execution_day = "tomorrow" if cur_time.hour >= 23 else "today"
                else:
                    h, m = cur_time.hour, cur_time.minute
                    execution_day = "today"

            execution_time = execution_time if execution_time else datetime.time(h, m)
            result.append(f"{int(execution_time.hour)}:{execution_time:%M} {execution_day} - {command}")

    for res in result:
        print(res)
    return result


if __name__ == "__main__":
    get_first_time(sys.argv[1], sys.stdin)
