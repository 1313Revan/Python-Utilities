## This script was developed out of spite for Road Atlanta and other tracks like it with many corners that are completely blind into harsh turns

def corners(track, total, blind):
    percentage = blind*100/total
    print('{per} percent of {cir}\'s corners are blind!'.format(cir=track,per=int(percentage)))

corners(input('What is the track name?\n'), int(input('How many corners total?\n')), int(input('How many are blind corners?\n')))