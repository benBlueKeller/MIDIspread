# from xlrd import open_workbook
from miditime.miditime import MIDITime

data = [1,2,3,4,5,6,7]
midi = MIDITime(120, 'midi.mid', 5, 5, 1)

def to_notelist(data,
            find_time = lambda ti: ti,
            find_pitch = lambda pi: pi,
            find_velocity = lambda ve=100: ve,
            find_duration = lambda du=1: du):
    notelist = []
    for point in data:
        if type(point) == list:
            notelist.append([
                find_time(point[0]),
                find_pitch(point[1]) if len(point) > 1 else find_pitch(point[0]),
                find_velocity(point[1]) if len(point) > 2 else find_velocity(),
                find_duration(point[3]) if len(point) > 3 else find_duration()
            ])
        else:
            notelist.append([
                find_time(point),
                find_pitch(point),
                find_velocity(),
                find_duration()
            ])
    return notelist

midi.add_track(to_notelist(data))
midi.save_midi()
