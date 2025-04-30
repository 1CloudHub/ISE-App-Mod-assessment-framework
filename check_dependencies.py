#!/usr/bin/env python3
"""
Dependency checker for Legacy Application Modernization Assessment Framework
This script checks if all required dependencies are installed and properly configured.
"""

import importlib
import sys
import subprocess
import pkg_resources

def check_package(package_name):
    """Check if a package is installed and return its version."""
    try:
        package = importlib.import_module(package_name)
        if hasattr(package, '__version__'):
            return package.__version__
        else:
            try:
                return pkg_resources.get_distribution(package_name).version
            except:
                return "Unknown version"
    except ImportError:
        return None

def main():
    """Main function to check dependencies."""
    print("Checking dependencies for Legacy Application Modernization Assessment Framework...\n")
    
    # Define required packages
    required_packages = {
        'mkdocs': 'Core MkDocs package',
        'pymdownx': 'PyMdown Extensions'
    }
    
    # Define optional packages
    optional_packages = {
        'mkdocs_minify_plugin': 'MkDocs Minify Plugin',
        'mkdocs_git_revision_date_localized_plugin': 'Git Revision Date Plugin',
        'PIL': 'Pillow (for social cards)',
        'cairosvg': 'CairoSVG (for social cards)',
        'mkdocs_tags_plugin': 'MkDocs Tags Plugin'
    }
    
    all_required_installed = True
    
    # Check required packages
    print("Required Dependencies:")
    for package, description in required_packages.items():
        version = check_package(package)
        if version:
            print(f"✅ {description} is installed (version: {version})")
        else:
            print(f"❌ {description} is NOT installed")
            all_required_installed = False
    
    # Check optional packages
    print("\nOptional Dependencies:")
    # ReadTheDocs theme is built into MkDocs, no need to check for it
    for package, description in optional_packages.items():
        version = check_package(package)
        if version:
            print(f"✅ {description} is installed (version: {version})")
        else:
            print(f"ℹ️ {description} is NOT installed")
    
    # Print summary
    print("\nSummary:")
    if all_required_installed:
        print("✅ All required dependencies are installed. You can run 'mkdocs serve' to start the documentation server.")
    else:
        print("❌ Some required dependencies are missing. Please run 'pip install -r requirements.txt' to install them.")
        print("   For more information, see the troubleshooting guide in docs/troubleshooting.md")
    
    return 0 if all_required_installed else 1

if __name__ == "__main__":
    sys.exit(main())
