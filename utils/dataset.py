import torch.utils.data as data
from PIL import Image
import os
import os.path


IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif']


def allowed_extension(filename, extensions):
    filename_lower = filename.lower()
    flag = any(filename_lower.endswith(ext) for ext in extensions)
    return flag


def create_dataset(dir, extensions):
    images = []
    for root, _, fnames in sorted(os.walk(dir)):
        for fname in sorted(fnames):
            if allowed_extension(fname, extensions):
                path = os.path.join(root, fname)
                item = (path, 0)
                images.append(item)

    return images


class DatasetFolder(data.Dataset):
    def __init__(self, root, loader, extensions, transform=None, target_transform=None):
        samples = create_dataset(root, extensions)
        if len(samples) == 0:
            raise(RuntimeError("未发现文件！"))

        self.root = root
        self.loader = loader
        self.extensions = extensions
        self.samples = samples
        self.transform = transform
        self.target_transform = target_transform

    def __getitem__(self, index):

        path, target = self.samples[index]
        sample = self.loader(path)
        if self.transform is not None:
            sample = self.transform(sample)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return sample, target

    def __len__(self):
        return len(self.samples)


def loader(path):
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')


class ImageFolder(DatasetFolder):
    def __init__(self, root, transform=None, target_transform=None,
                 loader=loader):
        super(ImageFolder, self).__init__(root, loader, IMG_EXTENSIONS, transform=transform, target_transform=target_transform)
        self.imgs = self.samples
