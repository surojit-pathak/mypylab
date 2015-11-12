#!/usr/bin/env python
#
# Functionality:
#
"""
Sample Usage:
"""

from lxml import html
import requests
HINDUSTANI_NOTES = ['S', 'r', 'R', 'g', 'G', 'm', 'M', 'P', 'd', 'D', 'n', 'N']
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
# My scale offset is C -> C#
NOTES = ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']
NOTES_NUM=len(NOTES)
open_chords = ['A', 'C', 'D', 'E', 'F', 'G']
open_chords_wt_map = {'A':2, 'C':1, 'D':2, 'E':2, 'F':1, 'G':1}

def form_maj_scale(key):
    MAJOR_DIST = { 1 : 2, 2 : 4, 3 : 5, 4 : 7, 5 : 9, 6 : 11, 7 : 12 }
    major = [key]
    j = 1
    while j < 7:
        major.append(NOTES[((MAJOR_DIST[j] + fi) % NOTES_NUM)]) 
        j = j + 1
    return major

def form_chords(scale):
    print scale
    LEN = len(scale)
    assert LEN == 7
    chords = []
    for ix in range(0, 7):
        triads = [scale[ix], scale[(ix + 2) % LEN], scale[(ix + 4) % LEN]]
        root = NOTES.index(triads[0])
        third = NOTES.index(triads[1])
        fifth = NOTES.index(triads[2])
        if root > third:
            third = third + NOTES_NUM
        if third > fifth:
            fifth = fifth + NOTES_NUM
        dist = third - root
        dist2 = fifth - third
        if dist == 4:
           # chords.append(triads[0] + 'maj')
           chords.append(triads[0] + '-maj')
           assert dist2 == 3
        elif dist == 3:
           if dist2 == 4:
              chords.append(triads[0] + '-min')
           elif dist2 == 3:
              chords.append(triads[0] + '-dim')
           else:
              raise Exception('Anomaly!')
        else:
              raise Exception('Anomaly!')

    return chords

def chrod_transpose(capo_pos):
    transpose_chords = []
    transpose_chords_map = {}
    for ch in open_chords:
        ix = NOTES.index(ch)
        ix = (ix + capo_pos) % NOTES_NUM
        transpose_chords.append(NOTES[ix])
        transpose_chords_map[NOTES[ix]] = ch
    return transpose_chords, transpose_chords_map
         

def find_best_match_for_chords(chords):
    find_map = []
    max_wt = 0
    max_ix = -1
    for ix in range(0, 12):
        tx_chds, tx_chds_map = chrod_transpose(ix)
        total = 0
        for ch in chords:
            main_ch = ch.split('-')[0]
            sfx = ch.split('-')[1]
            if sfx == 'dim':
                continue
            try:
                found = tx_chds.index(main_ch)
            except ValueError:
                found = -1 
            if found > -1:
                map_ch = tx_chds_map[main_ch]
                wt = open_chords_wt_map[map_ch]
                found = 0
                if sfx == 'maj' or (sfx == 'min' and wt == 2):
                    found = 1
                total = total + found 
        find_map.append((ix,total))
        if total > max_wt:
            max_wt = total
            max_ix = ix
    print chords
    # print find_map
    best_map = map(lambda (x,y): (y,x), find_map)
    best_map.sort()
    best_map = best_map[-3:]
    for (x,y) in best_map:
        print("Capo pos: {pos}".format(pos=y))
        tx_chds, tx_chds_map = chrod_transpose(y)
        print tx_chds
        print tx_chds_map
                
def get_hindustani_scale():
    thaat_dict = {
        'kaafi' : 'S-R-g-m-P-D-n',
        'bhairav': 'S-r-G-m-P-D-n',
        'bhairavi': 'S-r-g-m-P-d-n',
        'bilawal': 'S-R-G-m-P-D-N',
        'kalyan': 'S-R-G-M-P-D-N',
        'khamaj': 'S-R-G-m-P-D-n',
        'Todi': 'S-r-g-M-P-d-N',
    }
    raga_dict = {
        'simhendramadhyam': 'S-R-g-M-P-d-N',
        'bhimpalasi' : 'kaafi',
        'malhar': 'kaafi',
        'ahir bhairav' : 'bhairav'
    }
  
    print "Do you want to map a raga?"
    ans = raw_input()
    if ans == 'yes':
        print "Which raga?"
        raga = raw_input()
        thaat = thaat_dict[raga_dict[raga]]
    else: 
        print "Which thaat?"
        thaat = raw_input()
        thaat = thaat_dict[thaat]
    
    return thaat

def convert_hindustani_scale_to_western(scale):
    hscale = scale.split('-')
    return map(lambda x: NOTES[HINDUSTANI_NOTES.index(x)], hscale)
    

def main():
    hscale = get_hindustani_scale()
    wscale = convert_hindustani_scale_to_western(hscale)
    find_best_match_for_chords(form_chords(wscale))
  
if __name__ == '__main__':
    main()
        


