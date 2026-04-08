from argparse import ArgumentParser
from copy import deepcopy
import json
from pathlib import Path


def write_to_json_file(obj, output_dir, filename):
    if not isinstance(output_dir, Path):
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_filepath = output_dir / filename

    with open(output_filepath, "w") as f:
        json.dump(obj, f, indent=4)

    return output_filepath


def get_attack_patterns(stix_bundle):
    return [
        obj
        for obj in stix_bundle.get("objects", [])
        if obj.get("type") == "attack-pattern"
    ]


def get_collection(stix_bundle):
    for obj in stix_bundle.get("objects", []):
        if obj.get("type") == "x-mitre-collection":
            return obj
    return None


def get_external_id(attack_pattern):
    for ref in attack_pattern.get("external_references", []):
        if "external_id" in ref:
            return ref["external_id"]
    return None


def build_navigator_technique_objs_from_stix(stix_bundle):
    """
    Build Navigator layer technique entries from STIX attack-pattern objects.
    """
    objs = {}

    for obj in get_attack_patterns(stix_bundle):
        technique_id = get_external_id(obj)
        if not technique_id:
            continue

        kill_chain_phases = obj.get("kill_chain_phases", [])
        is_subtechnique = obj.get("x_mitre_is_subtechnique", False)

        # Skip techniques with no tactic assignments
        if not kill_chain_phases:
            continue

        for phase in kill_chain_phases:
            tactic = phase.get("phase_name")
            if not tactic:
                continue

            entry = {
                "techniqueID": technique_id,
                "tactic": tactic,
                "enabled": True,
                "metadata": [],
                "links": [],
                "comment": "",
            }

            # Only parent techniques should expand subtechniques
            if not is_subtechnique:
                entry["showSubtechniques"] = True

            objs[f"{technique_id}_{tactic}"] = entry

    return objs


def generate_matrix_layer(
    stix_bundle,
    output_dir,
    custom_data_url,
    attack_version="17",
    navigator_version="5.3.1",
    layer_version="4.5",
    domain="f3-financial",
):
    collection = get_collection(stix_bundle)
    navigator_technique_objs = build_navigator_technique_objs_from_stix(stix_bundle)

    color = "#FFFFFF"

    techniques = deepcopy(list(navigator_technique_objs.values()))
    for technique in techniques:
        technique["color"] = color

    layer_name = "F3 Matrix"
    layer_description = (
        "Knowledge base of tactics, techniques, and procedures used by "
        "financial fraud actors, see ctid.mitre.org/fraud"
    )

    metadata = []
    if collection and collection.get("x_mitre_version"):
        metadata.append(
            {"name": "f3_stix_version", "value": collection["x_mitre_version"]}
        )

    layer = {
        "name": layer_name,
        "versions": {
            "attack": attack_version,
            "navigator": navigator_version,
            "layer": layer_version,
        },
        "domain": domain,
        "customDataURL": custom_data_url,
        "description": layer_description,
        "filters": {"platforms": ["F3"]},
        "sorting": 0,
        "layout": {
            "layout": "side",
            "aggregateFunction": "average",
            "showID": False,
            "showName": True,
            "showAggregateScores": False,
            "countUnscored": False,
            "expandedSubtechniques": "none",
        },
        "hideDisabled": False,
        "techniques": techniques,
        "gradient": {
            "colors": ["#ff6666ff", "#ffe766ff", "#8ec843ff"],
            "minValue": 0,
            "maxValue": 100,
        },
        "legendItems": [{"label": "F3 technique", "color": color}],
        "metadata": metadata,
        "links": [],
        "showTacticRowBackground": False,
        "tacticRowBackground": "#dddddd",
        "selectTechniquesAcrossTactics": True,
        "selectSubtechniquesWithParent": False,
        "selectVisibleTechniques": False,
    }

    output_path = write_to_json_file(layer, output_dir, "f3-navigator.json")
    print(f"Navigator layer written to {output_path}")
    print(f"Included {len(techniques)} tactic-technique entries.")


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Generate a Navigator layer directly from F3 STIX JSON."
    )
    parser.add_argument(
        "-f",
        "--stix-file",
        dest="stix_filepath",
        default="public/f3-stix.json",
        help="Path to F3 STIX bundle JSON",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        dest="output_dir",
        default="public/",
        help="Output directory for Navigator layer JSON",
    )
    parser.add_argument(
        "--custom-data-url",
        dest="custom_data_url",
        default="https://raw.githubusercontent.com/center-for-threat-informed-defense/fight-fraud-framework/refs/heads/main/public/f3-stix.json",
        help="Public URL to the F3 STIX bundle JSON used by Navigator",
    )
    parser.add_argument(
        "--domain",
        dest="domain",
        default="f3-financial",
        help="Navigator custom domain name",
    )
    parser.add_argument(
        "--attack-version",
        dest="attack_version",
        default="17",
        help="ATT&CK/Navigator data version string",
    )
    parser.add_argument(
        "--navigator-version",
        dest="navigator_version",
        default="5.3.1",
        help="Navigator version string",
    )
    parser.add_argument(
        "--layer-version",
        dest="layer_version",
        default="4.5",
        help="Layer format version",
    )

    args = parser.parse_args()

    with open(args.stix_filepath, "r") as f:
        stix_bundle = json.load(f)

    generate_matrix_layer(
        stix_bundle=stix_bundle,
        output_dir=Path(args.output_dir),
        custom_data_url=args.custom_data_url,
        attack_version=args.attack_version,
        navigator_version=args.navigator_version,
        layer_version=args.layer_version,
        domain=args.domain,
    )
