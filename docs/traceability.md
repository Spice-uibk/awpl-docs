# Traceability

This document provides guidance on debugging, tracing, and maintaining visibility of AWPL applications.

### Development Workflow

```yaml
# 1. Write your AWPL application
# 2. Validate against schema
```

### Schema Validation

Validate your AWPL definitions before deployment:

```bash
# Example using Python (requires jsonschema package)
python -c "
import json, yaml
from jsonschema import validate

with open('schema.json') as f:
    schema = json.load(f)
with open('your-awpl-application.yaml') as f:
    doc = yaml.safe_load(f)

validate(instance=doc, schema=schema)
print('Validation passed!')
"
```
