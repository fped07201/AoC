# with open("../input.txt",'r') as fd:
NUM_SEGMENTS_1=2
NUM_SEGMENTS_4=4
NUM_SEGMENTS_7=3
NUM_SEGMENTS_8=7

def DecodePatterns(patterns):
    pattern_dict={}
    pending_patterns=[]
    for pattern in patterns:
        length = len(pattern)
        if length==NUM_SEGMENTS_1:
            pattern_dict['1']=pattern
        elif length==NUM_SEGMENTS_4:
            pattern_dict['4']=pattern
        elif length==NUM_SEGMENTS_7:
            pattern_dict['7']=pattern
        elif length==NUM_SEGMENTS_8:
            pattern_dict['8']=pattern
        else:
            pending_patterns.append(pattern)

    for pattern in pending_patterns:
        length = len(pattern)
        if length==6:
            missing_segment = [x for x in sorted(pattern_dict['8']) if x not in sorted(pattern)][0]
            if missing_segment in sorted(pattern_dict['1']):
                pattern_dict['6']=pattern
            elif missing_segment in sorted(pattern_dict['4']):
                pattern_dict['0']=pattern
            elif missing_segment not in sorted(pattern_dict['4']):
                pattern_dict['9']=pattern

    pending_patterns.remove(pattern_dict['6'])
    pending_patterns.remove(pattern_dict['0'])
    pending_patterns.remove(pattern_dict['9'])

    for pattern in pending_patterns:
        length = len(pattern)
        if len([x for x in sorted(pattern) if x not in sorted(pattern_dict['6'])]) == 0:
            pattern_dict['5']=pattern
        elif len([x for x in sorted(pattern_dict['1']) if x not in sorted(pattern)]) == 0:
            pattern_dict['3']=pattern
        else:
            pattern_dict['2']=pattern

    return pattern_dict

def DecodeOutput(patterns_dict, output):
    for key in patterns_dict:
        if ''.join(sorted(output)) == ''.join(sorted(patterns_dict[key])):
            return key
    return None


def DecodeEntry(entry_data):
    data={}
    data['patterns_raw'] = entry_data.split('|')[0].strip('\n').strip().split()
    data['outputs_raw'] = entry_data.split('|')[1].strip('\n').strip().split()

    data['patterns_dict'] = DecodePatterns(data['patterns_raw'])

    data['outputs_decoded'] = list(map(lambda out : DecodeOutput(data['patterns_dict'], out), data['outputs_raw']))
    return int(''.join(data['outputs_decoded']))
    
with open("../input.txt",'r') as fd:
    raw_data = fd.readlines()

    output_list = list(map(DecodeEntry, raw_data))
    print("Sum of all output values = %d"%sum(output_list))