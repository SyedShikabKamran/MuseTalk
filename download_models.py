import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from huggingface_hub import hf_hub_download

BASE = "/mnt/B2CC9B7ECC9B3C13/MuseTalk/MuseTalk/models"

folders = ["musetalk", "musetalkV15", "whisper", "dwpose", "syncnet", "sd-vae", "face-parse-bisent"]
for f in folders:
    os.makedirs(f"{BASE}/{f}", exist_ok=True)

print(f"Using endpoint: {os.environ.get('HF_ENDPOINT')}")

files_to_download = [
    ("TMElyralab/MuseTalk", "musetalk/musetalk.json", BASE),
    ("TMElyralab/MuseTalk", "musetalk/pytorch_model.bin", BASE),
    ("TMElyralab/MuseTalk", "musetalkV15/unet.pth", BASE),
    ("TMElyralab/MuseTalk", "musetalkV15/musetalk.json", BASE),
    ("openai/whisper-tiny", "pytorch_model.bin", f"{BASE}/whisper"),
    ("openai/whisper-tiny", "config.json", f"{BASE}/whisper"),
    ("openai/whisper-tiny", "preprocessor_config.json", f"{BASE}/whisper"),
    ("yzd-v/DWPose", "dw-ll_ucoco_384.pth", f"{BASE}/dwpose"),
    ("ByteDance/LatentSync", "latentsync_syncnet.pt", f"{BASE}/syncnet"),
    ("stabilityai/sd-vae-ft-mse", "config.json", f"{BASE}/sd-vae"),
    ("stabilityai/sd-vae-ft-mse", "diffusion_pytorch_model.bin", f"{BASE}/sd-vae"),
]

for repo_id, filename, local_dir in files_to_download:
    print(f"\nDownloading {filename} from {repo_id}...")
    try:
        hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=local_dir
        )
        print(f"Done: {filename}")
    except Exception as e:
        print(f"FAILED: {filename} --- Error: {e}")

print("\nDownload process complete.")
