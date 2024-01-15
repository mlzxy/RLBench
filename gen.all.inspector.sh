RLBENCH_ENHANCED_RANDOMNESS=1 python3  tools/dataset_generator.py  --tasks=all \
        --save_path=/media/xinyu/UDriveLinux/tmp/rlbench_all/inspector/ \
        --image_size=128,128 \
        --front_image_size=720,720 \
        --renderer=opengl \
        --episodes_per_task=5 \
        --processes=1 \
        --use_inspector_cam=True