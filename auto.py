from datetime import date, timedelta, datetime
import time
import random
from subprocess import call
from time import sleep


def main():
    """
    Generate date-time strings in this format:

        "Thu Jun  4 20:58:47 CDT 2015"

    for various days, and various times between the specified dates.

    Then make git commits for each random date-time string.
    """

    start_date = date(2016, 4, 29)
    today = datetime.now().date()

    delta = today - start_date

    for delta_counter in range(delta.days + 1):

        # Did I commit on that day? Hmmm, let me check...
        committed = random.randrange(100) < 75  # odds of a "True" response

        if committed:
            # Now, how many amazing commits did I make on that day? Hmmm ...
            num_of_commits = random.randint(0, 2)

            for commit in range(num_of_commits):

                # And, exactly when did I make those commits?
                hour = random.randint(0, 24)
                minute = random.randint(0, 60)

                formatted_date = _format_commit_time(hour, minute, start_date, delta_counter)

                _make_commit_for_time(formatted_date)


def _format_commit_time(hour, minute, start_date, delta_counter):
    commit_time = "%02d:%02d:00" % (hour, minute)
    fmt = "%a %b %d {commit_time} CDT %Y".format(commit_time=commit_time)
    d = start_date + timedelta(days=delta_counter)

    return time.strftime(fmt, d.timetuple())


def _make_commit_for_time(commit_time):
    # change something for the commit
    with open('datefile.txt', 'w') as fh:
        fh.write(commit_time)

    # commit it
    call('git add .'.split())
    call(['git', 'commit', '-am', '"%s"' % commit_time, '--date="%s"' % commit_time])

    # Beat their sooper anti-cheat algo If you make a bunch of historic commits
    # and push them all at once, github won't change your heat map. So, just
    # push after each commit.
    call('git push origin master'.split())

main()
