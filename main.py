import platform
import datetime
def main():
    f = open("/tmp/test.txt", "w")
    f.write("Current Date and time is: {}\n".format(datetime.datetime.now()))
    f.write("OS name and version is: {}".format(platform.platform(aliased=True)))
    f.close()
if __name__ == "__main__":
    main()