# TeamPCP VS Code Extension Auditor

> **Simple. Fast. Zero dependencies.**  
> Python auditor for the **2026 GitHub TeamPCP VS Code extension breach** (Nx Console v18.95.0).  
> One file. Runs in seconds. Helps thousands of developers check their machines **right now**.

---

## The Problem (Why This Matters)

On **May 19-20, 2026**, GitHub confirmed that a **poisoned VS Code extension** (`nrwl.angular-console` v18.95.0) compromised a developer’s machine, leading to the theft of **~3,800 internal repositories**.

This was a **supply-chain attack via a developer tool** that millions use daily.

**Core threat:** A single click or auto-update can expose your organization’s entire source code.  
**Assume Breach** is the new baseline.

## Quick Start (No Clone Needed)

```bash
# 1. Download
curl -O https://raw.githubusercontent.com/kobayashikazu/teampcp-vscode-auditor/main/audit.py

# 2. Run
python3 audit.py
