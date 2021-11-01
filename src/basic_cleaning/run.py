#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, 
exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    logger.info(f"Downloading {args.input_artifact} Artifact")
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    df = pd.read_csv(artifact_local_path)

    logger.info("Dropping price outliers")

    min_price = args.min_price
    max_price = args.max_price
    idx = df['price'].between(min_price, max_price)
    df = df[idx].copy()

    logger.info("Convert last_review feature to datetime")
    df['last_review'] = pd.to_datetime(df['last_review'])

    filename = args.output_artifact
    df.to_csv(filename, index=False)

    artifact = wandb.Artifact(
        name=args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(filename)

    logger.info("Logging artifact")
    run.log_artifact(artifact)

    os.remove(filename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Very basic data cleaning"
        )

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="Fully-qualified name for the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="Name for the artifact",
        required=True
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="Describe the output artifact",
        required=True
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="Maximum rental price allowed",
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="Maximum rental price allowed",
        required=True
    )

    args = parser.parse_args()

    go(args)
