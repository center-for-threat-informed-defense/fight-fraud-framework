from argparse import ArgumentParser
from copy import deepcopy
from datetime import datetime
import json
from pathlib import Path
import re


"""Converts F3 data to ATT&CK Navigator layers."""

# Captures the technique ID of a top-level technique or subtechnique ID
TECHNIQUE_ID_REGEX = re.compile(r"^(AML\.T\d{4})")


def generate_matrix_layer(
    output_dir,
    layer_data,
    navigator_technique_objs,
):
    """Outputs a layer JSON file highlighting the techniques used in ATLAS."""

    # Redefine name and description
    name = "ATLAS Matrix"
    description = "Adversarial Threat Landscape for Artificial-Intelligence Systems, see atlas.mitre.org"

    # Technique highlight color
    color = "#C8E6C9"  # Light green

    # Add color to Navigator technique objects
    techniques = deepcopy(list(navigator_technique_objs.values()))
    for technique in techniques:
        technique.update({"color": color})

    # Construct layer data
    matrix_layer_data = {
        "name": name,
        "description": description,
        "techniques": techniques,
        "legendItems": [{"label": "F3 technique", "color": color}],
    }
    # Combine with default layer data
    matrix_layer_data = {**layer_data, **matrix_layer_data}

    # Define output filename
    dir_path = output_dir
    matrix_filename = "f3_layer_matrix.json"
    # Write JSON to file
    write_to_json_file(matrix_layer_data, dir_path, matrix_filename)

    print(f"Matrix layer outputted to {dir_path / matrix_filename}")


def build_navigator_technique_objs(data):
    """Returns a dictionary of Navigator layer technique objects from the provided ATLAS data.

    https://github.com/mitre-attack/attack-navigator/blob/master/layers/LAYERFORMATv4.md
    """
    # Build mapping of tactic ID to Navigator tactic name
    navigator_tactic_names = {}

    # Track Navigator technique objects
    # Keyed by unique key `techniqueID_tacticID` or `subtechniqueID`
    objs = {}

    tactics = [obj for obj in data if obj.get("tactic") is True]
    techniques = [obj for obj in data if obj.get("tactic") is not True]

    for tactic in tactics:
        # Navigator tactic names are lowercase with hyphens in place of spaces
        navigator_tactic_names[tactic["id"]] = tactic["name"].replace(" ", "-").lower()

    for technique in techniques:
        technique_id = technique["id"]

        if "tactics" in technique:
            # This is a top-level technique
            for tactic_id in technique["tactics"]:
                obj = {
                    "techniqueID": technique_id,
                    "showSubtechniques": True,
                    "tactic": navigator_tactic_names[tactic_id],
                }
                objs[f"{technique_id}_{tactic_id}"] = obj

        else:
            # Otherwise, is a subtechnique
            obj = {"techniqueID": technique_id}
            objs[f"{technique_id}"] = obj

    return objs


def write_to_json_file(obj, output_dir, filename):
    """Outputs the specified object to JSON file,
    Creates the output directory if not exists.
    """
    # Assumes a Path directory param - if passed a string, convert to a Path
    if not isinstance(output_dir, Path) and isinstance(output_dir, str):
        output_dir = Path(output_dir)

    # Create the output directory if needed, included nested directories
    output_dir.mkdir(parents=True, exist_ok=True)

    # Construct output filepath
    output_filepath = output_dir / filename

    # Write JSON to file
    with open(output_filepath, "w") as f:
        json.dump(obj, f, indent=4)


if __name__ == "__main__":
    """Main entry point to F3 Navigator layer JSON file generation."""

    print("running generate_navigator_layer")

    parser = ArgumentParser(
        description="Creates a Navigator JSON file showing tactics and techniques used by F3."
    )
    parser.add_argument(
        "-f",
        type=str,
        dest="atlas_data_filepath",
        default="src/data/matrix-data.json",
        help="Path to F3 source data file",
    )

    parser.add_argument(
        "-o",
        type=str,
        dest="output_filepath",
        default="public/",
        help="Output filepath for Navigator JSON",
    )
    # Matrix layer gets updated when tactics and techniques change
    parser.add_argument(
        "-l",
        "--layer",
        choices=["matrix", "case_study"],
        dest="layer",
        default="matrix",
        help="Output specific layers, otherwise outputs all",
    )

    args = parser.parse_args()

    output_filepath = Path(args.output_filepath)
    output_filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(args.atlas_data_filepath) as f:
        data = json.load(f)
        # Define common Navigator layer info
        # nav-app/src/assets/config.json's version name before the 'vX' - domain name
        domain = "f3-f3"

        # Base for all layers
        layer_data = {
            "versions": {"layer": "4.5", "navigator": "4.6.4"},
            "domain": domain,
            "metadata": [{"name": "f3_data_version", "value": "v1.0"}],
        }
        navigator_technique_objs = build_navigator_technique_objs(data)
        generate_matrix_layer(output_filepath, layer_data, navigator_technique_objs)

    print("Done!")
