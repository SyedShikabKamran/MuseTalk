# MuseTalk Local Setup Guide

A simple, step-by-step guide to setting up and running MuseTalk locally with a Web GUI or real-time commands.

---

## 1. Clone the Repository

Open your terminal, paste this command, and move into the project directory:

```bash
git clone https://github.com/SyedShikabKamran/MuseTalk.git
cd MuseTalk
```

---

## 2. Create and Activate the Environment

Create an isolated environment directly inside the project folder so it does not interfere with your system:

```bash
# Create the environment
conda create --prefix ./musetalk_env python=3.10 -y

# Activate the environment
conda activate ./musetalk_env
```

---

## 3. Install Dependencies & PyTorch

Run these commands one by one to upgrade your package installer and set up the required AI framework libraries:

```bash
# Upgrade installation tools
python -m pip install --upgrade pip setuptools wheel

# Install PyTorch (CUDA 11.8 Accelerated version)
python -m pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 \
  --index-url https://download.pytorch.org/whl/cu118

# Install general project dependencies
python -m pip install -r requirements.txt

# Install core OpenMMLab computer vision engines
python -m pip install -U openmim
mim install mmengine
mim install "mmcv==2.0.1"
mim install "mmdet==3.1.0"
mim install "mmpose==1.1.0"
```

---

## 4. Download Model Weights

MuseTalk needs pre-trained model files to generate lip-syncing. Download them automatically by running:

```bash
bash download_weights.sh
```

### Manual Verification

If the download completes successfully, your `models/` directory structure should look exactly like this:

```text
models/
├── musetalk/
├── musetalkV15/
│   └── unet.pth
├── whisper/
│   └── pytorch_model.bin
├── dwpose/
│   └── dw-ll_ucoco_384.pth
├── syncnet/
│   └── latentsync_syncnet.pt
├── sd-vae/
│   └── diffusion_pytorch_model.bin
└── face-parse-bisent/
    └── 79999_iter.pth
```

Check the file structure:

```bash
ls models/musetalkV15/unet.pth \
   models/whisper/pytorch_model.bin \
   models/dwpose/dw-ll_ucoco_384.pth
```

---

## 5. How to Run MuseTalk

You have three different options to run the program depending on how you want to use it.

### Option A: Use the Web Browser GUI

Launch an interactive web interface by running:

```bash
python app.py
```

Once it starts, open your web browser and go to: **`http://127.0.0.1:7860`**

1. Upload your video or image avatar.
2. Upload your audio file.
3. Select **`v1.5`** as the model.
4. Click generate to get your result.

### Option B: Run Standard Script Inference

To run a basic lip-sync command via terminal:

```bash
bash inference.sh v1.5 normal
```

### Option C: Run Realtime Inference

This repo includes a pre-configured realtime inference config at `configs/inference/realtime.yaml`.

> ⚠️ **Important:** Realtime inference **cannot** be done through the Web UI; it must be executed strictly through the terminal using the command below.

```bash
python scripts/realtime_inference.py \
  --unet_config ./models/musetalkV15/musetalk.json \
  --unet_model_path ./models/musetalkV15/unet.pth \
  --inference_config configs/inference/realtime.yaml
```

---

## 6. Realtime Config Format

The realtime config file at `configs/inference/realtime.yaml` controls which avatars and audio clips are used.

### Example Config

```yaml
avator_1:
  preparation: True
  bbox_shift: 0
  video_path: "data/video/man4.mp4"
  audio_clips:
    audio_0: "data/audio/job_interview.wav"
```

### Config Fields Explained

| Field | Description |
| --- | --- |
| **`preparation`** | Set to `True` the first time you use a new avatar. Set to `False` on all future runs to reuse the cached avatar landmarks and save processing time. |
| **`bbox_shift`** | Adjusts the vertical position of the detected face bounding box. Start at `0`. |
| **`video_path`** | Relative local path to your target avatar video file. |
| **`audio_clips`** | One or more audio clips used to drive and animate the avatar. |

### Adding Multiple Avatars or Audio Clips

You can expand the config file to queue multiple audio tracks or even process entirely different avatars sequentially:

```yaml
avator_1:
  preparation: False
  bbox_shift: 0
  video_path: "data/video/man4.mp4"
  audio_clips:
    audio_0: "data/audio/job_interview.wav"
    audio_1: "data/audio/another_clip.wav"

avator_2:
  preparation: True
  bbox_shift: 0
  video_path: "data/video/woman1.mp4"
  audio_clips:
    audio_0: "data/audio/presentation.wav"
```

---

## 7. Where Results Are Saved

### GUI and Normal Inference

Output folders are created directly within the root results directory:

```text
results/
```

To find all generated output videos quickly, run:

```bash
find results -type f -name "*.mp4"
```

### Realtime Inference

Realtime results are isolated by version and avatar ID string:

```text
results/v15/avatars/<avatar_id>/vid_output/
```

*Example directory path for `avator_1`:*

```text
results/v15/avatars/avator_1/vid_output/
```

---

## 8. Quick Start Summary

Copy and run these commands in order to go from zero to running:

```bash
# Clone repo
git clone https://github.com/SyedShikabKamran/MuseTalk.git
cd MuseTalk

# Create and activate environment
conda create --prefix ./musetalk_env python=3.10 -y
conda activate ./musetalk_env

# Upgrade pip
python -m pip install --upgrade pip setuptools wheel

# Install PyTorch with CUDA 11.8
python -m pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 \
  --index-url https://download.pytorch.org/whl/cu118

# Install project requirements
python -m pip install -r requirements.txt

# Install OpenMMLab packages
mim install mmengine
mim install "mmcv==2.0.1"
mim install "mmdet==3.1.0"
mim install "mmpose==1.1.0"

# Download model weights
bash download_weights.sh

# Launch GUI
python app.py
```

Then open **`http://127.0.0.1:7860`** in your browser.
