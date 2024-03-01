"""cli entry point"""
import sys

from keypoint_detection.tasks.eval import eval_cli
from keypoint_detection.tasks.train import train_cli

TRAIN_TASK = "train"
EVAL_TASK = "eval"
TASKS = [TRAIN_TASK, EVAL_TASK]

#python keypoint_detection/tasks/train.py \
#--keypoint_channel_configuration  "box_corner0= box_corner1 = box_corner2= box_corner3: flap_corner0:flap_corner2" \
#--json_dataset_path "test/test_dataset/coco_dataset.json" --json_validation_dataset_path "test/test_dataset/coco_dataset.json" --batch_size  2 --wandb_project "keypoint-detector-integration-test" \
#--max_epochs 50 --early_stopping_relative_threshold -1.0 --log_every_n_steps 1 --accelerator="gpu" --devices 1 --precision 16 --augment_train

# python3 cli.py train --keypoint_channel_configuration "top" --json_dataset_path "test/test_dataset/coco_dataset.json" --json_validation_dataset_path "test/test_dataset/coco_dataset.json" --batch_size  2 --wandb_project "keypoint-detector-integration-test" \
#--max_epochs 50 --early_stopping_relative_threshold -1.0 --log_every_n_steps 1 --accelerator="gpu" --devices 1 --precision 16 --augment_train

def main():
    # read command line args in plain python

    # TODO this is a very hacky approach for combining independent cli scripts
    # should redesign this in the future.

    print(sys.argv)
    task = sys.argv[1]
    sys.argv.pop(1)

    if task == "--help" or task == "-h":
        print("Usage: keypoint-detection [task] [task args]")
        print(f"Tasks: {TASKS}")
    elif task == TRAIN_TASK:
        train_cli()
    elif task == EVAL_TASK:
        eval_cli()
