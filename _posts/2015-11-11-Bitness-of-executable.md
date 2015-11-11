Determining the bitness of a windows executable is realtively easy, when you know the magic.

    dumpbin /headers app.exe | grep machine
