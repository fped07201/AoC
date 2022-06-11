# with open("../input.txt",'r') as fd:
NUM_SEGMENTS_1=2
NUM_SEGMENTS_4=4
NUM_SEGMENTS_7=3
NUM_SEGMENTS_8=7

instances=0

def CheckSpecificNumSegments(length):
    if length==NUM_SEGMENTS_1 or length==NUM_SEGMENTS_4 or length==NUM_SEGMENTS_7 or length==NUM_SEGMENTS_8:
        return True
    return False

def CountInstances(outputs):

    lengths = [len(val) for val in outputs.split()]

    return sum([1 for i in lengths if CheckSpecificNumSegments(i)])

with open("../input.txt",'r') as fd:
    data_outputs = [x.split('|')[1].strip('\n').strip() for x in fd.readlines()]

    for d in data_outputs:
        instances = instances + CountInstances(d)

    print("Num instances: %d"%instances)
