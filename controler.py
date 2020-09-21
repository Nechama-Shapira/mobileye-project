import os
from tfl_manager import TFLMan


def print_col(*args):
    for arg in args:
        print(arg, end=" ")


def get_frames(pls_file):
    pls = []
    found_pkl = False
    pkl = ''
    with open(pls_file, 'r') as f:
        for line in f:
            if line != "":
                line = line.split("#")[0]
                line = line.strip()
                if line == "":
                    continue
                line = os.path.abspath(line)
                if line != "" and os.path.exists(line):
                    if not found_pkl and ".pkl" in line:
                        pkl = line
                        continue
                    else:
                        pls.append(line)
                # else:
                #     if args.verbose > 1:
                #         print_col("Warning:", '''COL_YELLOW''', str(line) + "does not exists!")
    return pkl, pls


def init():
    # args = args_handler()
    pls_file = "pls.txt"
    pkl, frame_list = get_frames(pls_file)
    # tfl_manager = TFLMan(args.verbose, pkl)
    tfl_manager = TFLMan(pkl, frame_list)
    # if args.verbose > 0:
    #     print("inputs:")
    #     for arg in vars(args):
    #         print(" -", arg, ":", getattr(args, arg))
    #     print("pkl", pkl)
    return pkl, frame_list, tfl_manager


def run():
    pkl, frame_list, tfl_manager = init()
    for i in range(2, len(frame_list)):
        tfl_manager.run(i)
    # for i, frame in enumerate(frame_list):
    #     if i > 0:
    #         tfl_manager.run(i)


def main():
    run()


if __name__ == '__main__':
    main()
