from main import get_first_time


def test_run_me_daily():
    curr_time = "23:10"
    config = [
        "11 23 /bin/run_me_daily1",
        "10 23 /bin/run_me_daily2",
        "09 23 /bin/run_me_daily3"
    ]
    results = get_first_time(curr_time, config)
    expected_results = [
        "23:11 today - /bin/run_me_daily1",
        "23:10 today - /bin/run_me_daily2",
        "23:09 tomorrow - /bin/run_me_daily3",
    ]
    assert results == expected_results


def test_run_me_sixty_times():
    curr_time = "22:10"
    config = [
        "* 22 /bin/run_me_sixty_times1",
        "* 23 /bin/run_me_sixty_times2",
        "* 21 /bin/run_me_sixty_times3"
    ]
    results = get_first_time(curr_time, config)
    expected_results = [
        "22:10 today - /bin/run_me_sixty_times1",
        "23:00 today - /bin/run_me_sixty_times2",
        "21:00 tomorrow - /bin/run_me_sixty_times3",
    ]
    assert results == expected_results


def test_run_me_hourly_23():
    curr_time = "23:10"
    config = [
        "30 * /bin/run_me_hourly1",
        "10 * /bin/run_me_hourly2",
        "09 * /bin/run_me_hourly3",
    ]
    results = get_first_time(curr_time, config)
    expected_results = [
        "23:30 today - /bin/run_me_hourly1",
        "23:10 today - /bin/run_me_hourly2",
        "0:09 tomorrow - /bin/run_me_hourly3",
    ]
    assert results == expected_results


def test_run_me_hourly():
    curr_time = "22:10"
    config = [
        "30 * /bin/run_me_hourly1",
        "10 * /bin/run_me_hourly2",
        "09 * /bin/run_me_hourly3",
    ]
    results = get_first_time(curr_time, config)
    expected_results = [
        "22:30 today - /bin/run_me_hourly1",
        "22:10 today - /bin/run_me_hourly2",
        "23:09 today - /bin/run_me_hourly3",
    ]
    assert results == expected_results


def test_run_me_every_minute():
    curr_time = "23:10"
    config = [
        "* * /bin/run_me_every_minute",
    ]
    results = get_first_time(curr_time, config)
    expected_results = [
        "23:10 today - /bin/run_me_every_minute",
    ]
    assert results == expected_results


def test_empty():
    curr_time = "23:10"
    config = []
    results = get_first_time(curr_time, config)
    expected_results = []
    assert results == expected_results
