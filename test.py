import os
import cv2
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--photo_path', type=str, help='input photo path')
parser.add_argument('--save_path', type=str, help='cartoon save path')
args = parser.parse_args()

os.makedirs(os.path.dirname(args.save_path), exist_ok=True)

if __name__ == '__main__':
    img = cv2.cvtColor(cv2.imread(args.photo_path), cv2.COLOR_BGR2RGB)
    c2p = P2C_test()
    cartoon = c2p.inference(img)
    if cartoon is not None:
        cv2.imwrite(args.save_path, cartoon)
        print('Cartoon portrait has been saved successfully!')
