# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | ✅ Currently supported |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it via:
- GitHub Security Advisories
- Or send details to the repository maintainer

Please **do not** open a public issue for security concerns.

## Security Best Practices

### Environment Variables

Never commit `.env` files or expose secrets:
```bash
# .env.example — safe to commit
BACKUP_DIR=/path/to/backup
HEALTHCHECK_SERVICES=localhost:8080,api.example.com:443
BACKUP_DIRS=/data/important
```

### Permissions

- Run with minimal required privileges
- Use dedicated service accounts in production
- Restrict backup directory access

### Network

- Health checks open TCP connections — configure firewall rules appropriately
- Use TLS for any network-based services checked

### Dependencies

Run security audits regularly:
```bash
pip install pip-audit
pip-audit
```
