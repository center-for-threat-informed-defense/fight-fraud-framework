from argparse import ArgumentParser
import datetime
import json
from pathlib import Path
import uuid

import requests
from stix2 import MemoryStore, properties
from stix2.v21 import (
    AttackPattern,
    Bundle,
    CourseOfAction,
    CustomObject,
    ExternalReference,
    Identity,
    KillChainPhase,
    Relationship,
)


"""
Custom MITRE ATT&CK STIX object to be able to use the Navigator.
        https://github.com/mitre/cti/blob/master/USAGE.md#the-attck-data-model
        https://stix2.readthedocs.io/en/latest/guide/custom.html?highlight=custom#Custom-STIX-Object-Types
"""


@CustomObject(
    "x-mitre-tactic",
    [
        ("name", properties.StringProperty()),
        ("description", properties.StringProperty()),
        # https://github.com/oasis-open/cti-python-stix2/blob/master/stix2/properties.py#L197
        ("external_references", properties.ListProperty(ExternalReference)),
        ("x_mitre_shortname", properties.StringProperty()),
    ],
)
class AttackTactic:
    """Custom MITRE ATT&CK tactic STIX object."""

    def __init__(self, **kwargs):
        pass


@CustomObject(
    "x-mitre-matrix",
    [
        ("name", properties.StringProperty()),
        ("description", properties.StringProperty()),
        # https://github.com/oasis-open/cti-python-stix2/blob/master/stix2/properties.py#L197
        ("external_references", properties.ListProperty(ExternalReference)),
        (
            "tactic_refs",
            properties.ListProperty(
                properties.ReferenceProperty(valid_types="x-mitre-tactic")
            ),
        ),
    ],
)
class AttackMatrix:
    """Custom MITRE ATT&CK matrix STIX object."""

    def __init__(self, **kwargs):
        pass


# Collection object modeled as ATT&CK collection
# https://github.com/center-for-threat-informed-defense/attack-workbench-frontend/blob/master/docs/collections.md#object-version-reference-properties
@CustomObject(
    "x-mitre-collection",
    [
        ("type", properties.StringProperty()),
        ("id", properties.IDProperty(type="x-mitre-collection")),
        ("name", properties.StringProperty()),
        ("description", properties.StringProperty()),
        ("created", properties.TimestampProperty()),
        ("modified", properties.TimestampProperty()),
        ("x_mitre_version", properties.StringProperty()),
        ("spec_version", properties.StringProperty()),
        ("x_mitre_attack_spec_version", properties.StringProperty()),
        ("created_by_ref", properties.ReferenceProperty(valid_types="identity")),
        (
            "object_marking_refs",
            properties.ListProperty(properties.IDProperty(type="x-mitre-collection")),
        ),
        ("x_mitre_contents", properties.ListProperty(properties.DictionaryProperty())),
    ],
)
class AttackCollection:
    """Custom MITRE ATT&CK collection STIX object."""

    def __init__(self, **kwargs):
        pass


class F3:
    """Converts from F3 JSON data to STIX."""

    def __init__(self, atlas_data, source_name, existing_stix_json=None):
        """Initialize an ATLAS object.  Defaults provided via arguments in main.

        Args:
            atlas_data (str): Dictionary of ATLAS.yaml data
        """
        self.uuid_domain = uuid.UUID("atlas.mitre.org.".encode("utf-8").hex())
        self.source_name = source_name
        self.parse_data_files(atlas_data)
        # Track ATLAS tactics by short ID for matrix ordering lookup
        self.tactic_mapping = {}
        # Existing STIX JSON, i.e. for ATT&CK Enterprise data
        self.existing_stix_json = existing_stix_json

    def parse_data_files(self, atlas_data):
        """Sets attributes from the ATLAS data."""
        self.data_id = "F3"
        self.data_name = "MITRE Fight Financial Fraud Framework"
        self.data_version = "1.0"

        if not isinstance(atlas_data, list):
            raise ValueError(
                "Expected atlas_data to be a list of objects (loaded JSON array)."
            )

        # need to create a matrix object here:
        self.matrices = []

        self.tactics = [obj for obj in atlas_data if obj.get("tactic") is True]
        self.techniques = [obj for obj in atlas_data if obj.get("tactic") is not True]
        print("number of techniques ", len(self.techniques))
        self.mitigations = []
        self.attack_derived_techniques = [
            obj for obj in self.techniques if obj.get("isAttack") is True
        ]
        self.attack_derived_tactics = [
            obj for obj in self.tactics if obj.get("isAttack") is True
        ]

        self.id_mapping = {t["id"]: t for t in atlas_data if "id" in t}

    def find_stix_technique_by_external_ref_id(self, stix_objects, external_ref_id):
        """Returns the corresponding STIX technique object for an ATLAS ID, or None if none are found."""
        # Look for an ATT&CK technique that has the corresponding ID
        return next(
            (
                obj
                for obj in stix_objects
                if obj["type"] == "attack-pattern"
                and obj["external_references"][0]["external_id"] == external_ref_id
            ),
            None,
        )

    def to_stix_json(self, stix_output_filepath, atlas_url, identity_name):
        """Saves a STIX JSON file of the ATLAS tactics and techniques info.

        STIX Bundle specs
        https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_nuwp4rox8c7r
        """

        # Convert ATLAS techniques first to populate the referenced ATT&CK tactics
        # Only for parent techniques, as subtechniques do not have tactics references

        stix_techniques = []
        relationships = []
        parent_technique = None
        for t in self.techniques:

            if len(t["id"].split(".")) > 1:
                # Create subtechnique and relationship
                subtechnique, relationship = self.subtechnique_to_attack_pattern(
                    t, parent_technique, atlas_url
                )
                # Add to trackers
                stix_techniques.append(subtechnique)
                relationships.append(relationship)
            else:
                # Create and add this technique
                technique = self.technique_to_attack_pattern(t, atlas_url)
                stix_techniques.append(technique)
                # Save off reference to this technique for use by its subtechniques, should there be any following
                parent_technique = technique
        print(
            f"Converted {len(stix_techniques)} techniques ({len(stix_techniques) - len(relationships)} top-level, {len(relationships)} subtechniques) to STIX objects."
        )
        print(f"Created {len(relationships)} subtechnique relationships.")
        # Convert F3 tactics to x-mitre-tactics
        stix_tactics = [
            self.tactic_to_mitre_attack_tactic(t, atlas_url) for t in self.tactics
        ]
        print(f"Converted {len(stix_tactics)} tactics to STIX objects.")
        external_references = [
            ExternalReference(
                source_name=self.source_name,
                url=atlas_url,
                external_id=self.source_name,  # https://github.com/mitre-attack/attack-navigator/issues/362
            )
        ]
        # create matrix
        stix_matrices = []
        tactic_refs = [t.id for t in stix_tactics]
        print(f"\tGenerated {len(tactic_refs)} tactic references for matrix")
        matrix_uuid = uuid.uuid5(self.uuid_domain, "F3-matrix")
        stix_matrix_obj = AttackMatrix(
            id=f"x-mitre-matrix--{matrix_uuid}",
            name="Fight Financial Fraud Matrix",
            description=f"{self.data_id} matrix for Fight Financial Fraud",
            external_references=external_references,
            tactic_refs=tactic_refs,
            allow_custom=True,
        )
        stix_matrices.append(stix_matrix_obj)
        print(f"Created {len(stix_matrices)} STIX matrix objects.")

        stix_data_objects = (
            stix_tactics + stix_techniques + relationships + stix_matrices
        )
        collection_uuid = uuid.uuid5(self.uuid_domain, "F3-collection")
        stix_collection_obj = AttackCollection(
            id=f"x-mitre-collection--{collection_uuid}",
            type="x-mitre-collection",
            name=f"{self.data_id}",
            description=f"{self.data_name}",
            # created = curr_datetime,
            # modified = curr_datetime,
            spec_version="2.1",
            x_mitre_version="0.1",
            x_mitre_attack_spec_version="2.1.0",
            created_by_ref="identity--f1e3e4d7-42b2-5b41-bbee-ffa8f4a03996",
            object_marking_refs=[],
            # Loop through data objects to store their references in this collection
            x_mitre_contents=[
                {"object_ref": obj.id, "object_modified": obj.modified}
                for obj in stix_data_objects
            ],
        )
        print(f"Created STIX collection object.")
        # JSON
        print("Bundling and serializing ATLAS data to JSON file...")
        bundle_uuid = uuid.uuid5(self.uuid_domain, "ATLAS-bundle")
        bundle = Bundle(
            id=f"bundle--{bundle_uuid}",
            objects=stix_data_objects
            + [stix_collection_obj],  # Collection is bundled along with data
            allow_custom=True,  # Needed as ATT&CK data has custom objects
        )

        # Convert to JSON
        stix_json = json.loads(bundle.serialize())
        with open(stix_output_filepath, "w") as f:
            json.dump(stix_json, f)

    def build_atlas_external_references(self, t, atlas_url, route="techniques"):
        """Returns a STIX External Reference for ATLAS data."""

        # Construct the full URL to the resource
        url = atlas_url + "/" + route + "/" + t["id"]

        # External references is a list
        return [
            ExternalReference(
                source_name=self.source_name,  # The only required property
                url=url,
                external_id=t["id"],
            )
        ]

    def tactic_to_mitre_attack_tactic(self, t, atlas_url):
        """Returns a STIX x-mitre-tactic representing this tactic."""
        tactic_uuid = uuid.uuid5(self.uuid_domain, t["id"])
        at = AttackTactic(
            id=f"x-mitre-tactic--{tactic_uuid}",
            name=t["name"],
            description=t["description"],
            external_references=self.build_atlas_external_references(
                t, atlas_url, "tactics"
            ),
            x_mitre_shortname=t["name"].lower().replace(" ", "-"),
            created="2026-04-02T19:15:57.686Z",
            modified=t["lastModified"],
        )

        # Track this tactic by short ID
        self.tactic_mapping[t["id"]] = at

        return at

    def technique_to_attack_pattern(self, t, atlas_url):
        """Returns a STIX AttackPattern representing this technique."""
        technique_uuid = uuid.uuid5(self.uuid_domain, t["id"])
        return AttackPattern(
            id=f"attack-pattern--{technique_uuid}",
            name=t["name"],
            description=t["description"],
            # kill_chain_phases=self.referenced_tactics_to_kill_chain_phases(
            #     t["tactics"]
            # ),
            external_references=self.build_atlas_external_references(t, atlas_url),
            # Needed by Navigator else TypeError technique.platforms is not iterable
            allow_custom=True,
            x_mitre_platforms=["ATLAS"],
            created="2026-04-02T19:15:57.686Z",
            modified=t["lastModified"],
        )

    def subtechnique_to_attack_pattern(self, t, parent, atlas_url):
        """Returns a STIX AttackPattern representing this subtechnique and a STIX Relationship
        between this subtechnique and its parent.

        https://github.com/mitre/cti/blob/master/USAGE.md#sub-techniques
        """
        subtechnique_uuid = uuid.uuid5(self.uuid_domain, t["id"])
        subtechnique = AttackPattern(
            id=f"attack-pattern--{subtechnique_uuid}",
            name=t["name"],
            description=t["description"],
            external_references=self.build_atlas_external_references(t, atlas_url),
            # Needed by Navigator else TypeError technique.platforms is not iterable
            allow_custom=True,
            x_mitre_platforms=["ATLAS"],
            x_mitre_is_subtechnique=True,
            created="2026-04-02T19:15:57.686Z",
            modified=t["lastModified"],
        )

        relationship_uuid = uuid.uuid5(
            self.uuid_domain, f"{t['id']}-subtechnique-of-{parent.id}"
        )
        relationship = Relationship(
            id=f"relationship--{relationship_uuid}",
            source_ref=subtechnique.id,
            relationship_type="subtechnique-of",
            target_ref=parent.id,
            created="2026-04-02T19:15:57.686Z",
            modified=t["lastModified"],
        )

        return subtechnique, relationship


if __name__ == "__main__":
    """Main entry point to STIX file generation for ATLAS data."""

    print("running generate_stix")

    parser = ArgumentParser(
        description="Creates a STIX JSON file showing tactics and techniques used by F3."
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
        default="public/f3-stix.json",
        help="Output filepath for STIX JSON",
    )
    parser.add_argument(
        "--url",
        type=str,
        dest="atlas_url",
        default="https://atlas.mitre.org",
        help="URL to ATLAS website for Navigator item linking",
    )
    parser.add_argument(
        "--identity_name",
        type=str,
        dest="identity_name",
        default="MITRE ATLAS",
        help="Name of the creator identity",
    )
    args = parser.parse_args()

    output_filepath = Path(args.output_filepath)
    output_filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(args.atlas_data_filepath) as f:
        data = json.load(f)

        f3 = F3(data, "mitre-f3")
        f3.to_stix_json(
            output_filepath,
            args.atlas_url,
            args.identity_name,
        )
