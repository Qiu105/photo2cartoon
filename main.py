from models.photo2cartoon import Photo2Cartoon
import argparse
import shutil
from utils.utils import *

def parse_args():
    parser = argparse.ArgumentParser(description="photo2cartoon")
    parser.add_argument('--mode', type=str, default='train', help='[train / test]')
    parser.add_argument('--dataset', type=str, default='photo2cartoon', help='dataset name')
    parser.add_argument('--epoch', type=int, default=10,help='The number of training epochs')
    parser.add_argument('--iteration', type=int, default=10000, help='The number of training iterations')
    parser.add_argument('--batch_size', type=int, default=1, help='The size of batch size')
    parser.add_argument('--decay_flag', type=str2bool, default=True, help='The decay_flag')
    parser.add_argument('--lr', type=float, default=0.0001, help='The learning rate')
    parser.add_argument('--device', type=str, default='cpu', help='Set gpu mode: [cpu, cuda]')
    args = parser.parse_args()
    args.result_dir = './ex'

    return check_args(args)


def check_args(args):
    check_folder(os.path.join(args.result_dir, args.dataset, 'model'))
    check_folder(os.path.join(args.result_dir, args.dataset, 'img'))
    check_folder(os.path.join(args.result_dir, args.dataset, 'test'))
    shutil.copy(__file__, args.result_dir)
    return args
    
def main():
    args = parse_args()
    if args is None:
        exit()

    net = Photo2Cartoon(args)
    net.build_model()

    if args.mode == 'train':
        net.train()
        print(" [*] Train finished!")

    if args.mode == 'test':
        net.test()
        print(" [*] Test finished!")


if __name__ == '__main__':
    main()
