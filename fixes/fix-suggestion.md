# Auto-Fix Suggestion

```
```bash
cd /path/to/project/root && npm install
```

Or check your CI/CD pipeline working directory:

```yaml
# In your CI/CD config (GitHub Actions example)
- name: Install dependencies
  working-directory: ./app
  run: npm install
```

Or ensure package.json exists:

```bash
ls -la package.json
git status package.json
```
```