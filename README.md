# Poisson Flow Generative Model for Image Generation

![project5](https://github.com/f-krause/uio-ADL-project-3/assets/93521294/9c1a82b9-c8f8-4024-8428-b42f0f0e26e7)

## Set up environment
Create conda environment with provided environment.yml file. We recommend using mamba to speed up the process.
```bash
conda env create -f environment.yml
```



## Get CIFAR-10 data
In downloads:
```bash
wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
```

In root to make it zip and get data for FID score computation:
```bash
python dataset_tool.py --source=downloads/cifar-10-python.tar.gz --dest=datasets/cifar-10-python.zip
python fid.py ref --data=datasets/cifar-10-python.zip --dest=fid-refs/cifar-10-python.npz
```


## Get MNIST data
In downloads:
```bash
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz 
```

In root to make it zip and get data for FID score computation:
```bash
python dataset_tool.py --source=downloads/train-images-idx3-ubyte.gz --dest=datasets/mnist_train.zip
```


## Run CIFAR training
```bash
torchrun --standalone --nproc_per_node=4 train.py --outdir=training-runs --name pfgm_baseline_128 --data=datasets/cifar10-32x32.zip --cond=0 --arch=ddpmpp --pfgmpp=1 --batch 512 --aug_dim 128 --duration 20
```

Adapt --name to the desired name of the training run.

You can set the flags --l1prior to enable l1 prior sampling and --dct to enable DCT based training/sampling.

## Generate 50.000 images
```bash
torchrun --standalone --nproc_per_node=4 generate.py --seeds=0-49999 --outdir=training-runs/pfgm_baseline_128 --pfgmpp=1 --aug_dim=128
```

## Compute FID score
```bash
torchrun --standalone --nproc_per_node=4 fid.py calc --images=training-runs/pfgm_baseline_128 --ref=fid-refs/cifar10-32x32.npz --num 50000
```
