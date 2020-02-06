# from xlrd import open_workbook
from miditime.miditime import MIDITime
from sheets import get_range


class Convert:
    """Convert turns google sheets into midi with miditime

    Attributes:
        spreadsheet_id (str): id of google sheet
        range (str): sheet range in a1 notation for notes
        bpm (int): beats per minute for the midi output
        find_time(function, optional): conversion function for time;
            the output will be when a note happens
        find_pitch(function, optional): conversion function for pitch;
            how high or low is it?
        find_velocity(function, optional): conversion function for velocity;
            how stong?
        find_duration(function, optional): conversion function for duration;
            how long?
    """

    def __init__(
        self,
        spreadsheet_id="1YkaCukkp0w-enqqJCDNgjbM3PKimfr6Ic6lo_02PSM0",
        range="periodic!B2:D119",
        bpm=120,
        find_time=lambda ti: ti,
        find_pitch=lambda pi: pi,
        find_velocity=lambda ve=100: ve,
        find_duration=lambda du=1: du,
    ):
        super()
        self.spreadsheet_id = spreadsheet_id
        self.range = range
        self.bpm = bpm
        self.find_time = find_time
        self.find_pitch = find_pitch
        self.find_duration = find_duration
        self.find_velocity = find_velocity

        # (beats per min, output file, sec/year, base octave, octaves in range)
        self.miditime = MIDITime(self.bpm, "midi.mid", 5, 5, 1)

    def to_notelist(self):
        """to_notelist takes a string of data and optional modifier functions for
        time, pitch, velocity, and duration then returns a list of notes"""
        notelist = []
        for point in self.data_list:
            if isinstance(point, list):
                notelist.append(
                    [
                        self.find_time(point[0]),
                        self.find_pitch(point[1])
                        if len(point) > 1
                        else self.find_pitch(point[0]),
                        self.find_velocity(point[2])
                        if len(point) > 2
                        else self.find_velocity(),
                        self.find_duration(point[3])
                        if len(point) > 3
                        else self.find_duration(),
                    ]
                )
            else:
                notelist.append(
                    [
                        self.find_time(point),
                        self.find_pitch(point),
                        self.find_velocity(),
                        self.find_duration(),
                    ]
                )
        return notelist


if __name__ == "__main__":

    def str_range_to_ints(range):
        """str_range_to_ints converts sheet schema to ints.

        range-a list of lists for row in sheets
        assumes all values are integars"""
        new = []
        for row in range:
            ints = []
            for cell in row:
                ints.append(int(cell))
            new.append(ints)
        return new

    # get_Range is taking SPREADSHEET_ID and A1 notation for a range
    data = get_range("1YkaCukkp0w-enqqJCDNgjbM3PKimfr6Ic6lo_02PSM0", "periodic!B2:D119")
    miditime.add_track(
        to_notelist(
            str_range_to_ints(data),
            find_pitch=lambda pi: 81 - pi * 2,
            find_velocity=lambda ve: 100 - ve * 3,
        )
    )
    self.miditime.save_midi()
