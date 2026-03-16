# AWPL Documentation

AWPL (Abstract Workflow Pipeline Language) is a declarative abstraction for defining both batch and stream applications in a human-readable format using YAML.

## Quickstart

### Prerequisites

- Ruby 3.0+
- Bundler
- Python 3.8+ (for schema validation tests)

### Local Deployment

```bash
cd src
bundle install
bundle exec jekyll serve
```

Access the documentation at [http://localhost:4000/awpl-docs/](http://localhost:4000/awpl-docs/)

### Using Deployment Scripts

```bash
# Local deployment
./deploy/local.sh
```

## Testing

### Continuous Integration
Tests run on every push using CI/CD.

### Running Tests Locally

```bash
# Install validation dependencies
pip install jsonschema pyyaml

# Run tests
pytest -v tests/ 
```

## Documentation

- [Architecture](docs/architecture.md)
- [Security](docs/security.md)
- [Traceability](docs/traceability.md)

