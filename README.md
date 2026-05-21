# TeamPCP VS Code Extension Auditor

> Simple Python auditor for the 2026 GitHub TeamPCP VS Code extension breach (Nx Console v18.95.0).
> One file. No dependencies. Runs in seconds. Helps thousands of developers check their machines right now.

## The Problem
On May 2026, GitHub confirmed that a poisoned VS Code extension (`nrwl.angular-console` v18.95.0) compromised a developer's device, leading to the exfiltration of approximately 3,800 internal repositories. This script detects if your local environment contains the malicious payload from this TeamPCP campaign or previous waves (like Checkmarx).

**The essence of the threat:** A single click on a developer tool can compromise an entire organization's source code. A "Zero Trust / Assume Breach" mindset is strictly required.

## Usage

You do not need to clone the repository. Run it directly:

```bash
# 1. Download
curl -O [https://raw.githubusercontent.com/YOURNAME/teampcp-vscode-auditor/main/audit.py](https://raw.githubusercontent.com/YOURNAME/teampcp-vscode-auditor/main/audit.py)

# 2. Run
python3 audit.py