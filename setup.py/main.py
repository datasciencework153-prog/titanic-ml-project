import os

print("🚀 Training Pipeline Start")
os.system("python pipeline/train_pipeline.py")

print("\n🚀 Inference Pipeline Start")
os.system("python pipeline/inference_pipeline.py")