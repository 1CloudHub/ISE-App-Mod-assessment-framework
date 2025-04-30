# Troubleshooting

This page provides solutions to common issues you might encounter when working with the Legacy Application Modernization Assessment Framework documentation.

## MkDocs Issues

### Theme Not Recognized

**Error:**
```
ERROR   -  Config value 'theme': Unrecognised theme name: 'readthedocs'. The available installed themes are: mkdocs
```

**Solution:**
This error is rare since the ReadTheDocs theme is built into MkDocs. To fix this:

1. Make sure you've installed MkDocs properly:
   ```
   pip install -r requirements.txt
   ```

2. Verify the MkDocs installation:
   ```
   mkdocs --version
   ```

3. Check the theme configuration in `mkdocs.yml`:
   ```yaml
   theme:
     name: readthedocs
     language: en
     direction: ltr
     favicon: assets/favicon.png
   ```

### Python Environment Issues

If you're using a virtual environment, make sure it's activated before installing dependencies or running MkDocs:

```bash
# Create a virtual environment (if not already created)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Assessment Team Tools Installation Issues

### D2 Diagram Language Setup Issues

**Issue: D2 Extension Not Working in VS Code**

**Error:**
```
The D2 extension requires the D2 binary to be installed.
```

**Solution:**
1. Install D2 using the appropriate method for your operating system:
   ```bash
   # macOS
   brew install d2

   # Windows (using Scoop)
   scoop install d2

   # Linux
   curl -fsSL https://d2lang.com/install.sh | sh -s --
   ```

2. Verify the installation:
   ```bash
   d2 --version
   ```

3. Restart VS Code after installation.

**Issue: D2 Diagram Rendering Problems**

**Solution:**
1. Ensure Graphviz is installed (D2 dependency):
   ```bash
   # macOS
   brew install graphviz

   # Windows
   scoop install graphviz

   # Ubuntu/Debian
   sudo apt-get install graphviz
   ```

2. Check D2 configuration in VS Code settings.json:
   ```json
   {
     "d2.previewMode": "live",
     "d2.layout": "dagre"
   }
   ```

### Amazon Q Developer CLI Issues

**Issue: Authentication Failures**

**Error:**
```
Unable to locate credentials. You can configure credentials by running "aws configure".
```

**Solution:**
1. Configure AWS credentials:
   ```bash
   aws configure
   ```

2. Verify your credentials are properly set up:
   ```bash
   aws sts get-caller-identity
   ```

3. Ensure you have the necessary permissions for Amazon Q Developer.

**Issue: Amazon Q Developer CLI Not Found**

**Solution:**
1. Install and update the AWS CLI:
   ```bash
   pip install awscli
   pip install --upgrade awscli
   ```

2. Install the Q CLI plugin:
   ```bash
   aws configure add-plugin q
   ```

3. Add to PATH if necessary:
   ```bash
   # For bash/zsh
   echo 'export PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc
   source ~/.bashrc
   
   # For Windows, add to system PATH environment variable
   ```

### API Testing Tools Issues

**Issue: Postman Not Connecting to APIs**

**Solution:**
1. Check network connectivity and proxy settings
2. Verify API endpoint URLs are correct
3. Ensure authentication tokens/keys are valid
4. Check for SSL certificate issues:
   ```
   Settings > General > SSL Certificate Verification (turn off for testing only)
   ```

**Issue: Swagger Editor Not Loading**

**Solution:**
1. Try using the online version: https://editor.swagger.io/
2. For local installation issues:
   ```bash
   # Reinstall using npm
   npm uninstall -g swagger-editor
   npm install -g swagger-editor
   ```

## Role-Specific Tool Issues

### Business Analyst Tools

**Issue: Collaboration Tools Access Problems**

**Solution:**
1. Verify account credentials and permissions
2. Check network connectivity and VPN settings if required
3. Clear browser cache or try a different browser
4. Contact the collaboration platform administrator for access issues

### Solution Architect Tools

**Issue: AWS Architecture Diagram Templates Missing**

**Solution:**
1. Download the latest templates from the shared repository
2. Check access permissions to the template storage location
3. Restore from backup templates if available
4. Recreate templates using the standard AWS architecture icons

### Development Lead Tools

**Issue: Code Analysis Tools Performance Problems**

**Solution:**
1. Increase memory allocation for the tool
2. Analyze smaller code segments instead of the entire codebase
3. Update to the latest version of the tool
4. Check for conflicting plugins or extensions

### Test Lead Tools

**Issue: Test Case Templates Not Loading**

**Solution:**
1. Verify file format compatibility
2. Check for template corruption and restore from backup
3. Recreate templates using the standard format
4. Update the test management tool to the latest version

## Verification Process Issues

**Issue: Tools Verification Checklist Failures**

**Solution:**
1. Review the specific tool installation that failed
2. Follow the tool-specific troubleshooting steps above
3. Request assistance from a team member who has successfully completed setup
4. Document any environment-specific issues for future reference

## Navigation Structure

The documentation is organized into the following sections:

1. **Home** - Landing page with an introduction to the framework
2. **Framework Overview** - High-level overview of the framework
3. **Assessment Process** - Information about the engagement model, execution plan, and governance
4. **Session Activities** - Detailed information about each assessment session
5. **Resources** - Tools, roles, and success factors for the assessment
6. **Troubleshooting** - Solutions to common issues

If you need to modify the navigation structure, edit the `nav` section in the `mkdocs.yml` file.

## Other Common Issues

### Missing Plugins

**Error:**
```
ERROR   -  Config value 'plugins': The "tags" plugin is not installed
```

**Solution:**
This error occurs when a plugin is configured in `mkdocs.yml` but not installed. To fix this:

1. Make sure you've installed all required plugins:
   ```
   pip install -r requirements.txt
   ```

2. If the error persists, install the specific missing plugin:
   ```
   pip install mkdocs-tags-plugin
   ```

3. Verify the plugin configuration in `mkdocs.yml`:
   ```yaml
   plugins:
     - search
     - minify:
         minify_html: true
     - tags:
         tags_file: tags.md
   ```

### Missing Markdown Extensions

If you encounter errors related to missing Markdown extensions, ensure that all required extensions are installed:

```bash
pip install pymdown-extensions
```

### Navigation Structure Issues

If pages are missing from the navigation or not displaying correctly, check the `nav` section in the `mkdocs.yml` file to ensure all pages are properly referenced.




