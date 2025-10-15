#!/usr/bin/env python3
"""
Python script to create a simple C# project
Created by: Cline AI Assistant
"""

import os
import sys


def load_template(template_path, project_name, framework_version=None):
    """
    Load template file and replace placeholders with project name and framework version

    Args:
        template_path (str): Path to the template file
        project_name (str): Name of the project to replace in template
        framework_version (str): .NET framework version to use (optional)

    Returns:
        str: Processed template content with placeholders replaced
    """
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('{PROJECT_NAME}', project_name)
        if framework_version:
            content = content.replace('{FRAMEWORK_VERSION}', framework_version)
        return content
    except Exception as e:
        print(f"❌ Error loading template {template_path}: {e}")
        return None


def get_installed_sdks():
    """
    Get list of installed .NET SDKs

    Returns:
        list: List of installed SDK versions, or None if error
    """
    try:
        import subprocess
        result = subprocess.run(['dotnet', '--list-sdks'],
                              capture_output=True, text=True, check=True)
        sdks = []
        for line in result.stdout.strip().split('\n'):
            if line.strip():
                # Extract version number (first part before space)
                version = line.strip().split()[0]
                # Convert to short format (e.g., 7.0.100 -> net7.0)
                version_parts = version.split('.')
                if len(version_parts) >= 2:
                    short_version = f"net{version_parts[0]}.{version_parts[1]}"
                    if short_version not in sdks:
                        sdks.append(short_version)
        return sorted(sdks) if sdks else None
    except (subprocess.CalledProcessError, FileNotFoundError, Exception):
        return None


def select_framework():
    """
    Allow user to select .NET framework version

    Returns:
        str: Selected framework version, or default if none available
    """
    installed_sdks = get_installed_sdks()

    if not installed_sdks:
        print("⚠️  No .NET SDKs detected, using default framework (net7.0)")
        return "net7.0"

    print("\n📋 Available .NET Framework Versions:")
    for i, sdk in enumerate(installed_sdks, 1):
        print(f"  {i}. {sdk}")

    while True:
        try:
            choice = input(f"\nSelect framework (1-{len(installed_sdks)}) or press Enter for default (net7.0): ").strip()
            if not choice:
                return "net7.0"
            choice_num = int(choice)
            if 1 <= choice_num <= len(installed_sdks):
                return installed_sdks[choice_num - 1]
            else:
                print(f"Please enter a number between 1 and {len(installed_sdks)}")
        except ValueError:
            print("Please enter a valid number")


def create_csharp_project():
    """
    Create a simple C# project with:
    - Program.cs file with "Hello World" content
    - README.md file with project name
    - Basic .csproj file
    """

    # Get project name from user
    project_name = input("Enter C# project name: ").strip()

    if not project_name:
        print("❌ Project name cannot be empty!")
        return False

    # Select .NET framework version
    framework_version = select_framework()
    print(f"🎯 Selected framework: {framework_version}")

    # Create project directory
    project_dir = project_name
    try:
        os.makedirs(project_dir, exist_ok=True)
        print(f"📁 Created directory: {project_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return False

    # Get template directory path
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')

    # Create Program.cs file from template
    program_template_path = os.path.join(template_dir, 'Program.cs.template')
    program_cs_content = load_template(program_template_path, project_name, framework_version)

    if program_cs_content is None:
        return False

    program_cs_path = os.path.join(project_dir, "Program.cs")
    try:
        with open(program_cs_path, 'w', encoding='utf-8') as f:
            f.write(program_cs_content)
        print(f"✅ Created file: Program.cs")
    except Exception as e:
        print(f"❌ Error creating Program.cs file: {e}")
        return False

    # Create README.md file from template
    readme_template_path = os.path.join(template_dir, 'README.md.template')
    readme_content = load_template(readme_template_path, project_name, framework_version)

    if readme_content is None:
        return False

    readme_path = os.path.join(project_dir, "README.md")
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"✅ Created file: README.md")
    except Exception as e:
        print(f"❌ Error creating README.md file: {e}")
        return False

    # Create .csproj file from template
    csproj_template_path = os.path.join(template_dir, 'project.csproj.template')
    csproj_content = load_template(csproj_template_path, project_name, framework_version)

    if csproj_content is None:
        return False

    csproj_path = os.path.join(project_dir, f"{project_name}.csproj")
    try:
        with open(csproj_path, 'w', encoding='utf-8') as f:
            f.write(csproj_content)
        print(f"✅ Created file: {project_name}.csproj")
    except Exception as e:
        print(f"❌ Error creating .csproj file: {e}")
        return False

    print(f"\n🎉 Project '{project_name}' has been created successfully!")
    print(f"📂 Project directory: {os.path.abspath(project_dir)}")
    print("\nTo run the project:")
    print(f"   cd {project_dir}")
    print("   dotnet run")

    return True


def main():
    """
    Main function
    """
    print("🚀 Create Simple C# Project")
    print("=" * 40)

    try:
        success = create_csharp_project()
        if success:
            print("\n✅ Complete! Project is ready to use.")
        else:
            print("\n❌ An error occurred during project creation.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⏹️  Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
