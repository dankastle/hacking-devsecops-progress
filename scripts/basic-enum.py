#!/usr/bin/env python3
import subprocess
import argparse
import os

def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"

def main():
    parser = argparse.ArgumentParser(description="Basic Linux Enumeration Tool - Día 1")
    parser.add_argument("--target", default="localhost", help="Host o VM GCP")
    args = parser.parse_args()

    print("🔍 Enumeración básica - Día 1 Hacking")
    print("="*50)
    
    checks = {
        "Usuarios con sudo": "cat /etc/group | grep sudo",
        "SSH keys expuestas": "ls -la ~/.ssh/",
        "Procesos privilegiados": "ps aux | grep root",
        "Puertos abiertos": "ss -tuln",
        "Versiones kernel": "uname -a"
    }
    
    for name, cmd in checks.items():
        print(f"\n📌 {name}:")
        print(run_command(cmd))
    
    print("\n✅ Script terminado. Guarda este output en tu GCP VM mañana.")

if __name__ == "__main__":
    main()
