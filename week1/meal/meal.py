def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(stime):
    # hour is entered in format ##:##
    hours, minutes = stime.split(":")
    hours = float(hours)

    # allowing user to put the time in format ##:## and ##:## a.m. or p.m.
    if minutes.endswith("p.m."):
        hours += 12
    minutes = float(minutes.split(" ")[0])

    # transform the minutes in hour by deviding it by 60 then add it to the hours
    stime = hours + (minutes / 60)
    return stime


if __name__ == "__main__":
    main()
