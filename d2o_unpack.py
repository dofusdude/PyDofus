import io, sys, os, json
from pydofus.d2o import D2OReader, InvalidD2OFile

file = sys.argv[1]

try:
    d2i_input = open(file, "rb")
    d2o_reader = D2OReader(d2i_input)
    d2o_data = d2o_reader.get_objects()

    json_output = open(file.replace("d2o", "json"), "w")
    json.dump(d2o_data, json_output, indent=4)
    json_output.close()
except InvalidD2OFile:
    pass

d2i_input.close()