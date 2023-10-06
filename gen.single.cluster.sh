RLBENCH_ENHANCED_RANDOMNESS=1 python3  tools/dataset_generator.py  --tasks=rvt$1 \
        --save_path=/scratch/xz653/datasets/rlbench/train \
        --image_size=128,128 \
        --renderer=opengl \
        --episodes_per_task=100 \
        --processes=1