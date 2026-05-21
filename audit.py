#!/usr/bin/env python3
"""
TeamPCP GitHub Breach VS Code Extension Auditor
2026/5/21 - Simple, dependency-free Python script
Detects the known malicious Nx Console v18.95.0 (and other TeamPCP-related extensions)
Author: Community Response Tool - Feel free to fork & improve
"""

import os
import json
import platform
from pathlib import Path
from typing import Dict, List

# ====================== KNOWN MALICIOUS EXTENSIONS (2026 TeamPCP campaign) ======================
KNOWN_MALICIOUS: Dict[str, List[str]] = {
    # GitHub breach vector (confirmed / strongly suspected)
    "nrwl.angular-console": ["18.95.0"],          # Nx Console - poisoned version (May 18, live ~11min)
    
    # Previous TeamPCP waves (for completeness)
    "checkmarx.ast-results": ["2.53.0"],
    "checkmarx.cx-dev-assist": ["1.7.0"],
}

def get_vscode_extensions_path() -> Path:
    """Cross-platform VS Code extensions directory"""
    system = platform.system()
    if system == "Windows":
        return Path(os.environ.get("USERPROFILE", "")) / ".vscode" / "extensions"
    else:
        # macOS & Linux
        return Path.home() / ".vscode" / "extensions"

def audit_extensions() -> None:
    extensions_path = get_vscode_extensions_path()
    
    print("🔍 TeamPCP GitHub Breach - VS Code Extension Auditor")
    print("=" * 70)
    print(f"📂 Scanning: {extensions_path}\n")
    
    if not extensions_path.exists():
        print("❌ VS Code extensions directory not found. Nothing to audit.")
        return
    
    suspicious: List[str] = []
    total = 0
    
    for ext_dir in extensions_path.iterdir():
        if not ext_dir.is_dir():
            continue
            
        package_json = ext_dir / "package.json"
        if not package_json.exists():
            continue
            
        try:
            with open(package_json, encoding="utf-8") as f:
                data = json.load(f)
            
            publisher = data.get("publisher", {}).get("name", "unknown")
            name = data.get("name", "unknown")
            version = data.get("version", "unknown")
            full_id = f"{publisher}.{name}"
            
            total += 1
            # print(f"✅ {full_id} v{version}") # Optional: Uncomment to see all extensions
            
            if full_id in KNOWN_MALICIOUS and version in KNOWN_MALICIOUS[full_id]:
                suspicious.append(f"{full_id} v{version} ← MALICIOUS (TeamPCP)")
                
        except Exception:
            continue
    
    print("\n" + "=" * 70)
    print(f"📊 Total extensions scanned: {total}")
    
    if suspicious:
        print("\n🚨 🚨 CRITICAL FINDINGS 🚨 🚨")
        for item in suspicious:
            print(f"   • {item}")
        print("\n⚠️  ASSUME BREACH!")
        print("   → Immediately rotate ALL secrets (GitHub PAT, SSH keys, AWS, 1Password, etc.)")
        print("   → Uninstall the extension(s) above")
        print("   → Consider full device wipe / credential reset if you opened workspaces recently")
    else:
        print("\n✅ No known TeamPCP malicious extensions detected.")
        print("   Still recommended: Review extensions manually + rotate secrets as GitHub advised.")
    
    print("\n🛡️  Next steps (GitHub official + community best practice):")
    print("   1. Rotate all GitHub tokens / SSH keys / cloud credentials NOW")
    print("   2. Disable auto-update for extensions temporarily")
    print("   3. Use only verified publishers")

if __name__ == "__main__":
    audit_extensions()