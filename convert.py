# from xlrd import open_workbook
from miditime.miditime import MIDITime
from sheets import get_range

midi = MIDITime(120, "midi.mid", 5, 5, 1)


def to_notelist(
    data_list,
    find_time=lambda ti: ti,
    find_pitch=lambda pi: pi,
    find_velocity=lambda ve=100: ve,
    find_duration=lambda du=1: du,
):
    """to_notelist takes a string of data and optional modifier functions for
    time, pitch, velocity, and duration then returns a list of notes"""
    notelist = []
    for point in data_list:
        if isinstance(point, list):
            notelist.append(
                [
                    find_time(point[0]),
                    find_pitch(point[1]) if len(point) > 1 else find_pitch(point[0]),
                    find_velocity(point[2]) if len(point) > 2 else find_velocity(),
                    find_duration(point[3]) if len(point) > 3 else find_duration(),
                ]
            )
        else:
            notelist.append(
                [find_time(point), find_pitch(point), find_velocity(), find_duration()]
            )
    return notelist


if __name__ == "__main__":
    data = get_range("1YkaCukkp0w-enqqJCDNgjbM3PKimfr6Ic6lo_02PSM0", "periodic!B2:E119")
    midi.add_track(to_notelist(data))
    midi.save_midi()
