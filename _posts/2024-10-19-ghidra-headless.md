---
layout: post
title: Ghidra's Headless Analyzer
description: RE faster.
tag: [ghidra, reverse engineering]
---

Say you are beginning a new project to pentest an embedded device, and you're able to get a copy of firmware and get access to the filesystem on the device. At this point, there may be a number of reasons you'd want to import all the executables and libraries into a ghidra project:

- The device uses a lot of custom libraries. In order to resolve calls to functions from these libraries in ghidra, you'll need to import the libraries into your ghidra project, which would take very long to do manually.
- You have a guess as to how some of the devices funtionality is implemented, but would like to avoid manually opening up every binary/library in ghidra in order to see if the file has what you're looking for (eg a bind to a certain port, calls to a particular library, etc).
- There are files you'd like to inspect with ghidra, but you don't want to have to wait for ghidra to analyze each file when you open each for the first time.

All these problems can be solved with ghidra's headless analyzer, which can **import**, **analyze**, and **execute scripts** on entire directories of files.

The ability to execute a ghidra script on all the binareis from a devices is particularly powerful. You can do things like:

- search every binary to for a partiuclar function that has particular arguments (as in actual argument values, not just a function prototype)
- search every binary for historically unsafe functions 
- do tasks that may be difficult to do at scale or at all from the linux command line 

### Usage

The headless anaylzer binary, `analyzeHeadless`, is in the `support` directory of the unzipped [ghidra zip file](https://github.com/NationalSecurityAgency/ghidra/releases). Instructions to use it are in the same directory in `analyzeHeadlessREADME.html`, or you can read them online [here](https://static.grumpycoder.net/pixel/support/analyzeHeadlessREADME.html).

Those instructions are well written and have all the info you need to use `analyzeHeadless`, but here are some common actions for easy reference:

- recursively import a directory into a project:


```bash
./analyzeHeadless <ghidra_project_path> -import <directory_path> <project_name> -recursive
```

- run a custom script called `myScript.java` on all files in a ghidra project

```bash
./analyzeHeadless <ghidra_project_path> -process -portScript myScript.java

# path to `myScript.java` is not needed;
# analyzer will search the default ghidra script location
```

        
> Tip: In addition to being able to import files and directories, you can also provide a path to a zip file and the analyzer will go through all the file therein. This can be particularly useful when zipping a filesystem; normally if the analyzer encounters a symlink when importing binaries, it follows the symlink and imports the symlink target. This can cause unwanted extra imports (eg. many imports of busybox under many different names). However, when parsing a zip file, the anaylzer will treat the symlinks like any other non-binary file and skip it.
{: .prompt-tip}

