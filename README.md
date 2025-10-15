# .NET Kickstart

A powerful Python script that automates the creation of C# console applications with customizable templates and framework selection.

## 🚀 Features

- **Interactive Project Creation** - Simple command-line interface for creating C# projects
- **Framework Selection** - Automatically detects and allows selection from installed .NET SDKs
- **Template-Based Architecture** - Clean separation of templates for easy customization
- **Multi-Language Support** - Originally created in Vietnamese, now fully in English
- **Error Handling** - Robust error handling with user-friendly messages
- **Template Customization** - Easy to modify project structure and content

## 📋 Requirements

- Python 3.6 or higher
- .NET SDK (any version - the tool will detect installed versions)
- Terminal/Command prompt access

## 🛠️ Installation

1. Clone or download the project files
2. Ensure `create_csharp_project.py` is executable:
   ```bash
   chmod +x create_csharp_project.py
   ```
3. Verify .NET SDK is installed:
   ```bash
   dotnet --version
   ```

## 📖 Usage

### Basic Usage

Run the script from the terminal:
```bash
python3 create_csharp_project.py
```

### Interactive Flow

1. **Enter Project Name**: Provide a name for your new C# project
2. **Select Framework**: Choose from detected .NET SDKs or use default (net7.0)
3. **Project Creation**: The tool creates a complete project structure

### Example Session

```bash
$ python3 create_csharp_project.py
🚀 Create Simple C# Project
========================================
Enter C# project name: MyAwesomeApp

📋 Available .NET Framework Versions:
  1. net6.0
  2. net7.0
  3. net8.0

Select framework (1-3) or press Enter for default (net7.0): 2
🎯 Selected framework: net7.0
📁 Created directory: MyAwesomeApp
✅ Created file: Program.cs
✅ Created file: README.md
✅ Created file: MyAwesomeApp.csproj

🎉 Project 'MyAwesomeApp' has been created successfully!
📂 Project directory: /path/to/MyAwesomeApp

To run the project:
   cd MyAwesomeApp
   dotnet run

✅ Complete! Project is ready to use.
```

## 📁 Project Structure

After running the tool, your project will have this structure:

```
MyProject/
├── Program.cs          # Main C# source file
├── README.md           # Project documentation
└── MyProject.csproj    # .NET project file
```

### Generated Files

#### Program.cs
```csharp
using System;

namespace MyProject
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World from MyProject!");
        }
    }
}
```

#### MyProject.csproj
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net7.0</TargetFramework>
    <RootNamespace>MyProject</RootNamespace>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
```

## ⚙️ Configuration

### Template Customization

The tool uses template files located in the `templates/` directory:

- `templates/Program.cs.template` - Main source code template
- `templates/README.md.template` - Documentation template
- `templates/project.csproj.template` - Project file template

### Template Variables

- `{PROJECT_NAME}` - Replaced with the user-provided project name
- `{FRAMEWORK_VERSION}` - Replaced with selected .NET framework version

### Customizing Templates

To customize generated files, edit the template files:

1. Modify `templates/Program.cs.template` for different starter code
2. Update `templates/README.md.template` for custom documentation
3. Edit `templates/project.csproj.template` for different project settings

## 🔧 Advanced Features

### Framework Detection

The tool automatically detects installed .NET SDKs using:
```bash
dotnet --list-sdks
```

Detected frameworks are presented as numbered options during project creation.

### Default Framework

If no framework is selected (user presses Enter), the tool defaults to `net7.0`.

### Error Handling

The tool includes comprehensive error handling for:
- Missing project names
- Template file errors
- Directory creation failures
- .NET SDK detection issues

## 🐛 Troubleshooting

### Common Issues

**Issue**: No .NET SDKs detected
```
⚠️  No .NET SDKs detected, using default framework (net7.0)
```
**Solution**: Install a .NET SDK or verify `dotnet` command is available in PATH

**Issue**: Template files not found
```
❌ Error loading template templates/Program.cs.template: [Errno 2] No such file or directory
```
**Solution**: Ensure the `templates/` directory exists and contains the required template files

**Issue**: Permission denied creating directory
```
❌ Error creating directory: [Errno 13] Permission denied: 'ProjectName'
```
**Solution**: Run the script from a directory where you have write permissions

### Getting Help

If you encounter issues:
1. Check that all requirements are met
2. Verify file permissions
3. Ensure .NET SDK is properly installed
4. Check the templates directory exists

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Created with Cline AI Assistant
- Supports multiple .NET framework versions
- Template-based architecture for maintainability

---

**Happy Coding!** 🎉
