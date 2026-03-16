#!/usr/bin/env python3

import json
import sys
from pathlib import Path
import pytest
import yaml
from jsonschema import ValidationError, validate

def load_schema():
    """Load the AWPL JSON schema."""
    schema_path = Path(__file__).parent.parent.parent / "src" / "schema.json"
    with open(schema_path) as f:
        return json.load(f)

def load_examples():
    """Load all example YAML files."""
    examples_dir = Path(__file__).parent.parent.parent / "tests" / "applications"
    examples = []
    for yaml_file in examples_dir.glob("*.yaml"):
        examples.append(yaml_file)
    return examples

class TestAWPLSchema:
    """Test suite for AWPL schema validation."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.schema = load_schema()
        self.examples = load_examples()

    def test_schema_exists(self):
        """Test that schema.json exists and is valid JSON."""
        assert self.schema is not None
        assert "$schema" in self.schema

    def test_examples_exist(self):
        """Test that example files exist."""
        assert len(self.examples) > 0

    @pytest.mark.parametrize("example_file", load_examples(), ids=lambda x: x.name)
    def test_example_validates(self, example_file):
        """Validate each example against the schema."""
        with open(example_file) as f:
            yaml_content = yaml.safe_load(f)

        validate(instance=yaml_content, schema=self.schema)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
