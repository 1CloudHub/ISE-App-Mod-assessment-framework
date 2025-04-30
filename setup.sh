#!/bin/bash

# Setup script for Legacy Application Modernization Assessment Framework
# This script installs all required dependencies

echo "Setting up Legacy Application Modernization Assessment Framework..."
echo "Installing required Python packages..."

pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Setup completed successfully!"
    echo "You can now run 'mkdocs serve' to start the documentation server"
    echo ""
    echo "📋 New team members: Please review the onboarding documentation:"
    echo "   - docs/governance.md - See the 'Assessment Team Onboarding' section"
    echo "   - docs/onboarding-checklist.md - Complete this checklist during onboarding"
    echo "   - docs/troubleshooting.md - Reference for common installation issues"
else
    echo "❌ Error installing dependencies. Please check your Python environment and try again."
    exit 1
fi
