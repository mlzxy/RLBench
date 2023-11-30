RLBENCH_ENHANCED_RANDOMNESS=1 python3  tools/dataset_generator.py  --tasks=novel \
        --save_path=/home/xinyu/Workspace/RLBench/novel/train/ \
        --image_size=128,128 \
        --renderer=opengl \
        --episodes_per_task=5 \
        --processes=1