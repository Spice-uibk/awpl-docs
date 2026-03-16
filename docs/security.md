# Security

### Input Validation

All AWPL applications should be validated against the JSON Schema before processing:

The schema enforces:
- Required fields (`name`, `runtime`, `config`)
- Type checking for all properties
- Enum constraints for runtime selection
- Array constraints for dependencies

### YAML Security Best Practices

- Never use `!include` or `!load` tags with untrusted input
- Avoid referencing external YAML files from untrusted sources
- Review any use of template variables for injection risks

### Documentation

The documentation site is served via HTTPS.

