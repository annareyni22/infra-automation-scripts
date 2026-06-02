#!/bin/bash

echo "Disk Usage Report"
df -h

echo ""
echo "Top 10 Largest Directories"

du -sh /* 2>/dev/null | sort -hr | head -10
